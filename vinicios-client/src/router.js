import Vue from 'vue';
import Router from 'vue-router';
Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Home.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('./views/About.vue')
    },
    {
      path: '/wines',
      name: 'wines',
      component: () => import('./views/Wines/Wines.vue')
    },
    {
      path: '/wines/:id',
      name: 'selectedWine',
      component: () => import('./views/Wines/SelectedWine.vue')
    },
    {
      path: '/wineries',
      name: 'wineries',
      component: () => import('./views/Wineries/Wineries.vue')
    },
    {
      path: '/wineries/:id',
      name: 'selectedWinery',
      component: () => import('./views/Wineries/SelectedWinery.vue')
    },
    {
      path: '/countries',
      name: 'countries',
      component: () => import('./views/Countries/Countries.vue')
    },
    {
      path: '/provinces/:id',
      name: 'selectedProvince',
      component: () => import('./views/Provinces/SelectedProvince.vue')
    }
  ]
});
