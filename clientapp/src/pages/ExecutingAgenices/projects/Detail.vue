<template>
  <div class="q-pa-md">
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
        <q-tab label="Update project" name="update"/>
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
            <tr>
              <th class="text-left ">Actions</th>
              <td class="text-left">
                <q-btn>Report</q-btn>
              </td>
            </tr>
            </tbody>
          </q-markup-table>
        </q-tab-panel>
        <q-tab-panel name="gantt">
          <div style="height: 70vh">
            <Gantt></Gantt>
          </div>
        </q-tab-panel>

        <q-tab-panel name="update">
          <div>
            <div class="q-pa-md" style="max-width: 800px; height: 100vh;">
              <q-form
                @submit="onSubmit"
                class="q-gutter-md"
                style="margin-top: 10px; padding-right: 10px; padding-left: 10px"
              >
                <q-input
                  filled
                  v-model="actual_cost"
                  step="0.01"
                  label="Actual Project Cost"
                  hint="Enter actual cost"
                  type="number"
                  lazy-rules
                  :rules="[ val => val && val.length > 0 || 'Please enter something']"
                />
                <q-input
                  class="q-input-padding"
                  filled
                  v-model="timespan"
                  step="0.01"
                  label="Timespan"
                  type="number"
                  hint="Enter project Longitude"
                  lazy-rules
                  :rules="[ val => val && val.length > 0 || 'Please enter something']"
                />

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
import {ref} from 'vue'
import Gantt from "components/gantt.vue";
import {api} from "boot/axios";

export default {
  name: 'ExecProjectDetails',
  components: {
    Gantt
  },
  data() {
    return {
      filter: ref(''),
      tab: 'details',
      actual_cost: null,
      timespan: null,
      project_id: '',
      project: null,
    }
  },
  mounted() {
    this.project_id = this.$route.params.project_id;
    api.get(`projects/${this.project_id}`).then((response) => {
      this.project = response.data.data
      this.actual_cost = this.project.actual_cost
      this.timespan = this.project.timespan
    })
  },
  methods: {
    onSubmit(){
      let temp={
        project_id: this.project.project_id,
        exec: "MOEDU",
        project_name: this.project.project_name,
        location: this.project.location,
        start_date: this.project.start_date,
        latitude: this.project.latitude,
        longitude: this.project.longitude,
        cost: this.project.cost,
        timespan: this.timespan,
        feedback: this.project.feedback,
        rating: this.project.rating,
        goal: this.project.goal,
        completion: this.project.completion,
        actual_cost: this.actual_cost,
        is_accepted: true,
        is_deleted: false
      }
      api.put('projects',temp).then((response)=>{
        if(response.status === 200){
          this.$router.push('/govt/projects')
        }
      })
    },
    onReset(){}
  },
}
</script>
<style scoped>
.myTable{
  margin-left: 15px;
  margin-right: 15px;
}

</style>
