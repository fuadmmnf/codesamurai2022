<template>
  <div class="q-pa-md">
    <div class="text-h6" style="margin-left: 17px; margin-bottom: 15px;">Project Name</div>
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
      </q-tabs>

      <q-separator/>

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="details">
          <q-markup-table class="myTable">
            <tbody>
            <tr>
              <th class="text-left ">Location</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Latitude</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Longitude</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Executing Company</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Cost</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Actual Cost</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Timepsan</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Start Date</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Completion</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Goal</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Actions</th>
              <td class="text-left">
                <q-btn>Delete</q-btn>
                <q-btn @click="$router.push('/govt/projects/update')">Update</q-btn>
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
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script>
import {ref} from 'vue'
import Gantt from "components/gantt.vue";

export default {
  // name    - TItle of the project
  // Location - Location of the Project
  // Latitude - Latitude of the project location
  // Longitude - Longitude of the project location
  // Exec - Executing Agency
  // Cost - Projected Cost in crores
  // Timespan - Timespan of the project in years
  // Project_id - Unique id of the project
  // Goal - Goals of the project
  // Start_date - Date of project start
  // Completion - Percentage of project completed
  // Actual_cost - Actual cost of the project to date
  name: 'ProjectDetails',
  components: {
    Gantt
  },
  data() {
    return {
      filter: ref(''),
      tab: 'details'
    }
  },
  methods: {},
}
</script>
<style scoped>
.myTable{
  margin-left: 15px;
  margin-right: 15px;
}

</style>
