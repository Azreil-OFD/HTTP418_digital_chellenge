<template>
  <div class="card">
    <Statistic></Statistic>
    <br>
      <DataTable v-model:filters="filters" :value="data" :rows="10" dataKey="date" filterDisplay="row" :loading="loading"
              :globalFilterFields="['date', 'debit', 'ee_consume', 'expenses', 'pump_operating']">

          <template #empty> No records found. </template>
          <template #loading> Loading data. Please wait. </template>
          <Column field="date" header="Date" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.date }}
              </template>
          </Column>
          <Column field="debit" header="Debit" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.debit }}
              </template>
          </Column>
          <Column field="ee_consume" header="Energy Consumption" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.ee_consume.toFixed(2) }}
              </template>
          </Column>
          <Column field="expenses" header="Expenses" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.expenses.toFixed(2) }}
              </template>
          </Column>
          <Column field="pump_operating" header="Pump Operating" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.pump_operating }}
              </template>
          </Column>
          <template #footer> 
            <Paginator v-model:first="page" :rows="1" :totalRecords="totalPage" template="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink" />
             </template>
      </DataTable>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { FilterMatchMode } from '@primevue/core/api';
const route = useRoute()

const data = ref([]);
const totalPage = ref(1)
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  date: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
  debit: { value: null, matchMode: FilterMatchMode.EQUALS },
  ee_consume: { value: null, matchMode: FilterMatchMode.EQUALS },
  expenses: { value: null, matchMode: FilterMatchMode.EQUALS },
  pump_operating: { value: null, matchMode: FilterMatchMode.EQUALS }
});

// Загрузка данных (замените на ваш API-запрос)
onMounted(async () => {
  const response = await fetch(`/api/objects/search/?obj_id=${route.params.id}&order_direction=asc&page=${page.value +1}&per_page=10&mode=history`, {
      method: 'GET',
      headers: {
          'accept': 'application/json'
      }
  });
  const result = await response.json()
  data.value = result.data;
  totalPage.value = result.meta.total_page
});

const page = ref(0);
watch(page , async ( ) => {
  const response = await fetch(`/api/objects/search/?obj_id=${route.params.id}&order_direction=asc&page=${page.value +1}&per_page=10&mode=history`, {
      method: 'GET',
      headers: {
          'accept': 'application/json'
      }
  });
  const result = await response.json()
  data.value = result.data;
})
</script>


