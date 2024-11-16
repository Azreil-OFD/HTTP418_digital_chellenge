import { defineStore } from 'pinia';
import { useUserState } from './useUserState'; 
import axios from 'axios';

const userState = useUserState()

interface orderCreate {
  title: string;
  description: string;
  image: File | null;
}

interface orderCreateResponse {
  order_id: string; 
}

export const useOrderState = defineStore("orderState", () => {
  
  // Метод для создания ордера
  async function createOrder(order: orderCreate): Promise<orderCreateResponse> {
    // Получаем токен из состояния пользователя
    const token = userState.token;
    
    // Проверяем наличие токена
    if (!token) {
      throw new Error('Токен авторизации отсутствует');
    }

    // Формируем FormData для отправки на сервер
    const formData = new FormData();
    formData.append('title', order.title);
    formData.append('description', order.description);
    if (order.image) {
      formData.append('image', order.image);
    }

    try {
      // Отправляем POST-запрос на создание ордера
      const response = await axios.post('/api/create_order/', formData, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'multipart/form-data'
        }
      });

      // Возвращаем данные ответа, содержащие order_id
      return response.data;
    } catch (error) {
      console.error('Ошибка при создании ордера:', error);
      throw error; // Прокидываем ошибку для обработки в компоненте
    }
  }

  return { createOrder };
});
