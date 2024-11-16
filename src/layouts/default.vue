<template>
  <div style="position: absolute; left: 0; top: 0; height: 10%; width: 100%; z-index: -5;" class="backdrop-blur-sm"></div>
  <Menubar :model="items" class="m-5">
    <template #start>
      <NuxtLink to="/">HTTP418</NuxtLink>
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
onMounted(() => {
  if(!token.value) {
    navigateTo('/auth/login')
  }
})

const items = ref([
  {
    label: 'Home',
    icon: 'pi pi-home',
    command: () => { navigateTo('/') }
  },
  {
    label: 'Objects',
    icon: 'pi pi-server',
    items: [
      {
        label: 'Objects list',
        icon: 'pi pi-bars',
        command: () => {
          navigateTo('/objects')
        }
      },
      {
        label: 'Top Objects',
        icon: 'pi pi-chart-bar',
        command: () => {
          navigateTo('/objects')
        }
      }
    ]
  }
]);
</script>

<style></style>