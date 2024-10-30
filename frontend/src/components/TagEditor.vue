<script setup lang="ts">
import {PropType, ref, Ref} from "vue";

import {noteService, Tag} from "@/services/notes";

const props = defineProps({
  model: {
    required: true,
    type: Object as PropType<Tag[]>
  }
})

const tags: Ref<Tag[]> = ref([]);

noteService.getAllTags().then(value => tags.value = value);

function appendNewTag() {
  props.model.push({color: "#000", name: ""});
}

function deleteTag(id: number) {
  props.model.splice(id, 1)
}

</script>

<template>
<div>
  <div class="flex flex-wrap gap-2 items-center">
    <div class="text-xl dark:text-gray-300">Добавить теги:</div>
    <Button icon="pi pi-plus" @click="appendNewTag" size="small" />
    <div v-for="(t, index) in model" :key="index" class="p-2 border rounded dark:border-gray-700">
      <ColorPicker v-model="t.color" />
      <InputText v-model="t.name" class="py-1 px-2 border-0 shadow-none" />
      <Button icon="pi pi-times" outlined text severity="danger" @click="() => deleteTag(index)" size="small"/>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>