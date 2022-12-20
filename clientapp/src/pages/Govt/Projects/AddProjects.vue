<template>
  <q-page-container style="padding-left: 65px;padding-right: 65px;">
    <div class="text-h6 flex flex-center" style="margin-bottom: 15px;">⚒ <b>Add New Project</b></div>
    <div class="q-pa-md" style="max-width: 100%">

      <q-form
        @submit="onSubmit"
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
              label="Longitude"
              step="0.01"
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
              label="Project Cost"
              step="0.01"
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
              label="Project Timespan"
              step="0.01"
              hint="Enter project timespan"
              type="number"
              lazy-rules
              :rules="[ val => val && val.length > 0 || 'Please enter something']"
            />
          </div>
          <div class="col-lg-4 col-md-4" style="padding-left: 10px;">
            <q-input
              filled
              v-model="Start_date"
              hint="Start Date"
              type="Date"
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
        </div>
      </q-form>

    </div>
  </q-page-container>
</template>

<script>
import {ref} from "vue";
import {api} from "boot/axios";

export default {
  name: "AddProjects",
  data () {
    return {
      name: '',
      Location: '',
      Latitude: 0.0,
      Longitude: 0.0,
      Exec: '',
      Cost: 0.0,
      Timespan: 0.0,
      Goal: '',
      Start_date: null,
      Completion: 0.0,
      Actual_cost: 0.0,
    }
  },
  methods: {
    onSubmit(){
      let temp = {
        project_id: "prop"+Math.random(),
        exec: "MOEDU",
        project_name: this.name,
        location: this.Location,
        start_date: new Date(this.Start_date).toISOString().split('T')[0],
        latitude: this.Latitude,
        longitude: this.Longitude,
        cost: this.Cost,
        timespan: this.Timespan,
        feedback: "",
        rating: null,
        goal: this.Goal,
        completion: 0.0,
        actual_cost: 0.0,
        is_accepted: true,
        is_deleted: false
      }
      api.post('projects',temp).then((response)=>{
        if(response.status === 200){
          this.$router.push('/govt/projects')
        }
      })
    },
  }
}
</script>

<style scoped>
my-q-input-padding{
  margin-left: 7px;
  margin-right: 7px;
}
</style>
