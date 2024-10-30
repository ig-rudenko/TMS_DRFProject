<script setup lang="ts">
import {Ref, ref} from "vue";

const src: Ref<any> = ref(null);

function onFileSelect(event: any) {
  const file = event.files[0];
  const reader = new FileReader();

  reader.onload = async (e) => {
    src.value = e.target?.result;
  };

  reader.readAsDataURL(file);
}
</script>

<template>
  <div class="card flex flex-col items-center pb-2">
    <FileUpload mode="basic" @select="onFileSelect" customUpload auto severity="secondary" class="p-button-outlined"/>
  </div>
  <div v-if="src" class="flex justify-center">
    <img :src="src" class="rounded max-h-[20rem] w-full object-cover object-center" alt="preview">
  </div>
</template>
