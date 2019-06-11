<template>
  <v-toolbar app class="toolb">
    <v-toolbar-title class="headline text-uppercase">
      <span>Vinícios</span>
      <span class="font-weight-light">wine reviews</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn @click="$router.push('/')" flat>Home</v-btn>
    <v-btn @click="$router.push('/wines')" flat>Wines</v-btn>
    <v-btn @click="$router.push('/wineries')" flat>Wineries</v-btn>
    <v-btn @click="$router.push('/countries')" flat>Country Listing</v-btn>
    <v-btn @click="$router.push('/about')" flat>About</v-btn>
  </v-toolbar>
</template>

<script>
export default {
  data: function() {
    return {};
  },
  methods: {
    gotoWines: () => {
      this.router.push('/wines/');
    },
    gotoWineries: () => {
      this.router.push('/wineries/');
    },
    gotoCountries: () => {
      this.router.push('/countries/');
    }
  }
};
</script>
<style scoped></style>
