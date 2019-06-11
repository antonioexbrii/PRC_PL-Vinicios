<template>
  <v-container grid-list-md text-xs-center class="container1">
    <div class="headline">List of Provinces by Country</div>
    <v-card>
      <v-expansion-panel>
        <v-expansion-panel-content
          v-for="country in countries.lst"
          :key="country.country"
        >
          <template v-slot:header>
            <div>{{ country.country }}</div>
          </template>
          <v-card v-for="prov in country.provinces" v-bind:key="prov.id">
            <v-btn flat block @click="gotoProvince(prov.id)">{{
              prov.name
            }}</v-btn>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-card>
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
  background-color: white;
  padding-left: 5%;
  padding-right: 5%;
  margin-top: 100px;
  padding-top: 80px;
  padding-bottom: 80px;
}
</style>
