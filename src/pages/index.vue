<script setup lang="ts">

</script>

<template>
    <div class="flex main">
        <MapboxMap map-id="map" style="position: absolute; height: 110%; width: 75%; left: 0; top: 0; z-index: -10;  "
            :options="{
                style: 'mapbox://styles/mapbox/light-v11', // style URL
                center: [-68.137343, 45.137451], // starting position
                zoom: 5 // starting zoom
            }" />

    </div>
</template>

<style></style>