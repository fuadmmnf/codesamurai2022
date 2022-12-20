<template>
  <div class="q-pa-md">
    <q-table
      class="my-sticky-header-table"
      title="📁 Proposals (DPPs)"
      :data="rows"
      :columns="columns"
      row-key="name"
      :filter="filter"
    >
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" v-model="filter" placeholder="Search">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-btn style="margin-left: 10px;" text-color="white" color="brown-5" label="+ Add Proposals"
               @click="$router.push('/exec/proposals/add')"/>
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
          <q-td key="Timespan" :props="props">
            {{ props.row.Timespan }}
          </q-td>
          <q-td key="Timespan" :props="props" style="align-items: end">
            <q-btn style="margin-left: 10px;" text-color="white" color="brown-5" label="Details"
                   @click="$router.push('/exec/proposals/detail')"/>
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'ExecProposalsIndex',
  data () {
    return {
      filter: ref(''),
      columns: [
        // name    - TItle of the project
        // Location - Location of the Project
        // Latitude - Latitude of the project
        // Longitude - Longitude of the project
        // Exec - Executing Agency
        // Cost - Projected Cost in crores
        // Timespan - Timespan of the project in years
        // Project_id - unique id of the project
        // Goal - Objective of the project
        // proposal_date    - When was the project proposed
        {
          name: 'name', required: true, label: 'Project Name', align: 'left', field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'Location', align: 'center', label: 'Location', field: 'Location', sortable: true },
        { name: 'Exec', label: 'Executing Agency', field: 'Exec', sortable: true },
        { name: 'Cost', label: 'Cost', field: 'Cost', sortable: true },
        { name: 'Timespan', label: 'Timespan', field: 'Timespan' },
        { name: 'actions', label: 'Actions', field: 'action', sortable: true }
      ],
      rows: [
        {
          name: "Fazlul Rahman Memorial General Hospital",
          Location: "Tarabo",
          Exec: "LGD",
          Cost: 1000000,
          Timespan: '2'
        }

      ]
    }
  }
}
</script>
<style lang="sass">
.my-sticky-header-table

  .q-table__top,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    background-color: #52DBCA

</style>
