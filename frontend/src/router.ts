import {createRouter, createWebHistory} from "vue-router";

import Home from "@/pages/Home.vue";
import Auth from "@/pages/Auth.vue";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: Home},
        {path: '/note/:id', component: () => import("@/pages/NoteDetail.vue")},
        {path: '/create', component: () => import("@/pages/CreateNote.vue")},
        {
            path: '/auth', component: Auth, children: [
                {path: '/auth/login', component: () => import("@/components/LoginForm.vue")},
                {path: '/auth/signup', component: () => import("@/components/RegisterForm.vue")},
            ]
        }
    ],
});

export default router;