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
                <q-btn>Delete</q-btn>
                <q-btn @click="$router.push(`/govt/projects/update/${project.project_id}`)">Update</q-btn>
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
import {api} from "boot/axios";

export default {
  name: 'ProjectDetails',
  components: {
    Gantt
  },
  data() {
    return {
      filter: ref(''),
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
    })
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
