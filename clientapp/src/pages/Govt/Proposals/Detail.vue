<template>
  <div class="q-pa-md">
    <div class="text-h6" style="margin-left: 17px; margin-bottom: 15px;">Project Name</div>
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
  </div>
</template>

<script>
export default {
  name: "ProposalDetails"
}
</script>

<style scoped>

</style>
