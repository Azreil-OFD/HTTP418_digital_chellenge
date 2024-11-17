import { defineStore } from 'pinia';

export const useUserState = defineStore("userState", () => {
  const token = ref<string>("");

  onMounted(() => {
    // Проверка наличия токена в localStorage
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      token.value = storedToken;
    }
  });

  async function login(login: string, password: string): Promise<boolean> {
    try {
      const response = await $fetch('https://backends.ru.tuna.am/api/authorization', {
        method: 'POST',
        body: { login, password },
      });
      if (response?.token) {
        token.value = response.token;
        localStorage.setItem("token", token.value);
        return true;
      } else {
        console.error("Login failed: No token received");
        return false;
      }
    } catch (error) {
      console.error("Login error:", error);
      return false;
    }
  }

  function isAuthenticated(): boolean {
    return !!token.value; // Возвращает true, если токен существует, иначе false
  }

  return { token, login, isAuthenticated };
});
