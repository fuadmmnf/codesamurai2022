<template>
  <div class="q-pa-md" v-if="proposal">
    <div class="text-h6" style="margin-left: 17px; margin-bottom: 15px;">{{ proposal.project_name }}</div>
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
              <td class="text-left">{{ proposal.location  }}</td>
            </tr>
            <tr>
              <th class="text-left ">Latitude</th>
              <td class="text-left">{{ proposal.latitude }}</td>
            </tr>
            <tr>
              <th class="text-left ">Longitude</th>
              <td class="text-left">{{ proposal.longitude }}</td>
            </tr>
            <tr>
              <th class="text-left ">Executing Company</th>
              <td class="text-left">{{ proposal.exec }}</td>
            </tr>
            <tr>
              <th class="text-left ">Cost</th>
              <td class="text-left">{{ proposal.cost }}</td>
            </tr>
            <tr>
              <th class="text-left ">Timepsan</th>
              <td class="text-left">{{ proposal.timespan }}</td>
            </tr>
            <tr>
              <th class="text-left ">Proposal Date</th>
              <td class="text-left">{{ proposal.proposal_date}}</td>
            </tr>
            <tr>
              <th class="text-left ">Actions</th>
              <td class="text-left">
                <q-btn @click="$router.push('/govt/projects/update')">Approve</q-btn>
                <q-btn @click="onReject">Reject</q-btn>
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
import {api} from "boot/axios";
export default {
  name: "ProposalDetails",
  components: {
    Gantt
  },
  data(){
    return{
      tab: 'details',
      proposal_id: '',
      proposal: null,
    }
  },
  mounted() {
    this.proposal_id = this.$route.params.project_id;
    api.get(`proposals/${this.proposal_id}`).then((response) => {
      this.proposal = response.data.data
    })
  },
  methods:{
    onApproval(){

    },
    onReject(){
      api.delete(`proposals/${this.proposal_id}`).then((response) => {
        this.$router.push('/govt/proposals')
      })
    }
  }
}
</script>

<style scoped>

</style>
