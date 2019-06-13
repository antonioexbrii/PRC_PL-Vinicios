<template>
  <div>
    <HomeComponent />
    <WineListing />
    <CountryListing />
  </div>
</template>

<script>
import HomeComponent from '../components/HomeComponent';
import WineListing from '@/components/Wines/WineListing';
import CountryListing from '@/components/Countries/CountryListing';

export default {
  components: {
    HomeComponent,
    WineListing,
    CountryListing
  }
};
</script>
<style></style>
