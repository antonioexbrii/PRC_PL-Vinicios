<template>
  <v-container grid-list-md text-xs-center class="container1">
    <v-data-table :headers="headers" :items="wines" :pagination.sync="pag">
      <template v-slot:no-data>
        <v-alert :value="true" color="error" icon="mdi-warning"
          >Something went wrong fetching Wine data.</v-alert
        >
      </template>
      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td>{{ props.item.wine.value }}</td>
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
    wines: []
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
