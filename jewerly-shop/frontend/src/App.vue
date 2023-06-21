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
import Cookies from 'js-cookie';


export default {
  name: 'app',
  components: { FooterComponent, HeaderComponent },
  methods: {
    loginWithJWT() {
      const api = process.env.VUE_APP_BACKEND_URL + '/api/' || 'http://localhost:8000/api/';
      const jwt_token = Cookies.get('jwt');

      fetch(api + "get_user/", {
        headers: {
          "Authorization": "Bearer " + jwt_token
        }
      })
      .then(res => res.json())
      .then(data => {
        localStorage.setItem('username', data.username);
        localStorage.setItem('email', data.email);
        localStorage.setItem('picture', data.picture);
        this.$router.push('/').catch(()=>{});
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    if (Cookies.get('jwt') !== undefined && localStorage.getItem('username') == undefined) {
      this.loginWithJWT();
    }

    this.$root.$on('loginWithJWT', this.loginWithJWT);
  }
}
</script>

<style>
main {
  min-height: calc(100vh - 516px);
}
</style>