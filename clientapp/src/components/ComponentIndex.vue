<template>
  <div v-if="rows">
    <div class="q-pa-md">
      <q-table
        class="my-sticky-header-table"
        title="⚒ Components"
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
                 v-if="getUser.role.code !== 'EXEC'"
                 @click="$router.push('/govt/projects/add')"/>
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td key="budget_ratio" :props="props">
              {{ props.row.budget_ratio }}
            </q-td>
            <q-td key="component_type" :props="props">
              {{ props.row.component_type }}
            </q-td>
            <q-td key="est_completion_date" :props="props">
              {{ props.row.est_completion_date }}
            </q-td>
            <q-td key="est_start_date" :props="props">
              {{ props.row.est_start_date }}
            </q-td>
            <q-td key="start_date" :props="props">
              {{ props.row.start_date }}
            </q-td>
            <q-td key="actions" :props="props" style="align-items: end" v-if="getUser.role.code !== 'EXEC'">
              <q-btn style="margin-left: 10px;" text-color="white" color="brown-5" label="Update"
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
import {mapGetters} from "vuex";

export default {
  name: 'ComponentIndex',
  props: {
    project_name: {
      type: String,
      required: true
    },
    project_id: {
      type: String,
      default: ''
    },

  },
  computed: {
    ...mapGetters("auth", ["getUser"]),
  },
  data() {
    return {
      filter: ref(''),
      columns: [
        {
          name: 'budget_ratio', required: true, label: 'Budget Ratio', align: 'left', field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        {name: 'component_type', align: 'center', label: 'Component type', field: 'component_type', sortable: true},
        {name: 'est_completion_date', label: 'Estimated completion date', field: 'est_completion_date', sortable: true},
        {name: 'est_start_date', label: 'Estimated Start Date', field: 'est_start_date', sortable: true},
        {name: 'actions', label: 'Actions', field: 'actions', sortable: true}
      ],
      rows: null,
    }
  },
  mounted(){
    api.get(`projects/${this.project_id}/components`).then((response)=>{
      console.log(response)
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
