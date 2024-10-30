<script setup lang="ts">

import NoteFilter from "@/components/NoteFilter.vue";
import {Ref, ref} from "vue";
import {NoteFilterType} from "@/services/filter";
import {NotePaginated, noteService} from "@/services/notes.ts";
import NoteElement from "@/components/NoteElement.vue";
import Welcome from "@/components/Welcome.vue";

const filter: Ref<NoteFilterType> = ref({});

const notes: Ref<NotePaginated|null> = ref(null);

function getPage(page: number) {
  noteService.getNotes(page, filter.value).then(value => notes.value = value)
}

function search() {
  // filter.value = newFilter;
  // console.log(newFilter)
  getPage(1)
}

getPage(1);

</script>

<template>
  <Welcome/>
  <div class="flex justify-center p-6">
    <NoteFilter :filter="filter" @search="search"/>
  </div>
  <div class="flex items-center justify-center p-1 py-6 pb-8">
    <section class="rounded-xl flex flex-col">
      <div v-if="notes" class="flex flex-wrap justify-center gap-3">
        <NoteElement v-if="notes.results.length" v-for="note in notes.results" :key="note.id" :note="note" />
        <div v-else>
          <div class="dark:text-gray-300 text-3xl p-6">Не найдено</div>
        </div>
      </div>

      <div>
        <Paginator @page="p => getPage(p.page+1)" v-if="notes?.next || notes?.previous" :rows="100" :totalRecords="notes.count"></Paginator>
      </div>
    </section>
  </div>
</template>

<style scoped>

</style>