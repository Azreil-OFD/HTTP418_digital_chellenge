<template>
    <div class="flex items-center justify-center">
        <div class="card p-6 border rounded-lg border-gray-200">
            <div class="flex flex-col gap-1 w-full items-center justify-center">
                <SelectButton v-model="selection" name="selection" :options="['Вход', 'Регистрация'] " />
            </div>
            <Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit"
                class="flex flex-col gap-4 items-center justify-center">
                <div class="flex flex-col gap-1 w-full">
                    <label for="email">Email</label>
                    <InputText id="email" name="email" type="email" placeholder="Введите email" />
                    <Message class="mt-2" v-if="$form.email?.invalid" severity="error">{{ $form.email.error?.message }}</Message>
                </div>
                <div class="flex flex-col gap-1 w-full">
                    <label for="password">Password</label>
                    <Password id="password" name="password" toggleMask placeholder="Введите пароль" />
                    <Message class="mt-2" v-if="$form.password?.invalid" severity="error">{{ $form.password.error?.message }}
                    </Message>
                </div>
                <Button class="w-full" type="submit" severity="secondary" :label="selection"></Button>
            </Form>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { zodResolver } from '@primevue/forms/resolvers/zod';
import { useToast } from "primevue/usetoast";
import { z } from 'zod';
import { compileScript } from 'vue/compiler-sfc';

const toast = useToast();
const initialValues = ref({
    email: '',
    password: ''
});
const selection = ref('Вход')
const resolver = ref(zodResolver(
    z.object({
        email: z.string().email({ message: 'Невалидная почта' }).nonempty({ message: 'Введите почту' }),
        password: z.string().min(6, { message: 'Минимум 6 символов' }).nonempty({ message: 'Введите пароль' })
    })
));

const onFormSubmit = ({ valid }: { valid: boolean }) => {
    console.log(resolver.value)
    if (valid) {
        toast.add({ severity: 'success', summary: 'Form is submitted.', life: 3000 });
    }
};
</script>

<style></style>
