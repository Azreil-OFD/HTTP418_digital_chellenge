<template>
  <Menubar :model="items" class="m-5">
    <template #start>
      <NuxtLink to="/">HTTP418</NuxtLink>
    </template>

    <template #end>
      <div class="flex items-center gap-2" v-if="!token" >
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
import { useUserState } from '~/state/useUserState';
const userState = useUserState()
const {token} = storeToRefs(userState)

const items = ref([
  {
    label: 'Home',
    icon: 'pi pi-home',
    command: () => {navigateTo('/')}
  },
  {
    label: 'Orders',
    icon: 'pi pi-server',
    items: [
            {
                label: 'Order list',
                icon: 'pi pi-bars',
                command: () => {
                  navigateTo('/orders')
                }
            },
            {
                label: 'Create Order',
                icon: 'pi pi-plus',
                command: () => {
                  navigateTo('/orders/create')
                }
            }
        ]

  },
]);

</script>

<style>
</style>