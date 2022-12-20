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
        <q-tab label="Update project" name="update"/>
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
                @reset="onReset"
                class="q-gutter-md"
                style="margin-top: 10px; padding-right: 10px; padding-left: 10px"
              >
                <q-input
                  filled
                  v-model="actual_cost"
                  label="Actual Project Cost"
                  hint="Enter actual cost"
                  type="number"
                  lazy-rules
                  :rules="[ val => val && val.length > 0 || 'Please enter something']"
                />
                <q-input
                  class="q-input-padding"
                  filled
                  v-model="name"
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
  name: 'ExecProjectDetails',
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
