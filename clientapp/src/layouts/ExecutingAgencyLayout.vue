<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-cyan-6 text-black">
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
          Executing Agency
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
      </q-list>
      <div align="center" style="margin-top: 15px;">
        <q-btn
          color="primary"
          label="Logout"
          @click="onLogout"
        />
      </div>
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
    caption: 'Executing agency dashboard',
    icon: '🏣',
    link: '/#/exec'
  },
  {
    title: 'Projects',
    caption: 'List of all projects',
    icon: '⚒',
    link: '/#/exec/projects'
  },
  {
    title: 'Proposals (DPPs)',
    caption: 'List of all proposals',
    icon: '📁',
    link: '/#/exec/proposals'
  },
  {
    title: 'Add Proposals (DPPs)',
    caption: 'Add new project',
    icon: '➕',
    link: '/#/exec/proposals/add'
  },
]

export default {
  name: 'ExecutingLayout',
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
    if(this.getUser.role.code !== 'EXEC'){
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
