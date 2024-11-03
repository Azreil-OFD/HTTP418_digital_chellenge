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
    <div>
      {{ message }}
    </div>
  </div>
</template>
