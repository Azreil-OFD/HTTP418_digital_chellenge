<script setup lang="tsx">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const Markups = ref([]);

// Загружаем данные из API
onMounted(async () => {
    try {
        if (!localStorage.getItem('maps')) {
            const response = await axios.get('/api/objects/map');
            Markups.value = response.data.map((item) => ({
                markerId: item.id,
                name: item.name,
                lnglat: [item.coordinates.lon, item.coordinates.lat],
                isVisible: true, // Изначально попап скрыт
            }));
            localStorage.setItem('maps', JSON.stringify(Markups.value))
            location.reload()
        } else {
            Markups.value = JSON.parse(localStorage.getItem('maps'))
        }
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
            <MapboxDefaultMarker v-for="item in Markups" :key="item.markerId" :popup-id="item.markerId"
                :lnglat="item.lnglat" @click="togglePopup(item.markerId)">
                <MapboxDefaultPopup v-if="item.isVisible" :popup-id="`popup-${item.markerId}`" :lnglat="item.lnglat"
                    :options="{
                        closeOnClick: true,
                    }">
                    <h1 class="test" @click="goToPage(item.markerId)">
                        {{ item.name }}
                    </h1>
                </MapboxDefaultPopup>
            </MapboxDefaultMarker>
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
