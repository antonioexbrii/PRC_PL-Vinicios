<template>
  <v-container grid-list-md text-xs-center class="container1">
    <v-data-table :headers="headers" :items="wineries" :pagination.sync="pag">
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="mdi-warning"
          >Something went wrong fetching Winery data.</v-alert
        >
      </template>
      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td>{{ props.item.name.value }}</td>
          <td>{{ props.item.ctn.value }}</td>
        </tr>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  data: () => ({
    headers: [
      {
        text: 'Name',
        align: 'left',
        sortable: false,
        value: 'title',
        class: 'title'
      },
      {
        text: 'Country',
        align: 'left',
        sortable: false,
        value: 'country',
        class: 'title'
      }
    ],
    pag: {
      rowsPerPage: 25
    },
    wineries: []
  }),
  created: async function() {
    try {
      var response = await axios.get('http://localhost:3000/api/listWineries');
      this.wineries = response.data;
    } catch (e) {
      return e;
    }
  },
  methods: {
    rowClicked: function(item) {
      const id = item.s.value.split('/').reverse()[0];
      this.$router.push('/wineries/' + id);
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
