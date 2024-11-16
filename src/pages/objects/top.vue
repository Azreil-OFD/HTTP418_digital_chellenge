<template>
  <div class="card">
      <DataTable v-model:filters="filters" :value="dataEntries" paginator showGridlines :rows="10" dataKey="date"
              filterDisplay="menu" :loading="loading" :globalFilterFields="['date', 'debit', 'ee_consume', 'expenses', 'pump_operating']">
          <template #header>
              <div class="flex justify-between">
                  <Button type="button" icon="pi pi-filter-slash" label="Clear" outlined @click="clearFilter()" />
                  <IconField>
                      <InputIcon>
                          <i class="pi pi-search" />
                      </InputIcon>
                      <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                  </IconField>
              </div>
          </template>
          <template #empty> No data found. </template>
          <template #loading> Loading data. Please wait. </template>
          <Column field="date" header="Date" dataType="date" style="min-width: 10rem">
              <template #body="{ data }">
                  {{ formatDate(data.date) }}
              </template>
              <template #filter="{ filterModel }">
                  <DatePicker v-model="filterModel.value" dateFormat="mm/dd/yy" placeholder="mm/dd/yyyy" />
              </template>
          </Column>
          <Column field="debit" header="Debit" dataType="numeric" style="min-width: 10rem">
              <template #body="{ data }">
                  {{ formatCurrency(data.debit) }}
              </template>
              <template #filter="{ filterModel }">
                  <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
              </template>
          </Column>
          <Column field="ee_consume" header="EE Consume" dataType="numeric" style="min-width: 10rem">
              <template #body="{ data }">
                  {{ formatCurrency(data.ee_consume) }}
              </template>
              <template #filter="{ filterModel }">
                  <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
              </template>
          </Column>
          <Column field="expenses" header="Expenses" dataType="numeric" style="min-width: 10rem">
              <template #body="{ data }">
                  {{ formatCurrency(data.expenses) }}
              </template>
              <template #filter="{ filterModel }">
                  <InputNumber v-model="filterModel.value" mode="currency" currency="USD" locale="en-US" />
              </template>
          </Column>
          <Column field="pump_operating" header="Pump Operating" dataType="numeric" style="min-width: 10rem">
              <template #body="{ data }">
                  {{ data.pump_operating }}
              </template>
              <template #filter="{ filterModel }">
                  <InputNumber v-model="filterModel.value" mode="decimal" locale="en-US" />
              </template>
          </Column>
      </DataTable>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { DataService } from '@/service/DataService'; // Измените на свой сервис
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';

const dataEntries = ref([]);
const filters = ref({});
const loading = ref(true);

onMounted(() => {
  DataService.getDataEntries().then((data) => {
      dataEntries.value = getDataEntries(data);
      loading.value = false;
  });
});

const initFilters = () => {
  filters.value = {
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      date: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.DATE_IS }] },
      debit: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
      ee_consume: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
      expenses: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
      pump_operating: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] }
  };
};

initFilters();

const formatDate = (value) => {
  return new Date(value).toLocaleDateString('en-US', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
  });
};

const formatCurrency = (value) => {
  return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
};

const clearFilter = () => {
  initFilters();
};

const getDataEntries = (data) => {
  return [...(data || [])].map((d) => {
      d.date = new Date(d.date);
      return d;
  });
};
</script>
