<template>
  <div>
      <div class="card">
          <Chart type="line" :data="chartData" :options="chartOptions" class="h-[30rem]" />
      </div>
      <div class="flex justify-center mt-4">
          <button @click="setField('debit')" class="btn">Debit</button>
          <button @click="setField('ee_consume')" class="btn">EE Consume</button>
          <button @click="setField('expenses')" class="btn">Expenses</button>
          <button @click="setField('pump_operating')" class="btn">Pump Operating</button>
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";

const props = defineProps({
  dates: {
      type: Array,
      default: () => []
  }
});

const chartData = ref();
const chartOptions = ref();
const selectedField = ref('debit');

const fetchData = async (mode) => {
  const response = await fetch(`/api/objects/search/?obj_id=111&order_field=date_add&order_direction=asc&page=1&per_page=50&mode=${mode}`);
  return await response.json();
};

const updateChartData = async () => {
  const historyData = await fetchData('history');
  const planData = await fetchData('plan');

  const labels = historyData.map(item => item.date);
  const historyValues = historyData.map(item => item[selectedField.value]);
  const planValues = planData.map(item => item[selectedField.value]);

  // Фильтрация данных в зависимости от выбранных дат
  const filteredHistory = filterDataByDate(historyData);
  const filteredPlan = filterDataByDate(planData);

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
