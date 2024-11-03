<template>
  <Menubar :model="items" class="m-5">
    <template #start>
      <NuxtLink to="/">HTTP418</NuxtLink>
    </template>

    <template #end>
      <div class="flex items-center gap-2">
        <Button type="submit" severity="secondary" label="Вход" @click="() => {navigateTo('/auth/login')}"></Button>
      </div>
    </template>
  </Menubar>

  <div class="ml-5 mr-5">
    <slot />
  </div>
</template>

<script lang="ts" setup>
import 'primeicons/primeicons.css';

const items = ref([
  {
    label: 'Home',
    icon: 'pi pi-home',
    command: () => {navigateTo('/')}
  },
]);

</script>

<style>
</style>