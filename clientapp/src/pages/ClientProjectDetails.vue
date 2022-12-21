<template>
  <div class="q-pa-md" v-if="project">
    <div class="text-h6" style="margin-left: 17px; margin-bottom: 15px;">{{ project.project_name }}</div>
    <q-card>
      <q-tabs
        v-model="tab"
        active-color="primary"
        align="justify"
        class="text-grey"
        dense
        indicator-color="primary"
      >
        <q-tab label="Details" name="details"/>
        <q-tab label="Gantt Chart" name="gantt"/>
        <q-tab label="Feedback" name="feedback"/>
      </q-tabs>

      <q-separator/>

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="details">
          <q-markup-table class="myTable">
            <tbody>
            <tr>
              <th class="text-left ">Location</th>
              <td class="text-left">{{ project.location }}</td>
            </tr>
            <tr>
              <th class="text-left ">Latitude</th>
              <td class="text-left">{{ project.latitude }}</td>
            </tr>
            <tr>
              <th class="text-left ">Longitude</th>
              <td class="text-left">{{ project.longitude }}</td>
            </tr>
            <tr>
              <th class="text-left ">Executing Company</th>
              <td class="text-left">{{ project.exec }}</td>
            </tr>
            <tr>
              <th class="text-left ">Cost</th>
              <td class="text-left">{{ project.cost }}</td>
            </tr>
            <tr>
              <th class="text-left ">Actual Cost</th>
              <td class="text-left">{{ project.actual_cost }}</td>
            </tr>
            <tr>
              <th class="text-left ">Timepsan</th>
              <td class="text-left">{{ project.timespan }}</td>
            </tr>
            <tr>
              <th class="text-left ">Start Date</th>
              <td class="text-left">{{ project.start_date }}</td>
            </tr>
            <tr>
              <th class="text-left ">Completion</th>
              <td class="text-left">{{ project.completion }}</td>
            </tr>
            </tbody>
          </q-markup-table>
        </q-tab-panel>
        <q-tab-panel name="gantt">
          <div style="height: 70vh">
            <Gantt></Gantt>
          </div>
        </q-tab-panel>

        <q-tab-panel name="feedback">
          <div class="text-h6">Submit your feedback</div>
          <div>
            <div class="q-pa-md" style="max-width: 800px">

              <q-form
                @submit="onsubmit"
                class="q-gutter-md"
              >
                <q-input
                  filled
                  v-model="feedback"
                  label="Feedback"
                  hint="Please, write Your feedback"
                  lazy-rules
                  :rules="[ val => val && val.length > 0 || 'Please type something']"
                />
                <q-rating hint=""
                          size="xl"
                          color="negative"
                          v-model="ratingModel" :max="5"
                          icon="star_border"
                          icon-selected="star"
                          no-dimming/>
                <span>Current Rating for project {{ ratingModel }}/5</span>


                <div class="flex flex-center">
                  <q-btn label="Submit" type="submit" color="primary"/>
                </div>
              </q-form>

            </div>
          </div>
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script>
import Gantt from "components/gantt.vue";
import {api} from "boot/axios";
import { jsPDF } from "jspdf";

export default {
  name: "ClientProjectDetails",
  components: {
    Gantt
  },
  data() {
    return {
      feedback: '',
      ratingModel: 3,
      tab: 'details',
      project_id: '',
      project: null,
    }
  },
  mounted() {
    this.project_id = this.$route.params.project_id;
    api.get(`projects/${this.project_id}`).then((response) => {
      this.project = response.data.data
      this.ratingModel = this.project.rating!=null ? this.project.rating : 0;
      this.feedback = this.project.feedback
      this.ratingModel = this.project.rating
      console.log(this.project)
    })
  },
  methods: {
    onsubmit() {
      let temp={
        project_id: this.project.project_id,
        exec: "MOEDU",
        project_name: this.project.project_name,
        location: this.project.location,
        start_date: this.project.start_date,
        latitude: this.project.latitude,
        longitude: this.project.longitude,
        cost: this.project.cost,
        timespan: this.project.timespan,
        feedback: this.feedback,
        rating: this.ratingModel,
        goal: this.project.goal,
        completion: this.project.completion,
        actual_cost: this.project.actual_cost,
        is_accepted: true,
        is_deleted: false
      }
      api.put('projects',temp).then((response)=>{
        if(response.status === 200){
          this.$router.push('/client/projects')
        }
      })
    },

  }
}
</script>

<style scoped>

</style>
