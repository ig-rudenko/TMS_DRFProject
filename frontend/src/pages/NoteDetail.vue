<script setup lang="ts">
import {Ref, ref} from "vue";
import {useRoute} from "vue-router";

import {DetailNoteType, noteService} from "@/services/notes";
import {getAvatar, textToHtml, verboseDatetime} from "@/services/formats";

const noteID = useRoute().params.id.toString();

console.log(noteID)

const note: Ref<DetailNoteType|null> = ref(null);

noteService.getNote(noteID).then(value => note.value = value);

</script>

<template>
<div class="md:w-2/3 mx-auto p-4">

  <div v-if="note" class="dark:text-gray-300">
    <div v-if="note.image" class="flex justify-center">
      <img :src="note.image" class="rounded max-h-[20rem] w-full object-cover object-center" alt="preview">
    </div>

    <div class="flex justify-between">
      <h2 class="my-4 p-5 border-l-4 border-gray-700 text-3xl font-bold">{{note.title}}</h2>

      <div class="flex gap-4">
        <div class="flex items-center gap-1">
          <i class="pi pi-calendar"/>
          <div class="text-sm font-normal">{{verboseDatetime(note.updated_at)}}</div>
        </div>
        <div class="flex items-center gap-2">
          <Avatar :image="getAvatar(note.owner.username)"/>
          <div>{{note.owner.username}}</div>
        </div>
      </div>

    </div>

    <div class="flex flex-wrap gap-2 p-4">
      <div v-for="t in note.tags" class="border-2 px-2 py-1 rounded text-[12px]" :style="{'border-color': '#' + t.color}">{{t.name}}</div>
    </div>

    <div class="py-4" v-html="textToHtml(note.content)">
    </div>

  </div>

</div>
</template>

<style scoped>

</style>