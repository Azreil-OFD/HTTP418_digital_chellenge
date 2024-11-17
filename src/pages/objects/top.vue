<template>
  <div class="p-5">
    <ButtonGroup>
      <Button @click="setField('debit')" label="Debit" :variant="selectedField === 'debit' ? 'outlined' : ''"></Button>
      <Button @click="setField('ee_consume')" label="EE Consume"
        :variant="selectedField === 'ee_consume' ? 'outlined' : ''"></Button>
      <Button @click="setField('expenses')" label="Expenses"
        :variant="selectedField === 'expenses' ? 'outlined' : ''"></Button>
      <Button @click="setField('pump_operating')" label="Pump Operating"
        :variant="selectedField === 'pump_operating' ? 'outlined' : ''"></Button>
    </ButtonGroup>
    <DataTable :value="tops" class="w-full" :rows="10" responsive-layout="scroll" row-hover>
      <Column field="id" header="ID" />
      <Column field="name" header="Скважина" />
      <Column field="value" header="Дебет (m³)" />
      <Column field="units" header="Единицы" />
    </DataTable>
  </div>
</template>

<script setup>

const tops = ref([]);
const selectedField = ref('debit')
const setField = async (name) => {
  selectedField.value = name
  await fetchTops(name)
} 
const fetchTops = async (name = 'debit') => {
  const response = await fetch(
    '/api/objects/tops/?order_field=' + name + '&order_direction=asc&date_from=2024-01-01&date_to=2024-12-31&counts=10',
    {
      headers: {
        Authorization: 'Bearer ' + localStorage.getItem('token'),
      },
    }
  );
  tops.value = await response.json();
};

onMounted(async () => {
  await fetchTops();
});
</script>

<style scoped></style>
