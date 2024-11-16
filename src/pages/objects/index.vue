<template>
    <div class="card flex justify-center">
        <Select v-model="selectedArea" :options="area" optionLabel="name" placeholder="Выберите месторождение"
            class="w-full md:w-56" />
    </div>
    <div style="overflow-y:scroll;">
        <OrganizationChart v-if="selectedArea" class="card flex justify-center mt-5 w-full" style="width: fit-content;"
            v-model:selectionKeys="selection" collapsible selectionMode="single" :value="data">
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
    </div>
    <span v-if="selectedArea">Скролл >></span>
</template>

<script setup>
import { ref } from "vue";

const selectedArea = ref();
const area = ref([
    { name: 'КедрНефть', code: 'KN' },
    { name: 'СоснаНефть', code: 'SN' },
    { name: 'ЛиственницаНефть', code: 'LN' },
    { name: 'ТуяНефть', code: 'TN' }
]);
watch(selectedArea, () => {

})
const data = ref({
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
                        id: 1,
                        name: 'куст 1',

                    }, children: [
                        {
                            id: 2,
                            key: '0_0_0_1',
                            type: 'well',
                            data: {

                                name: 'скважина 1',
                            }
                        },
                        {
                            id: 3,
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
                        id: 3,
                        name: 'куст 2',
                    }, children: [
                        {
                            id: 4,
                            key: '0_0_2_0',
                            type: 'well',
                            data: {
                                name: 'скважина 3',
                            }
                        },
                        {
                            id: 5,
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
                id: 6,
                name: 'Anna Fali',
                type: 'person',
            },
            children: [
                {
                    key: '0_1_1',
                    type: 'well',
                    data: {
                        id: 7,
                        name: 'Anna Fali',
                        type: 'person',
                    }
                }
            ]
        },
    ]
});
const selection = ref({});
watch(selection, () => {
    if (Object.keys(selection.value).length !== 0)
        if (Object.keys(selection.value)[0] !== 'undefined')
            navigateTo('/objects/select/' + Object.keys(selection.value)[0])
})
</script>
