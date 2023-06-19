import MainPage from '@/pages/MainPage'
import SignInPage from '@/pages/SignInPage'
import CartPage from '@/pages/CartPage'
import CatalogPage from '@/pages/CatalogPage'
import ItemPage from '@/pages/ItemPage'
import ChatPage from '@/pages/ChatPage'
import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage,
  },
  {
    path: '/signin',
    name: 'signin',
    component: SignInPage,
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartPage,
  },
  {
    path: '/catalog',
    name: 'catalog',
    component: CatalogPage,
  },
  {
    path: '/item',
    name: 'item',
    component: ItemPage,
  },
  {
    path: '/chat/:id',
    name: 'chat',
    component: ChatPage,
  },
  {
    path: '/chat',
    name: 'chat',
    component: ChatPage,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
