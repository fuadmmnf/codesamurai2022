<template>
  <div class="q-pa-md q-gutter-sm">
    <q-dialog
      v-model="dialog"
      persistent
      :maximized="true"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <q-card class="bg-primary text-white">
        <q-bar>
          <q-space />

          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
          </q-btn>
        </q-bar>

        <q-card-section>
          <div v-if="projectDetail !== null">
            <div class="text-h6">{{projectDetail.project_name}}</div>
          </div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div v-if="projectDetail !== null">
            {{projectDetail.location_coordinates}}
          </div>

        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "ProjectDetailsDialog",
  mounted() {
    this.$root.$on('marker-click', (project) => {
      this.dialog = true
      this.projectDetail = project
    })
  },
  data () {
    return {
      dialog: false,
      projectDetail: null
    }
  }
}
</script>

<style scoped>

</style>
