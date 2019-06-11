<template>
  <v-container fill-height grid-list-md text-xs-center>
    <v-layout justify-center class="lay1">
      <v-flex sm3 xs4 class="flex1">
        <v-card flat>
          <v-img
            :src="require('../assets/vinicios.svg')"
            stretch
            height="200"
            width="200"
            aspect-ratio="2.75"
          ></v-img>
          <v-card-title>
            <div class="display-2">Review Collection</div>
            <div class="headline md0">
              Browse through a sample database with over 10,000 entries.
            </div>
          </v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat @click="$router.push('/reviews')">Browse Reviews</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex sm3 xs4 class="flex1">
        <v-card flat>
          <v-img
            :src="require('../assets/vinicios.svg')"
            stretch
            height="200"
            width="200"
          ></v-img>
          <v-card-title>
            <div class="display-2">The finest Wineries</div>
            <div class="headline md0">
              Choose a Wine House for a complete wine listing.
            </div>
          </v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat @click="$router.push('/wineries')"
              >Browse Wineries</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-flex sm3 xs4 class="flex1">
        <v-card flat>
          <v-img
            :src="require('../assets/vinicios.svg')"
            height="200"
            width="200"
          ></v-img>
          <v-card-title>
            <div class="display-2">Browse by Country</div>
            <div class="headline md0">
              Pick your favourite wines by country of origin.
            </div>
          </v-card-title>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat @click="$router.push('/countries')"
              >Browse Countries</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({})
};
</script>
<style scoped>
.flex1 {
  margin: 2%;
}
.container2 {
  background-color: indigo;
}
.lay1 {
  background-color: white;
}
</style>
