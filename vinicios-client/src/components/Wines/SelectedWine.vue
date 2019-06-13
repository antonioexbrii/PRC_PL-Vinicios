<template>
  <v-container>
    <v-card
      class="cont1 mb-2"
      grid-list-md
      text-xs-center
      transition="slide-x-transition"
    >
      <v-card-title>
        <div v-if="wine" class="display-1">{{ wine.name.value }}</div>
      </v-card-title>
      <v-card-text>
        <v-layout>
          <v-flex xs12 md3 class="mt-3">
            <v-icon>mdi-currency-eur</v-icon>
            <div v-if="wine" class="headline">Price</div>
            <div v-if="wine" class="subheading">{{ wine.price.value }}</div>
          </v-flex>
          <v-flex xs12 md3 class="mt-3">
            <v-icon>mdi-book</v-icon>
            <div v-if="wine" class="headline">Designation</div>
            <div v-if="wine != 'nd'" class="subheading">
              {{ wine.des.value }}
            </div>
          </v-flex>
          <v-flex xs12 md3 class="mt-3">
            <v-icon>mdi-bottle-wine</v-icon>
            <div v-if="wine" class="headline">Variety</div>
            <div v-if="wine" class="subheading">{{ wine.variety.value }}</div>
          </v-flex>
          <v-flex xs12 md4 class="mt-3">
            <v-icon>mdi-pier</v-icon>
            <div v-if="wine" class="headline">Winery</div>
            <div v-if="wine" class="subheading">{{ wine.wnnm.value }}</div>
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
        <v-layout>
          <v-flex xs12 md4 class="mt-3">
            <div v-if="wine" class="headline">1st Region</div>
            <div v-if="wine" class="subheading">{{ wine.r1.value }}</div>
          </v-flex>
          <v-flex xs12 md4 class="mt-3">
            <div v-if="wine.r2" class="headline">2nd Region</div>
            <div v-if="wine.r2" class="subheading">{{ wine.r2.value }}</div>
          </v-flex>
          <v-flex xs12 md4 class="mt-3">
            <div v-if="wine" class="headline">Visit Province</div>
            <v-btn
              outline
              @click="gotoProvince(wine.prov.value)"
              class="subheading"
              >{{ wine.provnm.value }}</v-btn
            >
          </v-flex>
        </v-layout>
        <v-divider></v-divider>
      </v-card-text>
    </v-card>
    <v-card elevation="18" class="cont1">
      <v-card-title>
        <div class="display-1 mr-5">
          Review by
          <b>{{ wine.tname.value }}</b>
        </div>
        <a :href="'https://twitter.com/' + wine.ttw.value">
          <v-chip color="blue">
            <v-icon>mdi-twitter</v-icon>
            <div class="body-1">{{ wine.ttw.value }}</div>
          </v-chip>
        </a>
      </v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <div class="subheading mt-3 mb-3">
          <i>"{{ wine.descript.value }}"</i>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-sheet color="rgb(229, 137, 50)" class="pa-2">
          <div class="headline">
            <b>{{ wine.points.value }}</b
            >/100
          </div>
        </v-sheet>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  props: ['wineID'],
  data: () => ({
    wine: {}
  }),
  created: async function() {
    try {
      var getTitle = await axios.get(
        'http://localhost:3000/api/wines/getTitle/' + this.wineID
      );
      var title = getTitle.data[0].tit.value;
      const elem = {
        title
      };
      var resp = await axios.post(
        'http://localhost:3000/api/wines/getWine',
        elem
      );
      this.wine = resp.data[0];
    } catch (e) {
      return e;
    }
  },
  methods: {
    gotoWinery: function(wn) {
      const id = wn.split('/').reverse()[0];
      this.$router.push('/wineries/' + id);
    },
    gotoProvince: function(prov) {
      const id = prov.split('/').reverse()[0];
      this.$router.push('/provinces/' + id);
    }
  }
};
</script>

<style scoped>
.lay1 {
  padding-top: 80px;
  padding-bottom: 80px;
}
.cont1 {
  background-color: rgb(224, 170, 89, 0.8);
}
</style>
