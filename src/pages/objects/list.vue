<template>
    <div class="card">
        <div class="card flex justify-center">
            <Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Select a City"
                class="w-full md:w-56" @change="onPageChange()" />
        </div>
        <DataTable :value="products" @row-click="(e) => { navigateTo(`/objects/select/${e.data.id}`) }" paginator
            :rows="10" :rowsPerPageOptions="[10, 20, 50]" tableStyle="min-width: 50rem"
            paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
            currentPageReportTemplate="{first} to {last} of {totalRecords}">
            <template #paginatorstart>
                <Button type="button" icon="pi pi-refresh" text @click="onPageChange(meta.current_page)" />
            </template>
            <template #paginatorend>
                <Button type="button" icon="pi pi-download" @click="async () => {
                    await downloadFile(selectedCity.code)
                }" text />
            </template>
            <Column field="id" header="ID" style="width: 25%"></Column>
            <Column field="name" header="Name" style="width: 25%"></Column>
        </DataTable>
        <Pagination :totalPages="meta.total_page" :currentPage="meta.current_page" @pageChange="onPageChange" />
    </div>
</template>

<script setup>
import { useUserState } from '~/state/useUserState';
const userState = useUserState()

const products = ref([]);
const meta = ref({});
const selectedCity = ref({ name: 'Field', code: 'mest' });
const cities = ref([
    { name: 'Field', code: 'mest' },
    { name: 'CDNG', code: 'cdng' },
    { name: 'Bush', code: 'kust' },
    { name: 'Well', code: 'wells' },
    { name: 'NGDU', code: 'ngdu' }
]);

const currentType = ref('wells');

const fetchProducts = async (type, page = 1) => {
    console.log(userState.token.value)
    const response = await fetch(`/api/objects/list?order_direction=asc&obj_type=${selectedCity.value.code}&page=${page}&per_page=1000`, {
        headers: {
            "Authorization": 'Bearer ' + localStorage.getItem('token')
        }
    });
    const data = await response.json();
    products.value = data.data;
    meta.value = data.meta;
};

const onPageChange = (page = 1) => {
    fetchProducts(currentType.value, page);
};

onMounted(() => {
    fetchProducts(currentType.value);
});
</script>
