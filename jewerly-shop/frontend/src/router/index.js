import MainPage from '@/pages/MainPage'
import SignInPage from '@/pages/SignInPage'
import CartPage from '@/pages/CartPage'
import CatalogPage from '@/pages/CatalogPage'
import ItemPage from '@/pages/ItemPage'
import TestPage from '@/pages/TestPage'

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
    path: '/test',
    name: 'test',
    component: TestPage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
