<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-semibold mb-4">Create order</h1>
    <form @submit.prevent="createOrder" class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium">Title</label>
        <input v-model="title" id="title" type="text" required
          class="mt-1 p-2 border border-gray-300 rounded-md w-full" />
      </div>

      <div>
        <label for="description" class="block text-sm font-medium">Description</label>
        <textarea v-model="description" id="description" required
          class="mt-1 p-2 border border-gray-300 rounded-md w-full"></textarea>
      </div>

      <div class="flex justify-center mt-8">
        <div class="rounded-lg shadow-xl bg-gray-50 w-full">
          <div class="m-4">
            <label class="inline-block mb-2 text-gray-500">Upload
              Image (jpg, png, svg, jpeg)</label>
            <div class="flex items-center justify-center w-full">
              <label class="flex flex-col w-full h-32 border-4 border-dashed hover:bg-gray-100 hover:border-gray-300">
                <img v-if="imagePreview" :src="imagePreview" alt="Selected Image"
                  class=" object-contain w-full h-full  text-gray-400 group-hover:text-gray-600" />

                <div v-if="!imagePreview" class="flex flex-col items-center justify-center pt-7">

                  <svg xmlns="http://www.w3.org/2000/svg" class="w-12 h-12 text-gray-400 group-hover:text-gray-600"
                    viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd"
                      d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z"
                      clip-rule="evenodd" />
                  </svg>
                  <p class="pt-1 text-sm tracking-wider text-gray-400 group-hover:text-gray-600">
                    Select a photo</p>
                  <!-- Show the selected image here -->
                </div>
                <input ref="image" id="image" type="file" accept="image/jpeg,image/png,image/svg+xml"
                  @change="handleImageChange" required class="opacity-0" />
              </label>
            </div>
          </div>
        </div>
      </div>

      <Button  @click="createOrder" class="w-full"> 
        Create
      </Button>
    </form>
  </div>
</template>

<script setup>
import { useOrderState } from '~/state/useOrderState';
const title = ref('')
const description = ref('')
const image = ref(null)
const imagePreview = ref(null) // New ref for the image preview
const imageUpload = ref(null) // New ref for the image preview
const router = useRouter()
let orderState = useOrderState()

// Handle image change and generate a preview
const handleImageChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    imagePreview.value = URL.createObjectURL(file) // Create a URL for the selected file
    image.value = file // Store the file for form submission
    imageUpload.value = file
  }
}

const createOrder = async () => {
  if(!imagePreview.value) {
    console.error('Ошибка создания ордера: Изображение не выбрано ')
  }
  try {
    const response = await orderState.createOrder({
    title: title.value,
    description: description.value,
    image: imageUpload.value
  })

    // router.push(`/orders/${response.order_id}`)
    router.push(`/orders/`)

  } catch (error) {
    console.error('Ошибка создания ордера:', error)
  }
}
</script>

<style scoped>
/* Tailwind classes are already applied, but you can add custom styles if needed */
</style>
