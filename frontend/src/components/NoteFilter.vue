<script setup lang="ts">
import {PropType, ref} from "vue";
import TagSelect from "@/components/TagSelect.vue";
import {NoteFilterType} from "@/services/filter";
import {Tag} from "@/services/notes";

const emits = defineEmits(["search"])

const props = defineProps({
  filter: {
    required: true,
    type: Object as PropType<NoteFilterType>,
  }
})

const dates = ref(null);

const showFiltersDetail = ref(false);


function setTags(tags: Tag[]) {
  const newTags: string[] = []
  tags.forEach(value => newTags.push(value.name))
  props.filter.tags = newTags
}

function search() {

  if (dates.value) {
    props.filter.from_date = (<Date>dates.value[0]).toISOString();
    if (dates.value[1]) props.filter.to_date = (<Date>dates.value[1]).toISOString();
  }
  emits("search");
}

</script>

<template>
<div class="flex flex-col flex-wrap justify-center gap-2">
  <div class="flex gap-1 md:min-w-[30rem]">
    <Button @click="showFiltersDetail=!showFiltersDetail" :outlined="!showFiltersDetail" icon="pi pi-filter"/>
    <InputText @keydown.enter="search" placeholder="Поиск" id="search" input-class="w-full" fluid v-model="props.filter.search" />
    <Button @click="search" icon="pi pi-search"/>
  </div>

  <div v-if="showFiltersDetail" class="flex flex-wrap flex-col md:flex-row gap-2">
    <div>
      <DatePicker placeholder="Даты" fluid v-model="dates" inputId="date-range" selectionMode="range" :manualInput="false" />
    </div>
    <div>
      <InputText @keydown.enter="search" fluid placeholder="Автор" v-model="props.filter.owner"/>
    </div>
    <div>
      <TagSelect @update:modelValue="setTags" />
    </div>
  </div>
</div>
</template>

<style scoped>

</style>