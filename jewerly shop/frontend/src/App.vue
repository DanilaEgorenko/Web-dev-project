<template>
  <div id="app">
    <header-component/>
    <router-view/>
    <footer-component/>
  </div>
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import FooterComponent from './components/FooterComponent.vue';

export default {
  name: 'app',
  components: { FooterComponent, HeaderComponent }
}
</script>
