<template>
  <div>
    <v-container>
      <HomeComponent />
      <FlexIcons />
    </v-container>
  </div>
</template>

<script>
import HomeComponent from '../components/HomeComponent';
import FlexIcons from '../components/FlexIcons';

export default {
  components: {
    HomeComponent,
    FlexIcons
  }
};
</script>
