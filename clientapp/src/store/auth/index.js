export default {
  namespaced: true,
  state: {
    user: localStorage.getItem('user')
      ? JSON.parse(localStorage.getItem('user'))
      : null,
  },

  getters: {
    getUser: (state) => state.user,
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
