<template>
  <div class="card">

    <Statistic></Statistic>
    <br>
    <DataTable v-model:filters="filters" :value="data" :rows="10" dataKey="date" filterDisplay="row" :loading="loading"
      :globalFilterFields="['date', 'debit', 'ee_consume', 'expenses', 'pump_operating']">
      <template #empty> No records found. </template>
      <template #loading> Loading data. Please wait. </template>
      <template #header>
        <div class="flex gap-4">
          <FloatLabel class="w-full md:w-56">
            <Select v-model="selectField" inputId="over_label" :options="selectsFields" optionLabel="name"
              class="w-full" />
            <label for="over_label">Sorted by...</label>
          </FloatLabel>
          <Button :icon="`pi ${sortDirection !== 'asc' ? 'pi-arrow-up' : 'pi-arrow-down'}`" @click="() => {
            sortDirection === 'asc' ? sortDirection = 'desc' : sortDirection = 'asc'
          }" aria-label="Save" />
        </div>
      </template>
      <Column field="date" header="Date" style="min-width: 12rem">
        <template #body="{ data }">
          {{ data.date }}
        </template>
      </Column>
      <Column field="debit" header="Debit" style="min-width: 12rem">
        <template #body="{ data }">
          <span :style="{ 'color': data.plan.debit > data.debit ? 'red' : 'green' }">{{ data.debit }} </span>
          ( {{ data.plan.debit }} ) m³
        </template>
      </Column>
      <Column field="ee_consume" header="Energy Consumption" style="min-width: 12rem">
        <template #body="{ data }">
          <span :style="{ 'color': data.plan.ee_consume > data.ee_consume ? 'red' : 'green' }">{{
            data.ee_consume.toFixed(2) }} </span>
          ( {{ data.plan.ee_consume.toFixed(2) }} ) kWh
        </template>
      </Column>
      <Column field="expenses" header="Expenses" style="min-width: 12rem">
        <template #body="{ data }">
          <span :style="{ 'color': data.plan.expenses > data.expenses ? 'red' : 'green' }">{{ data.expenses.toFixed(2)
            }} </span>
          ( {{ data.plan.expenses.toFixed(2) }} ) c.u.
        </template>
      </Column>
      <Column field="pump_operating" header="Pump Operating" style="min-width: 12rem">
        <template #body="{ data }">
          <span :style="{ 'color': data.plan.pump_operating > data.pump_operating ? 'red' : 'green' }">{{
            data.pump_operating.toFixed(2) }} </span>
          ( {{ data.plan.pump_operating }} ) c.u.
        </template>
      </Column>
      <template #footer>
        <Paginator v-model:first="page" :rows="1" :totalRecords="totalPage"
          template="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink" />
      </template>
    </DataTable>


  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { FilterMatchMode } from '@primevue/core/api';
const route = useRoute()

const selectField = ref({ name: 'Date', code: 'date_add' });
const selectsFields = ref([
  { name: 'Date', code: 'date_add' },
  { name: 'Debit', code: 'debit' },
  { name: 'Energy Consumption', code: 'ee_consume' },
  { name: 'Expenses', code: 'expenses' },
  { name: 'Pump Operating', code: 'pump_operating' }
]);

const data = ref([]);
const dataPlan = ref([]);
const totalPage = ref(1)
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  date: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
  debit: { value: null, matchMode: FilterMatchMode.EQUALS },
  ee_consume: { value: null, matchMode: FilterMatchMode.EQUALS },
  expenses: { value: null, matchMode: FilterMatchMode.EQUALS },
  pump_operating: { value: null, matchMode: FilterMatchMode.EQUALS }
});

const sortDirection = ref('asc')
// Загрузка данных (замените на ваш API-запрос)
onMounted(async () => {


  const responsePlan = await fetch(`/api/objects/search/?obj_id=${route.params.id}&order_direction=asc&page=${page.value + 1}&per_page=10&mode=plan`, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
      "Authorization": 'Bearer ' + localStorage.getItem('token')
    }
  });

  const resultPlan = await responsePlan.json()
  dataPlan.value = resultPlan.data;

  const response = await fetch(`/api/objects/search/?obj_id=${route.params.id}&order_direction=asc&page=${page.value + 1}&per_page=10&mode=history`, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
      "Authorization": 'Bearer ' + localStorage.getItem('token')

    }
  });
  const result = await response.json()
  data.value = result.data.map((e, i) => {
    e.plan = resultPlan.data[i]
    return e
  });
  totalPage.value = result.meta.total_page;
});

const page = ref(0);

const updatePage = async (sort = 'asc', order_field = '') => {
  const responsePlan = await fetch(`/api/objects/search/?obj_id=${route.params.id}${selectField.value.code !== '' ? `&order_field=${selectField.value.code}` : ''}&order_direction=${sortDirection.value}&page=${page.value + 1}&per_page=10&mode=plan`, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
      "Authorization": 'Bearer ' + localStorage.getItem('token')
    }
  });

  const resultPlan = await responsePlan.json()
  dataPlan.value = resultPlan.data;

  const response = await fetch(`/api/objects/search/?obj_id=${route.params.id}${selectField.value.code !== '' ? `&order_field=${selectField.value.code}` : ''}&order_direction=${sortDirection.value}&page=${page.value + 1}&per_page=10&mode=history`, {
    method: 'GET',
    headers: {
      'accept': 'application/json',
      "Authorization": 'Bearer ' + localStorage.getItem('token')
    }
  });
  const result = await response.json()
  data.value = result.data.map((e, i) => {
    e.plan = resultPlan.data[i]
    return e
  });
}
watch([page, sortDirection, selectField], async () => {
  await updatePage()
})
</script>
