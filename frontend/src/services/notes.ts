import api from "@/services/api";
import {NoteFilterType} from "@/services/filter";

export interface Tag {
    name: string;
    color: string;
}

export interface ShortNoteType {
    id: number;
    title: string;
    short_content: string;
    image: string;
    owner: string;
    created_at: string;
    updated_at: string;
    tags: Tag[];
}

interface NoteOwner {
    id: number
    username: string
    first_name: string
    last_name: string
    date_joined: string
}


export interface BaseNoteType {
    title: string;
    content: string;
    image: string;
    tags: Tag[];
}

export interface DetailNoteType extends BaseNoteType{
    id: number;
    owner: NoteOwner;
    created_at: string;
    updated_at: string;
}

export interface NotePaginated {
    count: number
    next: string|null
    previous: string|null
    results: ShortNoteType[]
}
class NoteService {

    async getNotes(page: number, filter: NoteFilterType): Promise<NotePaginated> {
        const searchParams = new URLSearchParams(Object(filter));
        const resp = await api.get<NotePaginated>("/v1/notes?page="+page+"&"+searchParams);
        return resp.data;
    }

    async getNote(id: number|string): Promise<DetailNoteType> {
        const resp = await api.get<DetailNoteType>("/v1/notes/"+id);
        return resp.data;
    }

    async getAllTags(): Promise<Tag[]> {
        const resp = await api.get<Tag[]>("/v1/tags");
        return resp.data;
    }

    async createNote(note: BaseNoteType) {
        const resp = await api.post("/v1/notes", note);
        console.log(resp.data);
        return resp.data;
    }

}

export const noteService = new NoteService();
