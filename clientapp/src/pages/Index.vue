<template>
  <q-page class="flex flex-center">
    <MapView/>
  </q-page>
</template>

<script>
import MapView from "components/MapView.vue";

export default {
  name: 'PageIndex',
  components: { MapView }
}
</script>
