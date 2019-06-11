<template>
  <v-container fill-height grid-list-xl class="container1">
    <v-layout>
      <v-flex md4>
        <v-img
          :src="require('../assets/vinicios.svg')"
          contain
          height="400"
          width="400"
        ></v-img>
      </v-flex>
      <v-flex md5>
        <v-card flat>
          <v-card-title>
            <div class="display-3">Welcome to Vinícios.</div>
          </v-card-title>
          <v-card-text>
            <p>
              Vinícios is a web application dedicated to expose the best wines
              in the world. Get spot on information from the best enologists
              worldwide, and broaden your knowledge and selection of wines.
            </p>
            <p>
              To know more about the Vinícios Project, head to the 'About'
              section.
            </p>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn flat @click="$router.push('/wines')"
              >Browse Wine Collection</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
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
.container1 {
  background-color: white;
  padding-left: 5%;
  padding-right: 5%;
  margin-top: 100px;
  padding-top: 80px;
  padding-bottom: 80px;
}
.l1 {
  background-color: '#5b024b';
}
</style>
