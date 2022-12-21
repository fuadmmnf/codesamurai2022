<template>
  <q-page-container style="padding-left: 65px;padding-right: 65px;">
    <div class="text-h6 flex flex-center" style="margin-bottom: 15px;">⚒ <b>Add New Proposal</b></div>
    <div class="q-pa-md" style="max-width: 100%">

      <q-form
        @submit="onSubmit"
        @reset="onReset"
        class="q-gutter-md"
      >
        <div class="row">
          <div class="col-lg-8 col-md-8">
            <q-input
              filled
              v-model="name"
              label="Project Name"
              hint="Enter project name"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-4 col-md-4" style="padding-left: 10px;">
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
          <div class="col-lg-6 col-md-6">
            <q-input
              filled
              v-model="Latitude"
              step="0.01"
              label="Project Latitude"
              hint="Enter project latitude"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-6 col-md-6" style="padding-left: 10px;">
            <q-input
              class="q-input-padding"
              filled
              v-model="Longitude"
              step="0.01"
              label="Longitude"
              type="number"
              hint="Enter project Longitude"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 col-md-4">
            <q-input
              filled
              v-model="Cost"
              step="0.01"
              label="Project Cost"
              hint="Enter project cost"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-4 col-md-4" style="padding-left: 10px;">
            <q-input
              filled
              v-model="Timespan"
              step="0.01"
              label="Project Timespan"
              hint="Enter project timespan"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-4 col-md-4" style="padding-left: 10px;">
            <q-input
              filled
              v-model="proposal_date"
              hint="Proposal Date"
              type="Date"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
        </div>
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
import {api} from "boot/axios";

export default {
  // name    - TItle of the project
  // Location - Location of the Project
  // Latitude - Latitude of the project
  // Longitude - Longitude of the project
  // Exec - Executing Agency
  // Cost - Projected Cost in crores
  // Timespan - Timespan of the project in years
  // Project_id - unique id of the project
  // Goal - Objective of the project
  // proposal_date    - When was the project proposed
  name: "AddProposal",
  data () {
    return {
      name: '',
      Location: '',
      Latitude: null,
      Longitude: null,
      Exec: '',
      Cost: null,
      Timespan: null,
      proposal_date: null,
    }
  },
  methods: {
    onSubmit(){
      let temp ={
        project_id: "prop"+Math.random(),
        exec: "MOEDU",
        name: this.name,
        location: this.Location,
        start_date: null,
        latitude: this.Latitude,
        longitude: this.Longitude,
        cost: this.Cost,
        timespan: this.Timespan,
        feedback: "",
        rating: null,
        goal: '',
        completion: 0.0,
        actual_cost: 0.0,
        is_accepted: false,
        proposal_date: new Date(this.proposal_date).toISOString().split('T')[0],
        is_deleted: false
      }
      api.post('proposals',temp).then((response)=>{
        if(response.status === 200){
          this.$router.push('/exec/proposals')
        }
      })
    },
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
