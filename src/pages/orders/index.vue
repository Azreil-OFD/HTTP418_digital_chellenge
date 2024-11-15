
<template>
    <div class="card">
        <DataTable :value="orders" tableStyle="min-width: 50rem">
            <template #header>
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="text-xl font-bold">Orders</span>
                    <Button icon="pi pi-refresh" rounded raised />
                </div>
            </template>
            <Column field="name" header="Name"></Column>
            <Column header="Image">
                <template #body="slotProps">
                    <img :src="`${slotProps.data.image}`" :alt="slotProps.data.image" class="w-24 rounded" />
                </template>
            </Column>
            <Column field="description" header="Description"></Column>

            <template #footer> In total there are {{ orders ? orders.length : 0 }} orders. </template>
        </DataTable>
    </div>
</template>

<script setup>
const orders = ref({
    
});
</script>
