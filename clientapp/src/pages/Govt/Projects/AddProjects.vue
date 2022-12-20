<template>
  <q-page-container style="padding-left: 65px;padding-right: 65px;">
    <div class="text-h6 flex flex-center" style="margin-bottom: 15px;">⚒ <b>Add New Project</b></div>
    <div class="q-pa-md" style="max-width: 100%">

      <q-form
        @submit="onSubmit"
        @reset="onReset"
        class="q-gutter-md"
      >
        <div class="row">
          <div class="col-lg-8 col-md-8 col-sm-4 col-xs-2">
              <q-input
                filled
                v-model="name"
                label="Project Name"
                hint="Enter project name"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please enter something']"
              />
          </div>
          <div class="col-lg-4 col-md-4 col-sm-3 col-xs-2" style="padding-left: 10px;">
            <q-input
              class="q-input-padding"
              filled
              v-model="Location"
              label="Location"
              hint="Enter project location"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-3 col-xs-2">
            <q-input
              filled
              v-model="Latitude"
              label="Project Latitude"
              hint="Enter project latitude"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-6 col-md-6 col-sm-3 col-xs-2" style="padding-left: 10px;">
            <q-input
              class="q-input-padding"
              filled
              v-model="name"
              label="Longitude"
              type="number"
              hint="Enter project Longitude"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-3 col-xs-2">
            <q-input
              filled
              v-model="Cost"
              label="Project Cost"
              hint="Enter project cost"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-6 col-md-6 col-sm-3 col-xs-2" style="padding-left: 10px;">
            <q-input
              filled
              v-model="Timespan"
              label="Project Timespan"
              hint="Enter project timespan"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
        </div>


        <q-input
          filled
          v-model="Goal"
          label="Project Goal"
          hint="Enter project goal"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please enter something']"
        />
        <div class="flex flex-center">
          <q-btn label="Submit" type="submit" color="primary"/>
          <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
        </div>
      </q-form>

    </div>
  </q-page-container>
</template>

<script>
import {ref} from "vue";

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
  name: "AddProjects",
  data () {
    return {
      name: '',
      Location: '',
      Latitude: null,
      Longitude: null,
      Exec: '',
      Cost: null,
      Timespan: null,
      Goal: '',
      Start_date: null,
      Completion: 0,
      Actual_cost: 0,
    }
  },
  methods: {
    onSubmit(){},
    onReset(){},
  }
}
</script>

<style scoped>
my-q-input-padding{
  margin-left: 7px;
  margin-right: 7px;
}
</style>
