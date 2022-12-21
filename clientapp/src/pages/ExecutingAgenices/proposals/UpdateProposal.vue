<template>
  <q-page-container style="padding-left: 65px;padding-right: 65px;" v-if="project">
    <div class="text-h6 flex flex-center" style="margin-bottom: 15px;">⚒ <b>Update Proposal</b></div>
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
          <div class="col-lg-6 col-md-6" style="padding-left: 10px;">
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
        </div>

        <div class="flex flex-center">
          <q-btn label="Save Changes" type="submit" color="primary"/>
        </div>
      </q-form>

    </div>
  </q-page-container>
</template>

<script>
import {ref} from "vue";
import {api} from "boot/axios";

export default {
  name: "ExecUpdateProposal",
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
      project_id: '',
      project: null,
    }
  },
  mounted() {
    this.project_id = this.$route.params.project_id;
    api.get(`proposals/${this.project_id}`).then((response) => {
      this.project = response.data.data
      this.name = this.project.project_name
      this.Location = this.project.location
      this.Latitude = this.project.latitude
      this.Longitude = this.project.longitude
      this.Cost = this.project.cost
      this.Timespan = this.project.timespan
      this.proposal_date = this.project.proposal_date
    })
  },
  methods: {
    onSubmit(){
      let temp ={
        project_id: this.project.project_id,
        exec: "MOEDU",
        name: this.name,
        location: this.Location,
        start_date: this.project.start_date,
        latitude: this.Latitude,
        longitude: this.Longitude,
        cost: this.Cost,
        timespan: this.Timespan,
        feedback: "",
        rating: null,
        goal: '',
        completion: this.project.completion,
        actual_cost: this.project.actual_cost,
        is_accepted: this.project.is_accepted,
        proposal_date: this.project.proposal_date,
        is_deleted: this.project.is_deleted
      }
      api.put('proposals',temp).then((response)=>{
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
