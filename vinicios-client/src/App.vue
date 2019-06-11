<template>
  <v-app>
    <AppBar />
    <router-view />
    <Footer />
  </v-app>
</template>

<script>
import AppBar from '@/views/AppBar';
import Footer from '@/views/Footer';
export default {
  name: 'App',
  components: {
    AppBar,
    Footer
  }
};
</script>
