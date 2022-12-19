<template>
  <q-page>
    <MapView style="min-height: 94.5vh"/>
  </q-page>
</template>

<script>
import MapView from "components/MapView.vue";

export default {
  name: 'PageIndex',
  components: { MapView }
}
</script>
