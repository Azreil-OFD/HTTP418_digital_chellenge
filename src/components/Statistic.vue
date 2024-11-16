<template>
  <div>
    <div class="flex" style="justify-content: space-between; align-items: center;">
      <div v-if="naming">
        {{ naming.type }}
      {{ naming.name }}
      </div>
      <ButtonGroup>
        <Button @click="setField('debit')" label="Debit"
          :variant="selectedField === 'debit' ? 'outlined' : ''"></Button>
        <Button @click="setField('ee_consume')" label="EE Consume"
          :variant="selectedField === 'ee_consume' ? 'outlined' : ''"></Button>
        <Button @click="setField('expenses')" label="Expenses"
          :variant="selectedField === 'expenses' ? 'outlined' : ''"></Button>
        <Button @click="setField('pump_operating')" label="Pump Operating"
          :variant="selectedField === 'pump_operating' ? 'outlined' : ''"></Button>
      </ButtonGroup>
    </div>
    <div class="card">
      <Chart type="line" :data="chartData" :options="chartOptions" class="h-[30rem]" />
    </div>
    Select range
    <Slider v-model="pickDate" :max="maxPickDate" range class="w-fill mt-5" />
    <div class="flex justify-center mt-4">

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
const pickDate = ref([0, 100]);
const maxPickDate = ref(100)  

const props = defineProps({
  dates: {
    type: Array,
    default: () => []
  }
});
const route = useRoute()
const chartData = ref();
const chartOptions = ref();
const selectedField = ref('debit');
const naming = ref('')
let historyData = []
let planData = []
const fetchData = async (mode) => {
  const response = await fetch(`/api/objects/search/?obj_id=${route.params.id}&order_field=date_add&order_direction=asc&page=1&per_page=1600&mode=${mode}`);
  return (await response.json()).data;
};
onMounted(async () => {
  historyData = await fetchData('history');
  planData = await fetchData('plan');
  setField('debit')
  pickDate.value[1] = historyData.length
  maxPickDate.value = historyData.length

  const getWells = await fetch(`/api/objects/object/${route.params.id}`)
  naming.value = await getWells.json()
})
watch(pickDate, async () => {
  await updateChartData()
})
const updateChartData = async () => {
  const labels = historyData.map(item => item.date).slice(pickDate.value[0], pickDate.value[1]);
  const historyValues = historyData.map(item => item[selectedField.value]);
  const planValues = planData.map(item => item[selectedField.value]);

  // Фильтрация данных в зависимости от выбранных дат
  const filteredHistory = filterDataByDate(historyData).slice(pickDate.value[0], pickDate.value[1]);
  const filteredPlan = filterDataByDate(planData).slice(pickDate.value[0], pickDate.value[1]);

  chartData.value = {
    labels: labels,
    datasets: [
      {
        label: 'Historical Data',
        data: filteredHistory,
        fill: false,
        tension: 0.4,
        borderColor: 'blue'
      },
      {
        label: 'Planned Data',
        data: filteredPlan,
        fill: false,
        borderDash: [5, 5],
        tension: 0.4,
        borderColor: 'orange'
      }
    ]
  };
};

const filterDataByDate = (data) => {
  if (props.dates.length === 0) {
    return data.map(item => item[selectedField.value]);
  } else if (props.dates.length === 1) {
    const selectedDate = new Date(props.dates[0]);
    return data
      .filter(item => new Date(item.date) <= new Date())
      .map(item => item[selectedField.value]);
  } else if (props.dates.length === 2) {
    const startDate = new Date(props.dates[0]);
    const endDate = new Date(props.dates[1]);
    return data
      .filter(item => {
        const itemDate = new Date(item.date);
        return itemDate >= startDate && itemDate <= endDate;
      })
      .map(item => item[selectedField.value]);
  }
  return [];
};

const setField = (field) => {
  selectedField.value = field;
  updateChartData();
};

onMounted(() => {
  chartOptions.value = setChartOptions();
  updateChartData();
});

const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  const textColor = documentStyle.getPropertyValue('--p-text-color');
  const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color');
  const surfaceBorder = documentStyle.getPropertyValue('--p-content-border-color');

  return {
    maintainAspectRatio: false,
    aspectRatio: 0.6,
    plugins: {
      legend: {
        labels: {
          color: textColor
        }
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      },
      y: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      }
    }
  };
};
</script>

<style scoped>
.card {
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  margin: 1rem 0;
}

.btn {
  @apply bg-blue-500 text-white font-bold py-2 px-4 rounded mx-2;
}
</style>
