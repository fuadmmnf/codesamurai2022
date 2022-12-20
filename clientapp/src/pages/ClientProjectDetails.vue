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
        <th class="text-left ">Actual Cost</th>
        <td class="text-left">159</td>
      </tr>
      <tr>
        <th class="text-left ">Timepsan</th>
        <td class="text-left">159</td>
      </tr>
      <tr>
        <th class="text-left ">Start Date</th>
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
      </tbody>
    </q-markup-table>
    <div>
      <div class="q-pa-md" style="max-width: 800px">

        <q-form
          @submit="onSubmit"
          @reset="onReset"
          class="q-gutter-md"
        >
          <q-input
            filled
            v-model="name"
            label="Feedback"
            hint="Please, write Your feedback"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
          />
          <q-rating hint=""
                    size="xl"
                    color="negative"
                    v-model="ratingModel" :max="5"
                    icon="star_border"
                    icon-selected="star"
                    no-dimming/>
          <span>Current Rating for project 4/5</span>



          <div class="flex flex-center">
            <q-btn label="Submit" type="submit" color="primary"/>
            <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm"/>
          </div>
        </q-form>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "ClientProjectDetails",
  data(){
    return{
      feedback: '',
      ratingModel: 3
    }
  }
}
</script>

<style scoped>

</style>
