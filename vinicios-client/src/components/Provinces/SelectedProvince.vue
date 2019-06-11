<template>
  <v-container class="container1" column>
    <div class="headline">
      {{ province.provinceName }}, {{ province.countryName }}
    </div>
    <v-layout row wrap justify-center>
      <v-flex
        xs3
        v-for="wine in province.wines"
        v-bind:key="wine.wine.value"
        class="flex1"
      >
        <v-card height="100%">
          <v-card-title>
            <div class="subheading">{{ wine.wnnm.value }}</div>
          </v-card-title>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat @click="gotoWine(wine.wine.value)">View</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  props: ['provinceID'],
  data: () => ({
    province: {
      countryName: '',
      provinceName: '',
      wines: []
    }
  }),
  created: async function() {
    try {
      var resp = await axios.get(
        'http://localhost:3000/api/provinces/getProvince/' + this.provinceID
      );
      this.province.countryName = resp.data[0].ctn.value;
      this.province.provinceName = resp.data[0].tit.value;
      this.province.wines = resp.data;
    } catch (e) {
      return e;
    }
  },
  methods: {
    gotoWine: function(item) {
      const id = item.split('/').reverse()[0];
      this.$router.push('/wines/' + id);
    }
  }
};
</script>

<style scoped>
.container1 {
  background-color: white;
  padding-left: 5%;
  padding-right: 5%;
  padding-top: 100px;
}
.flex1 {
  margin: 5px;
}
</style>
