<template>
  <SelectedProvince :provinceID="$route.params.id" />
</template>

<script>
import SelectedProvince from '@/components/Provinces/SelectedProvince';
export default {
  components: {
    SelectedProvince
  }
};
</script>
