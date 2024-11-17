<script setup lang="tsx">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useUserState } from '~/state/useUserState';
const userState = useUserState()

const Markups = ref([]);

// Загружаем данные из API
onMounted(async () => {
    try {
        const response = await axios.get('https://backends.ru.tuna.am/api/objects/map', {
            headers: {
                Authorization: 'Bearer ' + localStorage.getItem('token')
            }
        });
        Markups.value = response.data.map((item) => ({
            markerId: item.id,
            name: item.name,
            lnglat: [item.coordinates.lon, item.coordinates.lat],
            isVisible: true,
        }));
    } catch (error) {
        console.error('Ошибка загрузки данных:', error);
    }
});

// Метод для управления видимостью попапа
const togglePopup = (markerId) => {
    Markups.value = Markups.value.map((item) =>
        item.markerId === markerId ? { ...item, isVisible: !item.isVisible } : item
    );
};
</script>

<template>
    <div class="flex main">

        <MapboxMap map-id="map" style="position: absolute; height: 110%; width: 100%; left: 0; top: 0; z-index: -10;"
            :options="{
                style: 'mapbox://styles/mapbox/streets-v12',
                center: [64.94895931101014, 64.7513899266245],
                zoom: 5
            }">
            <MapboxDefaultPopup popup-id="<POPUP_ID>1" :lnglat="[64.94895931101014, 64.7513899266245]" :options="{
                closeOnClick: false,
                closeButton: false
            }">
                <h1 class="test">
                    <a href="/objects/select/1111">1111</a>
                </h1>
            </MapboxDefaultPopup>
            <MapboxDefaultPopup popup-id="<POPUP_ID>2" :lnglat="[67, 64.7513899266245]" :options="{
                closeOnClick: false,
                closeButton: false
            }">
                <h1 class="test">
                    <a href="/objects/select/111">111</a>
                </h1>
            </MapboxDefaultPopup>
            <MapboxDefaultPopup popup-id="<POPUP_ID>3" :lnglat="[64.94895931101014, 67.7513899266245]" :options="{
                closeOnClick: false,
                closeButton: false
            }">
                <h1 class="test">
                    <a href="/objects/select/222">222</a>
                </h1>
            </MapboxDefaultPopup>
        </MapboxMap>
    </div>
</template>

<style>
.test {
    cursor: pointer;
    color: blue;
    text-decoration: underline;
}
</style>
