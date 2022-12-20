
const routes = [
  {
    name: 'login',
    path: '/login',
    component: () => import('layouts/login.vue'),
  },
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
    ]
  },
  {
    path: '/govt',
    component: () => import('layouts/GovtLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Govt/index.vue') },
      { path: 'projects', component: () => import('pages/Govt/Projects/index.vue') },
      { path: 'Proposals', component: () => import('pages/Govt/Proposals/index.vue') },
      { path: 'projects/add', component: () => import('pages/Govt/Projects/AddProjects.vue') },
      { path: 'projects/detail', component: () => import('pages/Govt/Projects/details.vue') },
    ]
  },
  {
    path: '/exec',
    component: () => import('layouts/ExecutingAgencyLayout.vue'),
  }
  // Always leave this as last one,
  // but you can also remove it
  // {
  //   path: '*',
  //   component: () => import('pages/Error404.vue')
  // }
]

export default routes
