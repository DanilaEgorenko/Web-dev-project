import Vue from 'vue'
import App from './App.vue'
import router from './router'
import GAuth from 'vue-google-oauth2'


Vue.config.productionTip = false

Vue.use(GAuth, {clientId: '507077891165-iplglfuq6h8rm6huk96opjrgg08li2vm.apps.googleusercontent.com'})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

