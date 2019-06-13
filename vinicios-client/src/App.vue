<template>
  <v-app>
    <AppBar />
    <v-container class="container1">
      <router-view />
    </v-container>
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
<style>
.container1 {
  background-image: url('~@/assets/bg.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
}
</style>
