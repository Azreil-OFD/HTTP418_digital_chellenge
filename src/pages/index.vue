<script setup lang="ts">


const route = useRoute()
const message = ref("")
</script>

<template>
  <div>
    

<div class="grid mb-8 border border-gray-200 rounded-lg shadow-sm dark:border-gray-700 md:mb-12 md:grid-cols-2 bg-white dark:bg-gray-800">
    <figure class="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 rounded-t-lg md:rounded-t-none md:rounded-ss-lg md:border-e dark:bg-gray-800 dark:border-gray-700">
        <blockquote class="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Самый крутой божественный программист</h3>
            <p class="my-4">Создал эту страницу.</p>
        </blockquote>
        <figcaption class="flex items-center justify-center ">
            <img class="rounded-full w-9 h-9" src="https://i.postimg.cc/6qtsb6Fm/image.png" alt="profile picture">
            <div class="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3">
                <div>Эльнур Гулиев</div>
                <div class="text-sm text-gray-500 dark:text-gray-400 ">Разработчик всего и вся</div>
            </div>
        </figcaption>    
    </figure>
    <figure class="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 md:rounded-se-lg dark:bg-gray-800 dark:border-gray-700">
        <blockquote class="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Везучая паскуда</h3>
            <p class="my-4">Лучший в мире разраб в сфере везения, и по совместительству будущий тимлид"</p>
        </blockquote>
        <figcaption class="flex items-center justify-center ">
            <img class="rounded-full w-9 h-9" src="https://steamuserimages-a.akamaihd.net/ugc/1824528943476571939/5E9D176331811B42B1AE8498A84AB04D4499D623/?imw=512&amp;&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=false" alt="profile picture">
            <div class="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3">
                <div>Ярик</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">Лидер нашей команды</div>
            </div>
        </figcaption>    
    </figure>
    <figure class="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 md:rounded-es-lg md:border-b-0 md:border-e dark:bg-gray-800 dark:border-gray-700">
        <blockquote class="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Стажор</h3>
            <p class="my-4">Впихну го туда куда его не впихать</p>
        </blockquote>
        <figcaption class="flex items-center justify-center ">
            <img class="rounded-full w-9 h-9" src="https://sun9-28.userapi.com/impf/gKoYNVQVkQiop65KA2C3NMAHwE0AIZZUvbb_nA/hXwQdxkxQHg.jpg?size=422x604&quality=96&sign=e8d2c6ccab43e23310ec28b5cadc32a3&type=album" alt="profile picture">
            <div class="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3">
                <div>Чингис Хандаев Зорикдоевич</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">5 колесо тележки</div>
            </div>
        </figcaption>    
    </figure>
    <figure class="flex flex-col items-center justify-center p-8 text-center bg-white border-gray-200 rounded-b-lg md:rounded-se-lg dark:bg-gray-800 dark:border-gray-700">
        <blockquote class="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Исмаил Бисмаил</h3>
            <p class="my-4">Фронтендер который ваще не в нашей команде</p>
        </blockquote>
        <figcaption class="flex items-center justify-center ">
            <img class="rounded-full w-9 h-9" src="https://cdnn21.img.ria.ru/images/07e4/07/1f/1575214694_0:0:2415:1359_1920x1080_80_0_0_b17b87417aa358f13185342fe6c99983.jpg" alt="profile picture">
            <div class="space-y-0.5 font-medium dark:text-white text-left rtl:text-right ms-3">
                <div>Исмаил Бисмаил</div>
                <div class="text-sm text-gray-500 dark:text-gray-400">Успешный инфоцыган</div>
            </div>
        </figcaption>    
    </figure>
</div>

  </div>
</template>
