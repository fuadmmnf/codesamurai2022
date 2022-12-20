<template>
  <div>
    <div class="q-pa-md">
      <q-table
        class="my-sticky-header-table"
        title="⚒ Projects"
        :data="rows"
        :columns="columns"
        row-key="name"
        :filter="filter"
      >
        <template v-slot:top-right>
          <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search"/>
            </template>
          </q-input>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="name" :props="props">
              {{ props.row.name }}
            </q-td>
            <q-td key="Location" :props="props">
              {{ props.row.Location }}
            </q-td>
            <q-td key="Exec" :props="props">
              {{ props.row.Exec }}
            </q-td>
            <q-td key="Cost" :props="props">
              {{ props.row.Cost }}
            </q-td>
            <q-td key="Start_date" :props="props">
              {{ props.row.Start_date }}
            </q-td>
            <q-td key="Start_date" :props="props" style="align-items: end">
              <q-btn style="margin-left: 10px;" text-color="white" color="brown-5" label="Details"
                     @click="$router.push('/client/projects/detail')"/>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue'
import {api} from "boot/axios"

export default {
  name: 'ClientProjects',
  data() {
    return {
      filter: ref(''),
      columns: [
        // name    - TItle of the project
        // Location - Location of the Project
        // Latitude - Latitude of the project location
        // Longitude - Longitude of the project location
        // Exec - Executing Agency
        // Cost - Projected Cost in crores
        // Timespan - Timespan of the project in years
        // Project_id - Unique id of the project
        // Goal - Goals of the project
        // Start_date - Date of project start
        // Completion - Percentage of project completed
        // Actual_cost - Actual cost of the project to date

        {
          name: 'name', required: true, label: 'Project Name', align: 'left', field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {name: 'Location', align: 'center', label: 'Location', field: 'Location', sortable: true},
        {name: 'Exec', label: 'Executing Agency', field: 'Exec', sortable: true},
        {name: 'Cost', label: 'Cost', field: 'Cost', sortable: true},
        {name: 'Start_date', label: 'Start Date', field: 'Start_date'},
        {name: 'actions', label: 'Actions', field: 'actions', sortable: true}
      ],
      rows: [
        {
          name: " Fazlul Rahman Memorial General Hospital",
          Location: "Tarabo",
          Exec: "LGD",
          Cost: 1000000,
          Start_date: '2023-01-02'
        }

      ]
    }
  },
  mounted(){
    api.get('projects').then((response)=>{
      console.log(response.data)
    })
  },
  methods: {},
}
</script>
<style lang="sass">
.my-sticky-header-table

  .q-table__top,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    background-color: #B3CDF5

</style>
