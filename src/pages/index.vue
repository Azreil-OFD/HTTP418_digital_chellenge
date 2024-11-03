<script setup lang="ts">
const route = useRoute()
const message = ref("")
const getHello = async () => {
  const hello = await (await fetch('/api')).json()
  message.value = hello.message
  return hello
} 
nextTick(async() => {
  await getHello()
})
</script>

<template>
  <div>
    <h1>Nuxt Routing set up successfully!</h1>
    <p>Current route: {{ route.path }}</p>
    <a href="https://nuxt.com/docs/getting-started/routing" target="_blank">Learn more about Nuxt Routing</a>
    {{ message }}
  </div>
</template>
