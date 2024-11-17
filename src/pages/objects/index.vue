<template>
    <div class="card flex justify-center">
        <Select v-model="selectedArea" :options="area" optionLabel="name" placeholder="Выберите месторождение"
            class="w-full md:w-56" />
    </div>
    <div style="overflow-y: scroll;">
        <OrganizationChart v-if="selectedArea" class="card flex justify-center mt-5 w-full" style="width: fit-content;"
            v-model:selectionKeys="selection" collapsible selectionMode="single" :value="data">
            <template #main="slotProps">
                <div class="flex flex-col">
                    <div class="flex flex-col items-center">
                        <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                        <span>{{ slotProps.node.data.counts }} well</span>
                    </div>
                </div>
            </template>
            <template #workshop="slotProps" collapsible>
                <div class="flex flex-col">
                    <div class="flex flex-col items-center">
                        <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                        <span>{{ slotProps.node.data.counts }} well</span>
                    </div>
                </div>
            </template>
            <template #bush="slotProps" collapsible>
                <span>{{ slotProps.node.data.name }}</span> <br>
                <span>{{ slotProps.node.data.counts }} well</span>
            </template>
            <template #well="slotProps" collapsible>
                <span>{{ slotProps.node.data.name }}</span>
            </template>
        </OrganizationChart>
    </div>
</template>
<script setup>
import { ref, watch, onMounted } from "vue";
import axios from "axios"; // Убедитесь, что axios установлен


const selectedArea = ref();
const area = ref([
    { name: 'КедрНефть', code: '1' },
    { name: 'СоснаНефть', code: '2' },
    { name: 'ЛиственницаНефть', code: '3' },
    { name: 'ТуяНефть', code: '4' }
]);

const data = ref([]);
const selection = ref({});

// Функция для получения данных из API
const fetchData = async (objId) => {
    try {
        const response = await axios.get(`/api/objects/tree/?obj_id=${objId}`, {
            headers: {
                "Authorization": 'Bearer ' + localStorage.getItem('token')
            }
        });
        console.log(response.data)
        data.value = response.data;
    } catch (error) {
        console.error("Ошибка при получении данных:", error);
    }
};

// Слушаем изменение выбранной области
watch(selectedArea, (newValue) => {
    if (newValue) {
        fetchData(newValue.code); // Получаем данные для выбранной области
    }
});

// Обработчик выбора
watch(selection, () => {
    if (Object.keys(selection.value).length !== 0 && Object.keys(selection.value)[0] !== 'undefined') {
        navigateTo('/objects/select/' + Object.keys(selection.value)[0]);
    }
});

// Вызываем fetchData при монтировании, если выбрана область
onMounted(() => {
    if (selectedArea.value) {
        fetchData(selectedArea.value.code);
    }
});
</script>
