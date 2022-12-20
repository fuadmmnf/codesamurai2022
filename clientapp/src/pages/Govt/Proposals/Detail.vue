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
              <th class="text-left ">Timepsan</th>
              <td class="text-left">159</td>
            </tr>
            <tr>
              <th class="text-left ">Proposal Date</th>
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
                <q-btn @click="$router.push('/govt/projects/update')">Approve</q-btn>
                <q-btn @click="$router.push('/govt/projects/update')">Reject</q-btn>
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
import Gantt from "components/gantt.vue";
export default {
  name: "ProposalDetails",
  components: {
    Gantt
  },
  data(){
    return{
      tab: 'details'
    }
  }
}
</script>

<style scoped>

</style>
