<template>
    <div class="card flex justify-center">
        <Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Выберите месторождение"
            class="w-full md:w-56" />
    </div>
    <OrganizationChart class="card flex justify-center mt-5" v-model:selectionKeys="selection" collapsible
        selectionMode="single" :value="data">
        <template #main="slotProps">
            <div class="flex flex-col">
                <div class="flex flex-col items-center">
                    <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                </div>
            </div>
        </template>
        <template #workshop="slotProps" collapsible>
            <div class="flex flex-col">
                <div class="flex flex-col items-center">
                    <span class="font-bold mb-2">{{ slotProps.node.data.name }}</span>
                </div>
            </div>
        </template>
        <template #bush="slotProps" collapsible>
            <span>{{ slotProps.node.data.name }}</span>
        </template>
        <template #well="slotProps" collapsible>
            <span>{{ slotProps.node.data.name }}</span>
        </template>
    </OrganizationChart>
</template>

<script setup>
import { ref } from "vue";

const selectedCity = ref();
const cities = ref([
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
]);
const data = ref({
    key: '0',
    type: 'main',
    data: {
        name: 'Месторождение',
    },
    children: [
        {
            key: '0_0',
            type: 'workshop',
            data: {
                name: 'цех 1',
            },
            children: [
                {
                    key: '0_0_1',
                    type: 'bush',
                    data: {
                        name: 'куст 1',
                    }, children: [
                        {
                            key: '0_0_0_1',
                            type: 'well',
                            data: {
                            
                                name: 'скважина 1',
                            }
                        },
                        {
                            key: '0_0_0_2',
                            type: 'well',
                            data: {
                                name: 'скважина 2',
                            }
                        }
                    ]
                },
                {
                    key: '0_0_2',
                    type: 'bush',
                    data: {
                        name: 'куст 2',
                    }, children: [
                        {
                            key: '0_0_2_0',
                            type: 'well',
                            data: {
                                name: 'скважина 3',
                            }
                        },
                        {
                            key: '0_0_2_1',
                            type: 'well',
                            data: {
                                name: 'скважина 4',
                            }
                        }
                    ]
                }
            ]
        },
        {
            key: '0_1',
            type: 'bush',
            data: {
                name: 'Anna Fali',
                type: 'person',
            },
            children: [
                {
                    key: '0_1_1',
                    type: 'well',
                    data: {
                        name: 'Anna Fali',
                        type: 'person',
                    }
                }
            ]
        },
    ]
});
const selection = ref({});
</script>
