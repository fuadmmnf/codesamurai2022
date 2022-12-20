<template>
  <q-page>
    <div class="q-pa-md">
      <div class="text-h6" style="margin-left: 17px; margin-bottom: 15px;">🏣 Executing Agency Dashboard</div>
      <div class="row">
        <div class="col-lg-4 col-md-6">
          <q-card
            class="my-card shadow-15 myMaxWidth myPointer" style="margin-top: 1%;margin-bottom: 2%;"
            @click="$router.push('/exec/projects')"
          >
            <q-card-section>
              <div class="text-h6">⚒ Projects</div>
              <q-badge class="text-black" color="green" style="margin-left: 2px;"><b>Completed</b>
              </q-badge>
              /
              <q-badge class="text-black" color="warning" style="margin-left: 2px;"><b>Running</b>
              </q-badge>
              <div class="text-subtitle1">See all on going projects and their current status</div>
            </q-card-section>
          </q-card>
        </div>
        <div class="col-lg-4 col-md-6">
          <q-card
            class="my-card shadow-15 myMaxWidth myPointer" style="margin-top: 1%;margin-bottom: 2%;"
            @click="$router.push('/exec/proposals')"
          >
            <q-card-section>
              <div class="text-h6">📁 Proposals (DPPs)</div>
              <q-badge class="text-black" color="green" style="margin-left: 2px;"><b>Accepted</b>
              </q-badge>
              /
              <q-badge class="text-white" color="red" style="margin-left: 2px;"><b>Rejected</b>
              </q-badge>
              /
              <q-badge class="text-black" color="warning" style="margin-left: 2px;"><b>Pending</b>
              </q-badge>
              <div class="text-subtitle1">See all submitted proposals and their current status</div>
            </q-card-section>
          </q-card>
        </div>
      </div>

    </div>

  </q-page>
</template>

<script>
export default {
  name: "govtIndex"
}
</script>

<style scoped>
.myMaxWidth{
  background-color: #BFDED8;
  margin-left: 15px;
  margin-right: 15px;
}
.myPointer{
  cursor: pointer;
}
</style>
