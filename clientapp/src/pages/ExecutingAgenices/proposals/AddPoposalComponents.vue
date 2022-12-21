<template>
  <q-page-container style="padding-left: 65px;padding-right: 65px;">
    <div class="text-h6 flex flex-center" style="margin-bottom: 15px;">⚒ <b>Add New Project</b></div>
    <div class="q-pa-md" style="max-width: 100%">

      <q-form
        @submit="onSubmit"
        class="q-gutter-md"
      >
        <q-input
          filled
          v-model="component_id"
          label="Component id"
          hint="Enter component id"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please enter something']"
        />
        <q-input
          class="q-input-padding"
          filled
          v-model="component_type"
          label="Component type"
          hint="Enter component type"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please enter something']"
        />

        <q-input
          filled
          v-model="budget_ratio"
          step="0.01"
          label="Budget Ration"
          hint="Enter Budget Ration"
          type="number"
          lazy-rules
          :rules="[ val => val && val.length > 0 || 'Please enter something']"
        />

        <q-input
          class="q-input-padding"
          filled
          v-model="depends_on_id"
          label="Dependent on"
          hint="Enter dependent id"
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
      component_id: '',
      component_type: '',
      budget_ratio: '',
      depends_on_id: '',
      project_id: ''
    }
  },
  mounted() {
    console.log('here')
    this.project_id = this.$route.params.project_id;
  },
  methods: {
    onSubmit(){
      let temp = {
        component_id: this.component_id,
        component_type: this.component_type,
        budget_ratio: this.budget_ratio,
        depends_on_id: this.depends_on_id,
        execution_agency: "MOEDU",
        project_id: this.project_id
      }
      api.post(`projects/${this.project_id}/components`,temp).then((response)=>{
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
