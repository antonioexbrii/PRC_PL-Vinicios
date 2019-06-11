<template>
  <SelectedWine :wineID="$route.params.id" />
</template>

<script>
import SelectedWine from '@/components/Wines/SelectedWine';
export default {
  components: {
    SelectedWine
  }
};
</script>
