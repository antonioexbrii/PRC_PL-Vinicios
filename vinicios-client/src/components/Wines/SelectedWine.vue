<template>
  <v-container class="container1">
    <v-layout>
      <v-flex>
        <v-img
          :src="require('../../assets/vinho1.jpg')"
          contain
          height="400"
          width="400"
        ></v-img>
      </v-flex>
      <v-flex>
        <v-container v-container grid-list-md text-xs-center>
          <div v-if="wine" class="headline">{{ wine.name.value }}</div>
          <v-sheet>
            <v-icon large>mdi-currency-eur</v-icon>
            <div v-if="wine" class="headline">Price</div>
            <div v-if="wine" class="subheading">{{ wine.price.value }}</div>
          </v-sheet>
          <v-divider></v-divider>
          <v-sheet>
            <v-icon large>mdi-book</v-icon>
            <div v-if="wine" class="headline">Designation</div>
            <div v-if="wine != 'nd'" class="subheading">
              {{ wine.des.value }}
            </div>
          </v-sheet>
          <v-divider></v-divider>
          <v-sheet>
            <v-icon large>mdi-bottle-wine</v-icon>
            <div v-if="wine" class="headline">Variety</div>
            <div v-if="wine" class="subheading">{{ wine.variety.value }}</div>
          </v-sheet>
          <v-divider></v-divider>
          <v-layout>
            <v-flex>
              <div v-if="wine" class="headline">1st Region</div>
              <div v-if="wine" class="subheading">{{ wine.r1.value }}</div>
            </v-flex>
            <v-flex>
              <div v-if="wine.r2" class="headline">2nd Region</div>
              <div v-if="wine.r2" class="subheading">{{ wine.r2.value }}</div>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <v-layout>
            <v-flex>
              <div v-if="wine" class="headline">Province</div>
              <v-btn
                outline
                v-if="wine.provnm"
                @click="gotoProvince(wine.prov.value)"
                >{{ wine.provnm.value }}</v-btn
              >
            </v-flex>
            <v-flex>
              <div v-if="wine" class="headline">Winery</div>
              <v-btn
                outline
                v-if="wine.wnnm"
                @click="gotoWinery(wine.wn.value)"
                >{{ wine.wnnm.value }}</v-btn
              >
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
    <v-divider></v-divider>
    <v-container text-sm-center>
      <div class="display-2">Review by {{ wine.tname.value }}</div>
      <v-sheet elevation6>
        <div class="display-1">{{ wine.points.value }}/100</div>
      </v-sheet>
      <v-flex xs4 offset-xs4>
        <div class="body-1">"{{ wine.descript.value }}"</div>
      </v-flex>

      <a :href="'https://twitter.com/' + wine.ttw.value">
        <v-btn v-if="wine.ttw" round large flat color="blue">
          <v-icon left>mdi-twitter</v-icon>
          <span>{{ wine.ttw.value }}</span>
        </v-btn>
      </a>
    </v-container>
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
.container1 {
  background-color: white;
  padding-left: 5%;
  padding-right: 5%;
  margin-top: 100px;
  padding-top: 80px;
  padding-bottom: 80px;
}
</style>
