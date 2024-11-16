
<template>
    <div class="card">
        <DataTable :value="orders" tableStyle="min-width: 50rem">
            <template #header>
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <span class="text-xl font-bold">Orders</span>
                    <Button severity="secondary" icon="pi pi-plus" @click="() => {navigateTo('/orders/create')}" rounded raised />
                </div>
            </template>
            <Column field="title" header="Title"></Column>
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
const orders = ref([
    {
        title: "Wooden Chair",
        image: "https://pic.rutubelist.ru/video/0c/f8/0cf8099c7c60b7b44fa12f80b59dfbe7.jpg",
        description: "A comfortable wooden chair suitable for home and office use."
    },
    {
        title: "Office Desk",
        image: "https://i.pinimg.com/originals/c8/6a/61/c86a61f9892ba2288316fc46846e1d12.jpg",
        description: "A modern office desk with a clean design, perfect for any workspace."
    },
    {
        title: "Floor Lamp",
        image: "https://dinastia96.ru/image/catalog/import_files/a3/a353613d-eefd-11e8-b0e2-485b392887e1_01eaabd7-401e-11eb-aca1-485b392887e1.jpeg",
        description: "A stylish floor lamp that brightens up any room."
    },
    {
        title: "Bookshelf",
        image: "https://avatars.mds.yandex.net/get-eda/2806911/82ebbfa86070e782fd46e3da33d2cc5e/orig",
        description: "A spacious bookshelf with multiple shelves for storing books and decor."
    },
    {
        title: "Dining Table",
        image: "https://attuale.ru/wp-content/uploads/2019/01/Bake-it-Dont-Buy-it1.jpg",
        description: "A large dining table for family meals or gatherings."
    }
]);
</script>
