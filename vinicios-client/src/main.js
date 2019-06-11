import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';
import store from './store';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import '@mdi/font/css/materialdesignicons.css';
Vue.config.productionTip = false;
Vue.use(Vuetify, {
  iconfont: 'mdi'
});
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
