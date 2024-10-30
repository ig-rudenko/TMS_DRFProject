<script setup lang="ts">
import {Ref, ref} from "vue";
import {useStore} from "vuex";

import router from "@/router";
import {getAvatar} from "@/services/formats";
import {User} from "@/services/user";
import {getCurrentTheme, setAutoTheme, setDarkTheme, setLightTheme, ThemesValues} from "@/services/themes.ts";
import LogoutButton from "@/components/LogoutButton.vue";

const store = useStore()
const user: User | null = store.state.auth.user

const items = ref([
  {
    label: 'Главная',
    icon: 'pi pi-home',
    command: () => router.push("/"),
  },
]);

if (user) {
  items.value.push({
    label: "Создать",
    icon: "pi pi-plus",
    command: () => router.push("/create"),
  })
} else {
  items.value.push({
    label: "Войти",
    icon: "pi pi-sign-in",
    command: () => router.push("/auth/login"),
  })
}

const currentTheme: Ref<ThemesValues> = ref(getCurrentTheme())

const toggle = () => {
  if (currentTheme.value == "auto") setLightTheme();
  if (currentTheme.value == "light") setDarkTheme();
  if (currentTheme.value == "dark") setAutoTheme();
  currentTheme.value = getCurrentTheme();
}


</script>

<template>
  <div class="card ">
    <Menubar :model="items" class="bg-transparent">

      <template #end>
        <div class="flex items-center gap-2">
          <div>
            <Button icon="pi pi-circle" v-if="currentTheme == 'auto'" @click="toggle"
                    v-tooltip.left="'Включить светлую тему'"
                    class="hover:text-gray-900 dark:text-gray-400 hover:dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 bg-opacity-15"
                    text/>
            <Button icon="pi pi-sun" v-if="currentTheme == 'light'" @click="toggle"
                    v-tooltip.left="'Включить темную тему'"
                    class="hover:text-gray-900 dark:text-gray-400 hover:dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 bg-opacity-15"
                    text/>
            <Button icon="pi pi-moon" v-if="currentTheme == 'dark'" @click="toggle"
                    v-tooltip.left="'Выбрать тему автоматически'"
                    class="hover:text-gray-900 dark:text-gray-400 hover:dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-gray-600 bg-opacity-15"
                    text/>
          </div>
<!--          <InputText placeholder="Search" type="text" class="w-8rem sm:w-auto"/>-->
          <template v-if="user" >
            <Avatar :image="getAvatar(user.username)" shape="circle"/>
            <LogoutButton />
          </template>
        </div>
      </template>
    </Menubar>
  </div>

</template>
