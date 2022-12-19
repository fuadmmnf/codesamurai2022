<template>
  <l-map style="height: 300px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <div v-for="(projectOffice, idx) in projectOffices" :key="idx">
      <l-marker :lat-lng="projectOffice"></l-marker>
    </div>
  </l-map>
</template>

<script>
import projectsJson from 'src/assets/projects'
import { LMap, LTileLayer, LMarker } from "vue2-leaflet";
import "leaflet/dist/leaflet.css";
import { Icon } from "leaflet";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

export default {
  name: "MapView",
  components: {
    LMap,
    LTileLayer,
    LMarker
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        "",
      zoom: 15,
      center: [23.732590, 90.395632],
      projectsInfo: projectsJson(),
      markerLatLng: [23.732590, 90.395632]
    };
  },
  computed: {
    // a computed getter
    projectOffices() {
      // `this` points to the component instance
      let coords = []
      for(const project of  this.projectsInfo){
        const points = project.location_coordinates.replace(/[()]/g, '').replace(/\s/g,'').split(",")
        console.log(points);
        for (let i=0; i<points.length; i=i+2){
          coords.push([parseFloat(points[i]), parseFloat(points[i+1])])
        }
      }
      return coords
    }
  }
};
</script>

<style scoped>

</style>
