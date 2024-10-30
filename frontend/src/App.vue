<template>
  <Header/>
  <router-view />
  <Toast />
</template>

<script setup lang="ts">
import Toast from 'primevue/toast';
import Header from "@/components/Header.vue";

</script>
