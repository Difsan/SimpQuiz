import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import LogIn                                  from './components/LogIn.vue'
import Ronda                                 from './components/Ronda.vue'
import Ranking                                from './components/Ranking.vue'

const routes = [
  {
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
    path: '/user/ronda/',
    name: "ronda",
    component: Ronda
  },
  {
    path: '/ranking/',
    name: "ranking",
    component: Ranking
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
