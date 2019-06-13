<template>
  <v-layout class="lay1" justify-center>
    <v-flex class="flex1" xs12 md5>
      <v-img
        :src="require('../assets/vinicios.svg')"
        contain
        height="400"
      ></v-img>
    </v-flex>
    <v-flex xs12 md7>
      <v-layout row wrap>
        <v-flex xs12>
          <v-card elevation="12" flat color="rgb(255, 255, 255,0.6)">
            <v-card-title>
              <div class="display-4">
                Welcome to
                <b>Vinícios</b>.
              </div>
            </v-card-title>
            <v-card-text>
              <div class="headline">
                Vinícios is a web application dedicated to expose the best wines
                in the world. Get spot on information from the best enologists
                worldwide, and broaden your knowledge and selection of wines. To
                know more about the Vinícios Project, head to the 'About'
                section.
              </div>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn outline @click="$router.push('/wines')"
                >Browse Wine Collection</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-flex class="mt-2" xs6 md4 offset-md4>
          <v-card elevation="18" color="rgb(249, 94, 94,0.4)">
            <v-card-title>
              <div class="display-2">Our Review Collection</div>
              <div class="subheading">
                Browse through a sample database with over 10,000 entries.
              </div>
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn outline @click="$router.push('/reviews')"
                >Browse Reviews</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-flex class="mt-2" xs6 md4>
          <v-card elevation="18" color="rgb(249, 94, 94,0.4)">
            <v-card-title>
              <div class="display-2">The finest Wineries</div>
              <div class="subheading">
                Choose a Wine House for a complete wine listing, and info on the
                House's location.
              </div>
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn outline @click="$router.push('/wineries')"
                >Browse Wineries</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-flex class="mt-2" xs6 md4 offset-md8>
          <v-card elevation="18" color="rgb(249, 94, 94,0.4)">
            <v-card-title>
              <div class="display-2">Browse by Country</div>
              <div class="subheading">
                Pick your favourite wines by country of origin, separated by
                province.
              </div>
            </v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn outline @click="$router.push('/countries')"
                >Browse Countries</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>
<script>
import FlexIcons from './FlexIcons';
export default {
  data: () => ({
    components: {
      FlexIcons
    }
  })
};
</script>
<style scoped>
.lay1 {
  padding-top: 70px;
}
.flex1 {
  padding-top: 80px;
}
</style>
