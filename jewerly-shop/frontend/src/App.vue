<template>
  <div id="app">
    <header-component />
    <router-view />
    <footer-component />
  </div>
</template>

<script>
import FooterComponent from './components/FooterComponent.vue';
import HeaderComponent from './components/HeaderComponent.vue';

export default {
  name: 'app',
  components: { FooterComponent, HeaderComponent }
}
</script>

<style>
main {
  min-height: calc(100vh - 516px);
}
</style>