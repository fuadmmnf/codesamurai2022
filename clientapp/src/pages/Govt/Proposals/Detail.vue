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
              <th class="text-left ">Rating</th>
              <td class="text-left"><q-rating hint=""
                                              size="xl"
                                              color="negative"
                                              v-model="ratingModel" :max="5"
                                              icon="star_border"
                                              icon-selected="star"
                                              no-dimming/></td>
            </tr>
            <tr>
              <th class="text-left ">Actions</th>
              <td class="text-left">
                <q-btn @click="onApproval">Approve</q-btn>
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
      ratingModel: null
    }
  },
  mounted() {
    this.proposal_id = this.$route.params.project_id;
    api.get(`proposals/${this.proposal_id}`).then((response) => {
      this.proposal = response.data.data
      this.ratingModel = this.proposal.rating!=null ? this.proposal.rating : 0;
    })
  },
  methods:{
    onApproval(){
      let temp={
        project_id: this.proposal.project_id,
        exec: "MOEDU",
        name: this.proposal.project_name,
        location: this.proposal.location,
        start_date: this.proposal.start_date,
        latitude: this.proposal.latitude,
        longitude: this.proposal.longitude,
        cost: this.proposal.cost,
        timespan: this.proposal.timespan,
        feedback: this.proposal.feedback,
        rating: this.proposal.rating,
        goal: this.proposal.goal,
        completion: this.proposal.completion,
        actual_cost: this.proposal.actual_cost,
        is_accepted: true,
        is_deleted: false
      }
      api.put('proposals',temp).then((response)=>{
        if(response.status === 200){
          this.$router.push('/govt/proposals')
        }
      })
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
