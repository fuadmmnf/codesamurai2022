export default {
  namespaced: true,
  state: {
    user: localStorage.getItem('user')
      ? JSON.parse(localStorage.getItem('user'))
      : null,
    agencies: localStorage.getItem('agencies')
      ? JSON.parse(localStorage.getItem('agencies'))
      : null,
  },

  getters: {
    getUser: (state) => state.user,
    getAgencies: (state) => state.agencies,
    isAuthenticated (state) {
      return !! state.user
    }
  },

  mutations: {
    SET_USER (state, payload) {
      let user = payload
      state.user = user
      localStorage.setItem('user', JSON.stringify(state.user))
    },
    SET_AGENCIES (state, payload){
      let agencies = payload
      state.agencies = agencies
      localStorage.setItem('agencies', JSON.stringify(state.user))
    },
    RESET_USER (state) {
      state.user = null
      localStorage.removeItem('user')
    },
    init (state) {
      state.user = localStorage.getItem('user')
        ? JSON.parse(localStorage.getItem('user'))
        : null;
    }
  },

  actions: {
  },

}
