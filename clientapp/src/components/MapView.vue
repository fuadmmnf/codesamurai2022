<template>
  <l-map style="height: 300px" :zoom="zoom" :center="center">
    <ProjectDetailsDialog/>

    <l-tile-layer :url="url"></l-tile-layer>

    <div v-for="projectInfo in projectsInfo" :key="projectInfo.id">
      <div v-for="(coord,idx) in parseCoords(projectInfo)" :key="`${projectInfo.id}_${idx}`">
        <l-marker :lat-lng="coord" @click="showDescription(projectInfo)"></l-marker>
      </div>

    </div>
    <!--      <l-control-zoom position="bottomright" />-->
    <l-control>

      <q-btn label="Filter Projects" icon="filter_alt" color="primary" @click="showFilterDialog=true"/>
      <q-dialog v-model="showFilterDialog" :position="'right'" persistent>
        <q-card>
          <q-bar>
            <div class="text-subtitle1  text-center">Filter by Category/ Daterange</div>

            <q-space />

            <q-btn dense flat icon="close" v-close-popup>
              <q-tooltip>Close</q-tooltip>
            </q-btn>
          </q-bar>

          <q-card-section class="items-center no-wrap">
            <div class="q-mb-md">
              <q-select outlined v-model="filter.category" :options="projectCategories"
                        label="Select Project Category"/>

            </div>

            <q-input filled v-model="filter.startDate" mask="date" :rules="['date']" label="Project Staring Date">
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="filter.startDate">
                      <div class="row items-center justify-end">
                        <q-btn v-close-popup label="Close" color="primary" flat/>
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>


            <q-input filled v-model="filter.endDate" mask="date" :rules="['date']" label="Project Ending Date">
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="filter.endDate">
                      <div class="row items-center justify-end">
                        <q-btn v-close-popup label="Close" color="primary" flat/>
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
            <div class="row justify-center">
              <q-btn outline color="primary" label="Apply" @click="applyFiltering"/>
              <q-btn outline color="danger" label="Clear" @click="resetFiltering"/>
            </div>

          </q-card-section>
        </q-card>
      </q-dialog>
    </l-control>
  </l-map>


</template>

<script>
import projectsJson from 'src/assets/projects'
import {LMap, LTileLayer, LMarker, LControl} from "vue2-leaflet";
import {date} from 'quasar'

import "leaflet/dist/leaflet.css";
import {Icon} from "leaflet";
import ProjectDetailsDialog from "components/ProjectDetailsDialog";

delete Icon.Default.prototype._getIconUrl;
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

export default {
  name: "MapView",
  components: {
    ProjectDetailsDialog,
    LMap,
    LTileLayer,
    LMarker,
    LControl
  },
  data() {
    return {
      showFilterDialog: false,
      filter: {
        category: null,
        startDate: null,
        endDate: null,
      },
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        "",
      zoom: 15,
      center: [23.732590, 90.395632],
      projectsInfo: projectsJson(),
      markerLatLng: [23.732590, 90.395632]
    };
  },
  methods: {
    parseCoords(project) {
      let coords = []
      const points = project.location_coordinates.replace(/[()]/g, '').replace(/\s/g, '').split(",")
      for (let i = 0; i < points.length; i = i + 2) {
        coords.push([parseFloat(points[i]), parseFloat(points[i + 1])])

      }
      return coords
    },
    showDescription(projectInfo) {
      this.$root.$emit('marker-click', projectInfo)
    },
    resetFiltering() {
      this.filter = {
        category: null,
        startDate: null,
        endDate: null,
      }

    },
    applyFiltering() {
      this.projectsInfo = projectsJson()
      if (this.filter.category !== null) {
        this.projectsInfo = this.projectsInfo.filter(project => project.category === this.filter.category)
      }

      if (this.filter.startDate !== null) {
        this.projectsInfo = this.projectsInfo.filter(project => date.getDateDiff(new Date(project.project_start_time), this.filter.startDate, 'days') >= 0)
      }
      if (this.filter.endDate !== null) {
        this.projectsInfo = this.projectsInfo.filter(project => date.getDateDiff(this.filter.endDate, new Date(project.project_completion_time), 'days') >= 0)
      }
    }
  },
  computed: {
    // a computed getter
    projectOffices() {
      // `this` points to the component instance
      let coords = []
      for (const project of this.projectsInfo) {
        const points = project.location_coordinates.replace(/[()]/g, '').replace(/\s/g, '').split(",")
        console.log(points);
        for (let i = 0; i < points.length; i = i + 2) {
          coords.push([parseFloat(points[i]), parseFloat(points[i + 1])])
        }
      }
      return coords
    },
    projectCategories() {
      return [...new Set(projectsJson().map(project => project.category))]
    }
  }
};
</script>

<style scoped>

</style>
