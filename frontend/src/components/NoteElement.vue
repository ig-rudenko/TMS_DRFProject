<script setup lang="ts">
import {PropType} from "vue";

import {ShortNoteType} from "@/services/notes";
import {getAvatar, verboseDatetime} from "@/services/formats.ts";

defineProps({
  note: {
    required: true,
    type: Object as PropType<ShortNoteType>
  }
})
</script>

<template>
<div class="rounded-xl border dark:border-gray-700 dark:bg-surface-900 w-[20rem] shadow-xl dark:text-gray-300">
  <router-link :to="'/note/'+note.id">
    <img v-if="note.image" :src="note.image" class="rounded-t-xl h-[10rem] w-full object-center object-cover" alt="preview">
  </router-link>
  <div class="p-3">
    <div class="flex justify-between">
      <div class="flex items-center gap-2">
        <Avatar :image="getAvatar(note.owner)"/>
        <div>{{note.owner}}</div>
      </div>
      <div class="flex items-center gap-1">
        <i class="pi pi-calendar"/>
        <div class="text-sm font-normal">{{verboseDatetime(note.updated_at)}}</div>
      </div>
    </div>

    <div class="py-3 text-2xl font-bold">
      <router-link :to="'/note/'+note.id" >{{note.title}}</router-link>
    </div>

    <div class="flex flex-wrap gap-2">
      <div v-for="t in note.tags" class="border-2 px-2 py-1 rounded text-[12px]" :style="{'border-color': '#' + t.color}">{{t.name}}</div>
    </div>
    <div class="py-3 text-sm">{{note.short_content}}</div>
  </div>
</div>
</template>

<style scoped>

</style>