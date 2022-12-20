import Vue from 'vue'
import axios from 'axios'

// We create our own axios instance and set a custom base URL.
// Note that if we wouldn't set any config here we do not need
// a named export, as we could just `import axios from 'axios'`
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/'
})

// for use inside Vue files through this.$axios and this.$api
Vue.prototype.$axios = axios
Vue.prototype.$api   = api

// Here we define a named export
// that we can later use inside .js files:
export { axios, api }
