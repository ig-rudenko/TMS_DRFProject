<script setup lang="ts">
import {Ref, ref} from "vue";

import {noteService, Tag} from "@/services/notes";

const selectedTags = ref();
const tags: Ref<Tag[]> = ref([]);

noteService.getAllTags().then(value => tags.value = value);

</script>

<template>
  <MultiSelect v-model="selectedTags" :options="tags" optionLabel="name" filter placeholder="Теги" display="chip" class="w-full md:w-80">
    <template #option="slotProps">
      <div class="flex items-center">
        <div class="border-2 px-2 py-1 rounded text-[12px]" :style="{'border-color': '#' + slotProps.option.color}">{{slotProps.option.name}}</div>
      </div>
    </template>
    <template #dropdownicon>
      <i class="pi pi-tag" />
    </template>
    <template #header>
      <div class="font-medium px-3 py-2">Доступные теги</div>
    </template>
  </MultiSelect>
</template>
