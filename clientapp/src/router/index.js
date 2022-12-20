import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'

Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default function ( { store, ssrContext }) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ x: 0, y: 0 }),
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })
  store.commit('auth/init')

  Router.beforeEach((to, from, next) => {
    // const currentUser = AUTH.currentUser
    const currentUser = store.state.auth.user
    console.log(currentUser)
    if (currentUser === null && to.name !=='login') {
      next('/login')
    } else if(currentUser !== null && to.name ==='login') {
      console.log('here')
      if(currentUser.role.code === 'APP'){
        next('/')
      } else if(currentUser.role.code === 'EXEC'){
        next('/exec')
      } else {
        next('/govt')
      }
    }
    else {
      next()
    }
  })
  return Router
}
