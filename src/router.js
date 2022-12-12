import { createRouter, createWebHistory } from "vue-router";

import App from './App.vue';
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Look from './components/Look.vue'
import Registrar from './components/Registrar.vue'
import PersonalRe from './components/PersonalRe.vue'
import FamiliarRe from './components/FamiliarRe.vue'

const routes = [{
    path: '/',
    name: 'root',
    component: App
},
{
    path: '/user/logIn',
    name: "logIn",
    component: LogIn
},
{
    path: '/user/signUp',
    name: "signUp",
    component: SignUp
},
{
    path: '/user/home',
    name: "home",
    component: Home
},
{
    path: '/user/home/Look',
    name: "look",
    component: Look
},
{
    path: '/user/home/RegistrarPaciente',
    name: "registrar",
    component: Registrar
},
{
    path: '/user/home/RegistrarPersonal',
    name: "personal",
    component: PersonalRe
},
{
    path: '/user/home/RegistrarFamiliar',
    name: "familiar",
    component: FamiliarRe
}
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;
