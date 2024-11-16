<template>
  <div class="card">
      <DataTable v-model:filters="filters" :value="data" paginator :rows="10" dataKey="date" filterDisplay="row" :loading="loading"
              :globalFilterFields="['date', 'debit', 'ee_consume', 'expenses', 'pump_operating']">
          <template #header>
              <div class="flex justify-end">
                  <IconField>
                      <InputIcon>
                          <i class="pi pi-search" />
                      </InputIcon>
                      <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                  </IconField>
              </div>
          </template>
          <template #empty> No records found. </template>
          <template #loading> Loading data. Please wait. </template>
          <Column field="date" header="Date" style="min-width: 12rem">
              <template #body="{ data }">
                  {{ data.date }}
              </template>
              <template #filter="{ filterModel, filterCallback }">
                  <InputText v-model="filterModel.value" type="text" @input="filterCallback()" placeholder="Search by date" />
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
      </DataTable>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { FilterMatchMode } from '@primevue/core/api';
const route = useRoute()

const data = ref([]);
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
  const response = await fetch(`http://127.0.0.1:3000/api/api/objects/search/?obj_id=${route.params.id}&order_field=name&order_direction=asc&page=1&per_page=50&mode=history`, {
      method: 'GET',
      headers: {
          'accept': 'application/json'
      }
  });
  data.value = await response.json();
});
</script>


