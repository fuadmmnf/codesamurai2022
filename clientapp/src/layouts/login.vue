<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex flex-center">
        <q-card
          class="my-card q-pa-md-sm shadow-15"
          color="white"
          inline
        >
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-0 col-xs-0 flex flex-center ">
              <img
                alt="Samurai Planner"
                height="70%"
                src="~assets/4380.jpg"
                width="100%"
              >
            </div>
            <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12 flex flex-center ">
              <h5 class="text-dark text-center"><b>Samurai Planner Log In</b></h5>
              <div>
                <form @submit.prevent="onLoginSubmit">
                  <div align="center" class="bottomMargin20">
                    <q-field
                      class="q-mt-md"
                      icon="email"
                      icon-color="light"
                    >
                      <q-input
                        v-model="username"
                        placeholder="Enter user name"
                        type="text"
                      >
                        <template v-slot:before>
                          <q-icon name="email"/>
                        </template>
                      </q-input>
                    </q-field>
                    <q-field
                      class="q-mt-md"
                      icon="password"
                      icon-color="light"
                    >
                      <q-input
                        v-model="password"
                        placeholder="Enter password"
                        type="password"
                      >
                        <template v-slot:before>
                          <q-icon name="password"/>
                        </template>
                      </q-input>
                    </q-field>
                  </div>
                  <div align="center" style="margin-bottom: 15px;">
                    <q-btn
                      color="primary"
                      label="Login"
                      type="submit"
                    />
                  </div>
                </form>
<!--                <div class="text-center" style="font-size: 12px; padding: 15px; margin-bottom: 10px;">-->
<!--                  If you don't have an account, Please-->
<!--                  <a class="textColor" @click="$router.push({ path: '/register'})">Sign Up</a>-->
<!--                </div>-->
              </div>
            </div>
          </div>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>

import {mapMutations} from 'vuex'
import {api} from "boot/axios";
export default {
  name: "login",
  components: {
    // vueAwesomeCountdown
  },
  data() {
    return {
      username: '',
      password: '',
    }
  },
  mounted() {
    api.get('agencies').then((response)=>{
      console.log(response.data)
        this.SET_AGENCIES(response.data.data)
    })
  },
  methods: {
    ...mapMutations('auth', ['SET_USER','SET_AGENCIES']),
    async onLoginSubmit() {
      let temp = {
        username: this.username,
        password: this.password
      }
      api.post('login',temp).then((response)=>{
        this.SET_USER(response.data.data)
        this.$router.push('/')
      })
    },
  },
}
</script>


<style scoped>
.my-card {
  width: 100%;
  max-width: 700px;
}
.leftMargin35 {
  margin-left: 35px;
}
.bottomMargin20 {
  margin-bottom: 20px;
}
.textColor {
  color: #9C27B0;
}
h5{
  margin-top: 30px;
  margin-bottom: 2px;
}
</style>
