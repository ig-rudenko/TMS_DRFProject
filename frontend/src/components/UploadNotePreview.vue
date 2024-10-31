<script setup lang="ts">
import {Ref, ref} from "vue";
import {FileUploadSelectEvent} from "primevue/fileupload";

const emits = defineEmits(["fileSelect"]);

const src: Ref<any> = ref(null);
const file: Ref<File|null> = ref(null);

function onFileSelect(event: FileUploadSelectEvent) {
  file.value = event.files[0];
  const reader = new FileReader();

  reader.onload = async (e) => {
    src.value = e.target?.result;
  };

  if (file.value) reader.readAsDataURL(file.value);
  emits("fileSelect", file.value);
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
