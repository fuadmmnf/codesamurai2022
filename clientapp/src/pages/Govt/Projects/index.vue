<template>
  <div v-if="rows">
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
          <q-btn style="margin-left: 10px;" text-color="white" color="brown-5" label="+ Add Project"
                 @click="$router.push('/govt/projects/add')"/>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="name" :props="props">
              {{ props.row.project_name }}
            </q-td>
            <q-td key="location" :props="props">
              {{ props.row.location }}
            </q-td>
            <q-td key="exec" :props="props">
              {{ props.row.exec_id }}
            </q-td>
            <q-td key="cost" :props="props">
              {{ props.row.cost }}
            </q-td>
            <q-td key="start_date" :props="props">
              {{ props.row.start_date }}
            </q-td>
            <q-td key="actions" :props="props" style="align-items: end">
              <q-btn style="margin-left: 10px;" text-color="white" color="brown-5" label="Details"
                     @click="$router.push(`/govt/projects/detail/${props.row.project_id}`)"/>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue'
import {api} from "boot/axios";

export default {
  name: 'GovtProjectIndex',
  data() {
    return {
      filter: ref(''),
      columns: [
        {
          name: 'name', required: true, label: 'Project Name', align: 'left', field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {name: 'location', align: 'center', label: 'Location', field: 'location', sortable: true},
        {name: 'exec', label: 'Executing Agency', field: 'exec', sortable: true},
        {name: 'cost', label: 'Cost', field: 'cost', sortable: true},
        {name: 'start_date', label: 'Start Date', field: 'start_date'},
        {name: 'actions', label: 'Actions', field: 'actions', sortable: true}
      ],
      rows: null,
    }
  },
  mounted(){
    api.get('projects').then((response)=>{
      this.rows = response.data.data
    })
  },
}
</script>
<style lang="sass">
.my-sticky-header-table

  .q-table__top,
  thead tr:first-child th
    /* bg color is important for th; just specify one */
    background-color: #B3CDF5

</style>
