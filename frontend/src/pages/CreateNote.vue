<script setup lang="ts">
import {useStore} from "vuex";
import {onBeforeMount, Ref, ref} from "vue";

import Editor from "@/components/Editor.vue";
import TagEditor from "@/components/TagEditor.vue";
import UploadNotePreview from "@/components/UploadNotePreview.vue";
import router from "@/router";
import {errorToast, successToast} from "@/services/my.toast";
import {BaseNoteType, noteService} from "@/services/notes";
import errorFmt from "@/services/errorFmt.ts";

onBeforeMount(async () => {
  const store = useStore();
  if (!store.state.auth.status.loggedIn) await router.push("/auth/login");
})

const file = ref<File|null>(null);

const note: Ref<BaseNoteType> = ref({
  title: "",
  content: "",
  image: "",
  tags: [],
})

async function createNote() {
  if (!file.value) return;
  const {image_url} = await noteService.uploadImage(file.value);
  note.value.image = image_url;

  noteService.createNote(note.value).then(
      (note) => {
        successToast("Запись создана", "");
        router.push("/note/"+note.id)
      }
  ).catch(reason => errorToast("Ошибка", errorFmt(reason)))
}

</script>

<template>
<div class="md:w-2/3 mx-auto p-4">
  <div>
    <UploadNotePreview @fileSelect="(f: File) => file = f" />
  </div>

  <div class="flex justify-center p-4">
    <Button label="Создать" icon="pi pi-file" @click="createNote" />
  </div>

  <div class="flex flex-col gap-2 py-3">
    <label for="title" class="text-xl dark:text-gray-300">Название</label>
    <InputText id="title" v-model="note.title" fluid/>
  </div>

  <TagEditor :model="note.tags"/>

  <div class="py-3">
    <Editor @update:modelValue="(v: string) => note.content = v" />
  </div>
</div>
</template>

<style scoped>

</style>