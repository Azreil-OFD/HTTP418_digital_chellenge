<template>
  <Menubar :model="items" class="m-5">
    <template #start>
      <NuxtLink to="/auth/login">HTTP418</NuxtLink>
    </template>

    <template #end>
      <div class="flex items-center gap-2" v-if="!token">
        <Button type="submit" severity="secondary" label="Вход" @click="() => { navigateTo('/auth/login') }"></Button>
      </div>
    </template>
  </Menubar>

  <div class="ml-5 mr-5">
    <slot />
  </div>
</template>

<script lang="ts" setup>
import 'primeicons/primeicons.css';
import '../../assets/css/input.css';
import { useUserState } from '~/state/useUserState';
const userState = useUserState()
const { token } = storeToRefs(userState)

const items = ref([]);
</script>

<style></style>