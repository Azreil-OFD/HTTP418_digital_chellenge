import Aura from "@primevue/themes/aura";
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ["@primevue/nuxt-module"],
  primevue: {
    options: {
      theme: {
        preset: Aura,
        darkModeSelector: true,
      },
    },
  },
  devtools: { enabled: true },
  srcDir: "src/",
  routeRules: {
    "/api/**": {
      proxy:
        process.env.NODE_ENV === "development"
          ? "http://127.0.0.1:8000/api/**"
          : "/api/**",
    },
    "/docs": {
      proxy: "http://127.0.0.1:8000/docs",
    },
    "/openapi.json": {
      proxy: "http://127.0.0.1:8000/openapi.json",
    },
  },
  nitro: {
    vercel: {
      config: {
        routes: [
          {
            src: "/api/(.*)",
            dest: "api/index.py",
          },
        ],
      },
    },
  },
});
