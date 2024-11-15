import { defineStore } from 'pinia';
import { ref, onMounted } from 'vue';
import { useUserState } from './useUserState';

const userState = useUserState()

interface Orders {
    orderId: string,
    title: string,
    description: string,
    imageURL: string
}
export const useOrderState = defineStore("orderState", () => {
  const orders = ref("");

  onMounted(() => {
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      token.value = storedToken;
    }
  });

  async function login(login: string, password: string): Promise<boolean> {
    try {
      const response: {
         
        data: {token: string}
        statusCode: number
      } = await $fetch('/backend/auth/login/', {
        method: 'POST',
        body: { login, password }
      });

      if (response.statusCode === 200) {
        token.value = response.data.token;
        localStorage.setItem("token", token.value);
        return true;
      } else {
        return false;
      }
    } catch (error) {
      console.error("Login error:", error);
      return false;
    }
  }

  async function registration(login: string, password: string): Promise<boolean> {
    try {
      const response = await $fetch('/backend/auth/registration/', {
        method: 'POST',
        body: { login, password }
      });

      if (response.statusCode === 200) {
        token.value = response.data.token;
        localStorage.setItem("token", token.value);
        return true;
      } else {
        return false;
      }
    } catch (error) {
      console.error("Registration error:", error);
      return false;
    }
  }

  function isAuthenticated(): boolean {
    return !!token.value;
  }

  return {token , login, registration, isAuthenticated };
});
