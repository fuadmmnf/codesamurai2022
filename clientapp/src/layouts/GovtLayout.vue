<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Govt Agency
        </q-toolbar-title>

        <div>IIT Heckers</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Samurai Planners
        </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
        <div align="center" style="margin-top: 15px;">
          <q-btn
            color="primary"
            label="Logout"
            @click="onLogout"
          />
        </div>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'
import {mapGetters, mapMutations} from "vuex";

const linksData = [
  {
    title: 'Dashboard',
    caption: 'Govt agency dashboard',
    icon: '🏣',
    link: '/#/govt'
  },
  {
    title: 'Projects',
    caption: 'List of all projects',
    icon: '⚒',
    link: '/#/govt/projects'
  },
  {
    title: 'Proposals (DPPs)',
    caption: 'List of all proposals',
    icon: '📁',
    link: '/#/govt/proposals'
  },
  {
    title: 'Add Project',
    caption: 'Add new project',
    icon: '➕',
    link: '/#/govt/projects/add'
  },
]

export default {
  name: 'GovtLayout',
  components: {
    EssentialLink
  },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  },
  computed: {
    ...mapGetters("auth", ["getUser"]),
  },
  mounted() {
    if(this.getUser.role.code === 'APP' || this.getUser.role.code === 'EXEC'){
      this.$router.push('/login');
    }
  },
  methods:{
    ...mapMutations('auth', ['RESET_USER']),
    onLogout(){
      this.RESET_USER()
      this.$router.push('/login')
    }
  }
}
</script>
