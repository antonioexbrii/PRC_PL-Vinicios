<template>
  <SelectedWinery :wineryID="$route.params.id" />
</template>

<script>
import SelectedWinery from '@/components/Wineries/SelectedWinery';
export default {
  components: { SelectedWinery }
};
</script>

<style lang="scss" scoped></style>
