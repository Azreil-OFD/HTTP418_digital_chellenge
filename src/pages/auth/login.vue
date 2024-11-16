<template>
    <div class="flex items-center justify-center mt-20">
        <div class="card p-6 border rounded-lg border-gray-200">
            <div class="flex flex-col gap-1 w-full items-center justify-center">
                <SelectButton v-model="selection" name="selection"  :options="['Вход']" />
            </div>
            <div v-if="error" class="p-4 m-3 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400"
                role="alert">
                {{error}}
            </div>
            <Form  @submit="onFormSubmit" class="flex flex-col gap-4 items-center justify-center">
                <div class="flex flex-col gap-1 w-full">
                    <label for="email">Email</label>
                    <InputText v-model="email" id="email" name="email" type="email" placeholder="Введите email" />
                </div>
                <div class="flex flex-col gap-1 w-full">
                    <label for="password">Password</label>
                    <Password v-model="password" id="password" name="password" toggleMask
                        placeholder="Введите пароль" />
                </div>
                <Button class="w-full" type="submit" severity="secondary" :label="selection"></Button>
            </Form>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useUserState } from '~/state/useUserState';

definePageMeta({
  layout: false
})
const userState = useUserState()

const email = ref('');
const error = ref('');
const password = ref('');
const selection = ref('Вход');

const onFormSubmit = async ({ valid }: { valid: boolean }) => {
    if (valid) {
        if(email.value.length < 3) {
            error.value = "Минимум 3 символа в email"
            return
        }
        if(password.value.length < 6) {
            error.value = "Минимум 6 символа в password"
            return
        }
        error.value = ""
        let result: boolean = false
        if (selection.value === 'Вход') {
            result = await userState.login(email.value, password.value)
        } else {
            result = await userState.registration(email.value, password.value)
        }
        console.log(result)
        if (result) {
            navigateTo('/')
        } else {
            if(selection.value === "Вход") {
                error.value = "Не правильный логин и пароль"
            } else if (selection.value === "Регистрация") {
                error.value = "Пользователь с данным email уже существует"
            }
         }
    }
};
</script>

<style></style>
