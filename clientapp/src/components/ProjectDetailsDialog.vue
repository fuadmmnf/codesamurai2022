<template>
  <div class="q-pa-md q-gutter-sm">
    <q-dialog
      v-model="dialog"
      persistent
      :maximized="true"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <q-card class="">
        <q-bar>
          <q-space/>

          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip content-class="bg-white text-primary">Close</q-tooltip>
          </q-btn>
        </q-bar>

        <q-card-section>
          <div v-if="projectDetail !== null">
            <div class="row q-pa-md ">
              <div class="col">
                <table class="text-left">
                  <caption class="text-h6">Project Details</caption>
                  <tr>
                    <th>Project Name:</th>
                    <td>{{ projectDetail.project_name }}</td>
                  </tr>
                  <tr>
                    <th>Category:</th>
                    <td>{{ projectDetail.category }}</td>
                  </tr>
                  <tr>
                    <th>Affiliated Agency:</th>
                    <td>{{ projectDetail.affiliated_agency }}</td>
                  </tr>
                  <tr>
                    <th>Description:</th>
                    <td>{{ projectDetail.description }}</td>
                  </tr>
                  <tr>
                    <th>Project Start Time:</th>
                    <td>{{ projectDetail.project_start_time }}</td>
                  </tr>
                  <tr>
                    <th>Project Completion Time:</th>
                    <td>{{ projectDetail.project_completion_time }}</td>
                  </tr>
                  <tr>
                    <th>Total Budget:</th>
                    <td>{{ projectDetail.total_budget }}</td>
                  </tr>
                  <tr>
                    <th>Completion Percentage:</th>
                    <td>{{ projectDetail.completion_percentage }}</td>
                  </tr>
                  <tr>
                    <th>Percent of Time Gone:</th>
                    <td>
                      <q-linear-progress stripe rounded size="20px" :value="timeGonePercentage" color="warning"
                                         class="q-ma-sm" style="width: 90%">
                        <div class="absolute-full flex flex-center">
                          <q-badge color="white" text-color="accent" :label="`${timeGonePercentage*100.0}%`"/>
                        </div>
                      </q-linear-progress>
                    </td>
                  </tr>
                </table>
              </div>
              <div class="col">
                <h6 class="text-center">form</h6>
              </div>

            </div>
          </div>
        </q-card-section>

        <!--        <q-card-section class="q-pt-none">-->
        <!--          <div v-if="projectDetail !== null">-->
        <!--            {{projectDetail.location_coordinates}}-->
        <!--          </div>-->

        <!--        </q-card-section>-->
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import {date} from "quasar";

export default {
  name: "ProjectDetailsDialog",
  mounted() {
    this.$root.$on('marker-click', (project) => {
      this.dialog = true
      this.projectDetail = project
    })
  },
  data() {
    return {
      dialog: false,
      projectDetail: null
    }
  },
  computed: {
    timeGonePercentage() {
      const totalDays = date.getDateDiff(new Date(this.projectDetail.project_completion_time), new Date(this.projectDetail.project_start_time), 'days')
      const goneDays = date.getDateDiff(new Date(), new Date(this.projectDetail.project_start_time), 'days')
      console.log(totalDays, goneDays)
      if (goneDays < 0) return 0
      if (goneDays > totalDays) return 1
      return (goneDays / totalDays.toFixed(2)).toFixed(2)
    }
  }
}
</script>

<style scoped>
table, th, td {
  border: 1px solid black;
}
</style>
