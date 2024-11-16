<script setup lang="tsx">

const Markups = [
    {
        markerId: "1asdasdas",
        lnglat: [-68.137343, 45.137451],
    }
]
</script>

<template>
    <div class="flex main">
        <MapboxMap map-id="map" style="position: absolute; height: 110%; width: 75%; left: 0; top: 0; z-index: -10;  "
            :options="{
                style: 'mapbox://styles/mapbox/light-v11',
                center: [-68.137343, 45.137451],
                zoom: 5
            }">
            <MapboxDefaultMarker v-for="item in Markups" :popup-id="item.markerId" :lnglat="item.lnglat" :options="{
            }">
                <MapboxDefaultPopup popup-id="popup1" :lnglat="item.lnglat" :options="{
                    closeOnClick: false
                }">
                    <h1 class="test">
                        Hello World!
                    </h1>
                </MapboxDefaultPopup>
            </MapboxDefaultMarker>
        </MapboxMap>

    </div>

</template>

<style></style>