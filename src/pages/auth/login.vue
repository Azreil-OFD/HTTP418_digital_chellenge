<template>
    <div class="flex items-center justify-center min-h-screen">
    <div class="card">
        <Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
            <div class="flex flex-col gap-1">
                <SelectButton name="selection" :options="['Вход', 'Регистрация']" />
                <Message v-if="$form.selection?.invalid" severity="error">{{ $form.selection.error?.message }}</Message>
            </div>
            <Button type="submit" severity="secondary" label="Submit"></Button>
        </Form>
    </div>
</div>

</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { zodResolver } from '@primevue/forms/resolvers/zod';
import { useToast } from "primevue/usetoast";
import { z } from 'zod';

const toast = useToast();
const initialValues = ref({
    selection: 'Вход'
});
const resolver = ref(zodResolver(
    z.object({
        selection: z.preprocess((val) => (val === null ? '' : val), z.string().min(1, { message: 'Selection is required' }))
    })
));

const onFormSubmit = ({ valid }: {valid: boolean}) => {
    if (valid) {
        toast.add({ severity: 'success', summary: 'Form is submitted.', life: 3000 });
    }
};

</script>

<style></style>