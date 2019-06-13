<template>
  <v-container class="container1">
    <v-sheet class="ma-2 pa-3" elevation="12" color="rgb(255, 255, 255,0.6)">
      <div class="display-4">Country Listing</div>
    </v-sheet>
    <v-layout row wrap>
      <v-flex v-for="country in countries.lst" :key="country.country" md2 xs4>
        <v-card class="ma-2" style="background-color: rgb(249, 94, 94,0.4)">
          <v-card-title>
            <div class="display-1">
              <b>{{ country.country }}</b>
            </div>

            <v-img
              :src="
                'https://www.countryflags.io/' +
                  country.countryKey +
                  '/flat/64.png'
              "
              height="50px"
              contain
            ></v-img>
          </v-card-title>
          <v-card-actions style="background-color: rgb(249, 94, 94,0.4)">
            <v-layout column>
              <v-flex v-for="prov in country.provinces" v-bind:key="prov.id">
                <v-btn flat block small @click="gotoProvince(prov.id)">{{
                  prov.name
                }}</v-btn>
              </v-flex>
            </v-layout>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  data: () => ({
    headers: [
      {
        text: 'Title',
        align: 'left',
        sortable: false,
        value: 'title',
        class: 'title'
      }
    ],
    pag: {
      rowsPerPage: 25
    },
    countries: []
  }),
  created: async function() {
    try {
      var response = await axios.get('http://localhost:3000/api/listCountries');
      this.countries = response.data;
    } catch (e) {
      return e;
    }
  },
  methods: {
    gotoProvince: function(prov) {
      this.$router.push('/provinces/' + prov);
    }
  }
};
</script>

<style scoped>
.container1 {
  background-color: rgb(224, 170, 89);
  padding-top: 80px;
  padding-bottom: 80px;
}
</style>
