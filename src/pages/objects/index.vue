<template>
    <div class="card flex justify-center">
        <Select v-model="selectedArea" :options="area" optionLabel="name" placeholder="Выберите месторождение"
            class="w-full md:w-56" />
    </div>
    <ZoomableDiv :ref="zoomable">
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
    </ZoomableDiv>
</template>

<script setup>
import { ref } from "vue";
const zoomable = ref()
const selectedArea = ref();
const area = ref([
    { name: 'КедрНефть', code: 'KN' },
    { name: 'СоснаНефть', code: 'SN' },
    { name: 'ЛиственницаНефть', code: 'LN' },
    { name: 'ТуяНефть', code: 'TN' }
]);
watch(selectedArea, () => {
    zoomable.centerObject()
})
const data = ref({
  "key": 1,
  "type": "main",
  "data": {
    "name": "КедрНефть"
  },
  "children": [
    {
      "key": 11,
      "type": "cdng",
      "data": {
        "name": "ц.11"
      },
      "children": [
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 111,
          "type": "kust",
          "data": {
            "name": "к.111"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        },
        {
          "key": 112,
          "type": "kust",
          "data": {
            "name": "к.112"
          }
        }
      ]
    },
    {
      "key": 12,
      "type": "cdng",
      "data": {
        "name": "ц.12"
      },
      "children": [
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 121,
          "type": "kust",
          "data": {
            "name": "к.121"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 122,
          "type": "kust",
          "data": {
            "name": "к.122"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        },
        {
          "key": 123,
          "type": "kust",
          "data": {
            "name": "к.123"
          }
        }
      ]
    },
    {
      "key": 13,
      "type": "cdng",
      "data": {
        "name": "ц.13"
      },
      "children": [
        {
          "key": 131,
          "type": "kust",
          "data": {
            "name": "к.131"
          }
        },
        {
          "key": 131,
          "type": "kust",
          "data": {
            "name": "к.131"
          }
        },
        {
          "key": 131,
          "type": "kust",
          "data": {
            "name": "к.131"
          }
        },
        {
          "key": 131,
          "type": "kust",
          "data": {
            "name": "к.131"
          }
        },
        {
          "key": 131,
          "type": "kust",
          "data": {
            "name": "к.131"
          }
        },
        {
          "key": 131,
          "type": "kust",
          "data": {
            "name": "к.131"
          }
        },
        {
          "key": 132,
          "type": "kust",
          "data": {
            "name": "к.132"
          }
        },
        {
          "key": 132,
          "type": "kust",
          "data": {
            "name": "к.132"
          }
        },
        {
          "key": 132,
          "type": "kust",
          "data": {
            "name": "к.132"
          }
        },
        {
          "key": 132,
          "type": "kust",
          "data": {
            "name": "к.132"
          }
        },
        {
          "key": 132,
          "type": "kust",
          "data": {
            "name": "к.132"
          }
        },
        {
          "key": 132,
          "type": "kust",
          "data": {
            "name": "к.132"
          }
        },
        {
          "key": 133,
          "type": "kust",
          "data": {
            "name": "к.133"
          }
        },
        {
          "key": 133,
          "type": "kust",
          "data": {
            "name": "к.133"
          }
        },
        {
          "key": 133,
          "type": "kust",
          "data": {
            "name": "к.133"
          }
        },
        {
          "key": 133,
          "type": "kust",
          "data": {
            "name": "к.133"
          }
        },
        {
          "key": 133,
          "type": "kust",
          "data": {
            "name": "к.133"
          }
        },
        {
          "key": 133,
          "type": "kust",
          "data": {
            "name": "к.133"
          }
        },
        {
          "key": 134,
          "type": "kust",
          "data": {
            "name": "к.134"
          }
        },
        {
          "key": 134,
          "type": "kust",
          "data": {
            "name": "к.134"
          }
        },
        {
          "key": 134,
          "type": "kust",
          "data": {
            "name": "к.134"
          }
        },
        {
          "key": 134,
          "type": "kust",
          "data": {
            "name": "к.134"
          }
        },
        {
          "key": 134,
          "type": "kust",
          "data": {
            "name": "к.134"
          }
        },
        {
          "key": 134,
          "type": "kust",
          "data": {
            "name": "к.134"
          }
        }
      ]
    },
    {
      "key": 14,
      "type": "cdng",
      "data": {
        "name": "ц.14"
      },
      "children": [
        {
          "key": 141,
          "type": "kust",
          "data": {
            "name": "к.141"
          }
        },
        {
          "key": 141,
          "type": "kust",
          "data": {
            "name": "к.141"
          }
        },
        {
          "key": 141,
          "type": "kust",
          "data": {
            "name": "к.141"
          }
        },
        {
          "key": 141,
          "type": "kust",
          "data": {
            "name": "к.141"
          }
        },
        {
          "key": 141,
          "type": "kust",
          "data": {
            "name": "к.141"
          }
        },
        {
          "key": 142,
          "type": "kust",
          "data": {
            "name": "к.142"
          }
        },
        {
          "key": 142,
          "type": "kust",
          "data": {
            "name": "к.142"
          }
        },
        {
          "key": 142,
          "type": "kust",
          "data": {
            "name": "к.142"
          }
        },
        {
          "key": 142,
          "type": "kust",
          "data": {
            "name": "к.142"
          }
        },
        {
          "key": 142,
          "type": "kust",
          "data": {
            "name": "к.142"
          }
        },
        {
          "key": 143,
          "type": "kust",
          "data": {
            "name": "к.143"
          }
        },
        {
          "key": 143,
          "type": "kust",
          "data": {
            "name": "к.143"
          }
        },
        {
          "key": 143,
          "type": "kust",
          "data": {
            "name": "к.143"
          }
        },
        {
          "key": 143,
          "type": "kust",
          "data": {
            "name": "к.143"
          }
        },
        {
          "key": 143,
          "type": "kust",
          "data": {
            "name": "к.143"
          }
        },
        {
          "key": 144,
          "type": "kust",
          "data": {
            "name": "к.144"
          }
        },
        {
          "key": 144,
          "type": "kust",
          "data": {
            "name": "к.144"
          }
        },
        {
          "key": 144,
          "type": "kust",
          "data": {
            "name": "к.144"
          }
        },
        {
          "key": 144,
          "type": "kust",
          "data": {
            "name": "к.144"
          }
        },
        {
          "key": 144,
          "type": "kust",
          "data": {
            "name": "к.144"
          }
        },
        {
          "key": 145,
          "type": "kust",
          "data": {
            "name": "к.145"
          }
        },
        {
          "key": 145,
          "type": "kust",
          "data": {
            "name": "к.145"
          }
        },
        {
          "key": 145,
          "type": "kust",
          "data": {
            "name": "к.145"
          }
        },
        {
          "key": 145,
          "type": "kust",
          "data": {
            "name": "к.145"
          }
        },
        {
          "key": 145,
          "type": "kust",
          "data": {
            "name": "к.145"
          }
        }
      ]
    },
    {
      "key": 15,
      "type": "cdng",
      "data": {
        "name": "ц.15"
      },
      "children": [
        {
          "key": 151,
          "type": "kust",
          "data": {
            "name": "к.151"
          }
        },
        {
          "key": 151,
          "type": "kust",
          "data": {
            "name": "к.151"
          }
        },
        {
          "key": 151,
          "type": "kust",
          "data": {
            "name": "к.151"
          }
        },
        {
          "key": 151,
          "type": "kust",
          "data": {
            "name": "к.151"
          }
        },
        {
          "key": 152,
          "type": "kust",
          "data": {
            "name": "к.152"
          }
        },
        {
          "key": 152,
          "type": "kust",
          "data": {
            "name": "к.152"
          }
        },
        {
          "key": 152,
          "type": "kust",
          "data": {
            "name": "к.152"
          }
        },
        {
          "key": 152,
          "type": "kust",
          "data": {
            "name": "к.152"
          }
        },
        {
          "key": 153,
          "type": "kust",
          "data": {
            "name": "к.153"
          }
        },
        {
          "key": 153,
          "type": "kust",
          "data": {
            "name": "к.153"
          }
        },
        {
          "key": 153,
          "type": "kust",
          "data": {
            "name": "к.153"
          }
        },
        {
          "key": 153,
          "type": "kust",
          "data": {
            "name": "к.153"
          }
        },
        {
          "key": 154,
          "type": "kust",
          "data": {
            "name": "к.154"
          }
        },
        {
          "key": 154,
          "type": "kust",
          "data": {
            "name": "к.154"
          }
        },
        {
          "key": 154,
          "type": "kust",
          "data": {
            "name": "к.154"
          }
        },
        {
          "key": 154,
          "type": "kust",
          "data": {
            "name": "к.154"
          }
        },
        {
          "key": 155,
          "type": "kust",
          "data": {
            "name": "к.155"
          }
        },
        {
          "key": 155,
          "type": "kust",
          "data": {
            "name": "к.155"
          }
        },
        {
          "key": 155,
          "type": "kust",
          "data": {
            "name": "к.155"
          }
        },
        {
          "key": 155,
          "type": "kust",
          "data": {
            "name": "к.155"
          }
        },
        {
          "key": 156,
          "type": "kust",
          "data": {
            "name": "к.156"
          }
        },
        {
          "key": 156,
          "type": "kust",
          "data": {
            "name": "к.156"
          }
        },
        {
          "key": 156,
          "type": "kust",
          "data": {
            "name": "к.156"
          }
        },
        {
          "key": 156,
          "type": "kust",
          "data": {
            "name": "к.156"
          }
        }
      ]
    },
    {
      "key": 16,
      "type": "cdng",
      "data": {
        "name": "ц.16"
      },
      "children": [
        {
          "key": 161,
          "type": "kust",
          "data": {
            "name": "к.161"
          }
        },
        {
          "key": 161,
          "type": "kust",
          "data": {
            "name": "к.161"
          }
        },
        {
          "key": 161,
          "type": "kust",
          "data": {
            "name": "к.161"
          }
        },
        {
          "key": 162,
          "type": "kust",
          "data": {
            "name": "к.162"
          }
        },
        {
          "key": 162,
          "type": "kust",
          "data": {
            "name": "к.162"
          }
        },
        {
          "key": 162,
          "type": "kust",
          "data": {
            "name": "к.162"
          }
        },
        {
          "key": 163,
          "type": "kust",
          "data": {
            "name": "к.163"
          }
        },
        {
          "key": 163,
          "type": "kust",
          "data": {
            "name": "к.163"
          }
        },
        {
          "key": 163,
          "type": "kust",
          "data": {
            "name": "к.163"
          }
        },
        {
          "key": 164,
          "type": "kust",
          "data": {
            "name": "к.164"
          }
        },
        {
          "key": 164,
          "type": "kust",
          "data": {
            "name": "к.164"
          }
        },
        {
          "key": 164,
          "type": "kust",
          "data": {
            "name": "к.164"
          }
        },
        {
          "key": 165,
          "type": "kust",
          "data": {
            "name": "к.165"
          }
        },
        {
          "key": 165,
          "type": "kust",
          "data": {
            "name": "к.165"
          }
        },
        {
          "key": 165,
          "type": "kust",
          "data": {
            "name": "к.165"
          }
        },
        {
          "key": 166,
          "type": "kust",
          "data": {
            "name": "к.166"
          }
        },
        {
          "key": 166,
          "type": "kust",
          "data": {
            "name": "к.166"
          }
        },
        {
          "key": 166,
          "type": "kust",
          "data": {
            "name": "к.166"
          }
        },
        {
          "key": 167,
          "type": "kust",
          "data": {
            "name": "к.167"
          }
        },
        {
          "key": 167,
          "type": "kust",
          "data": {
            "name": "к.167"
          }
        },
        {
          "key": 167,
          "type": "kust",
          "data": {
            "name": "к.167"
          }
        }
      ]
    },
    {
      "key": 17,
      "type": "cdng",
      "data": {
        "name": "ц.17"
      },
      "children": [
        {
          "key": 171,
          "type": "kust",
          "data": {
            "name": "к.171"
          }
        },
        {
          "key": 171,
          "type": "kust",
          "data": {
            "name": "к.171"
          }
        },
        {
          "key": 172,
          "type": "kust",
          "data": {
            "name": "к.172"
          }
        },
        {
          "key": 172,
          "type": "kust",
          "data": {
            "name": "к.172"
          }
        },
        {
          "key": 173,
          "type": "kust",
          "data": {
            "name": "к.173"
          }
        },
        {
          "key": 173,
          "type": "kust",
          "data": {
            "name": "к.173"
          }
        },
        {
          "key": 174,
          "type": "kust",
          "data": {
            "name": "к.174"
          }
        },
        {
          "key": 174,
          "type": "kust",
          "data": {
            "name": "к.174"
          }
        },
        {
          "key": 175,
          "type": "kust",
          "data": {
            "name": "к.175"
          }
        },
        {
          "key": 175,
          "type": "kust",
          "data": {
            "name": "к.175"
          }
        },
        {
          "key": 176,
          "type": "kust",
          "data": {
            "name": "к.176"
          }
        },
        {
          "key": 176,
          "type": "kust",
          "data": {
            "name": "к.176"
          }
        },
        {
          "key": 177,
          "type": "kust",
          "data": {
            "name": "к.177"
          }
        },
        {
          "key": 177,
          "type": "kust",
          "data": {
            "name": "к.177"
          }
        },
        {
          "key": 178,
          "type": "kust",
          "data": {
            "name": "к.178"
          }
        },
        {
          "key": 178,
          "type": "kust",
          "data": {
            "name": "к.178"
          }
        }
      ]
    }
  ]
});
const selection = ref({});
watch(selection, () => {
    if (Object.keys(selection.value).length !== 0)
        if (Object.keys(selection.value)[0] !== 'undefined')
            navigateTo('/objects/select/' + Object.keys(selection.value)[0])
})
</script>
