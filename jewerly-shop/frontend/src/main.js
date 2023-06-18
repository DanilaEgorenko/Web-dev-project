import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false;
Vue.prototype.$api = process.env.VUE_APP_BACKEND_URL + '/api/' || 'http://localhost:8000/api/';

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
