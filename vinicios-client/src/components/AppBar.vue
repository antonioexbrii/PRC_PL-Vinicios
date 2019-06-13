<template>
  <v-toolbar app color="rgb(224, 158, 96)">
    <v-toolbar-title class="headline text-uppercase">
      <span>Vinícios</span>
      <span class="font-weight-light">wine reviews</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn outline large @click="$router.push('/')">Home</v-btn>
    <v-btn outline large @click="$router.push('/wines')">Wines</v-btn>
    <v-btn outline large @click="$router.push('/countries')"
      >Country Listing</v-btn
    >
    <v-btn outline large @click="$router.push('/about')">About</v-btn>
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
<style scoped>
.toolb {
  background-color: saddlebrown;
}
</style>
