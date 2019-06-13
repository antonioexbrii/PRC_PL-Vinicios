<template>
  <v-container class="container1">
    <v-sheet class="ma-2 pa-3" elevation="12" color="rgb(255, 255, 255,0.6)">
      <div class="display-4">Wine Listing</div>
    </v-sheet>
    <v-layout row wrap>
      <v-flex md6>
        <v-sheet class="ma-1 pb-1">
          <v-text-field
            class="ma-2"
            v-model="search"
            append-icon="mdi-search"
            label="Search"
            single-line
            hide-details
          ></v-text-field>
        </v-sheet>
        <v-data-table
          class="t1 ma-1"
          :headers="headers"
          :items="wines"
          :search="search"
          :pagination.sync="pag"
        >
          <template v-slot:no-data>
            <v-alert :value="true" color="error" icon="mdi-warning"
              >Something went wrong fetching Wine data.</v-alert
            >
          </template>
          <template v-slot:items="props">
            <tr @click="rowClicked(props.item)" :key="props.item">
              <td>
                <div class="headline">{{ props.item.points.value }}</div>
              </td>
              <td>
                <div class="subheading">{{ props.item.wine.value }}</div>
              </td>
              <td>
                <div class="subheading">{{ props.item.price.value }} €</div>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-flex>
      <v-flex md6>
        <v-sheet color="rgb(255,255,255,0.1)" class="ma-1">
          <transition name="fade">
            <SelectedWine :v-show="show" :key="idw" :wineID="idw" />
          </transition>
        </v-sheet>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios';
import SelectedWine from '@/components/Wines/SelectedWine';
export default {
  components: {
    SelectedWine
  },
  data: () => ({
    headers: [
      {
        text: 'Points',
        align: 'center',
        sortable: true,
        value: 'points.value'
      },
      {
        text: 'Title',
        align: 'center',
        sortable: true,
        value: 'wine.value'
      },
      {
        text: 'Price',
        align: 'center',
        sortable: true,
        value: 'price.value'
      }
    ],
    wines: [],
    idw: '',
    show: false,
    search: '',
    pag: {
      rowsPerPage: 10
    }
  }),
  created: async function() {
    try {
      var response = await axios.get('http://localhost:3000/api/listWines');
      this.wines = response.data;
    } catch (e) {
      return e;
    }
  },
  methods: {
    rowClicked: function(item) {
      const id = item.w.value.split('/').reverse()[0];
      this.idw = id;
      this.show = true;
    }
  }
};
</script>

<style scoped>
.container1 {
  padding-top: 100px;
}
.t1 .v-table tbody tr td {
  background-color: bisque;
}
.fade-enter-active {
  transition: opacity 1.25s ease-out;
}
.fade-leave-active {
  transition: 0s;
}
.fade-enter,
fade-leave-to {
  opacity: 0;
}
</style>
