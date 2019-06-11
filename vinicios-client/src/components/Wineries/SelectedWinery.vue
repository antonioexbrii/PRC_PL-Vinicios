<template>
  <v-container class="container1">
    <v-layout>
      <v-flex>Imagem aqui</v-flex>
      <v-flex>
        <v-container v-container grid-list-md text-xs-center>
          <v-sheet>
            <v-icon large>mdi-city</v-icon>
            <div v-if="winery" class="headline">Winery Name</div>
            <div v-if="winery" class="subheading">{{ winery.name.value }}</div>
          </v-sheet>
          <v-divider></v-divider>
          <v-sheet>
            <v-icon large>mdi-bottle-wine</v-icon>
            <div class="headline">Wine Listing</div>
            <v-btn outline @click="btnClick(winery.wn.value)">{{
              winery.wtit.value
            }}</v-btn>
          </v-sheet>
          <v-divider></v-divider>
        </v-container>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  props: ['wineryID'],
  data: () => ({
    winery: {}
  }),
  created: async function() {
    try {
      var getTitle = await axios.get(
        'http://localhost:3000/api/wineries/getTitle/' + this.wineryID
      );
      var title = getTitle.data[0].tit.value;
      const elem = {
        title
      };
      var resp = await axios.post(
        'http://localhost:3000/api/wineries/getWinery',
        elem
      );
      this.winery = resp.data[0];
    } catch (e) {
      return e;
    }
  },
  methods: {
    btnClick: function(item) {
      var id = item.split('/').reverse()[0];
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
</style>
