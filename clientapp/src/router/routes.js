
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
      { path: '/client/projects', component: () => import('pages/ClientProjects.vue') },
      { path: '/client/proposals/detail', component: () => import('pages/ClientProjectDetails.vue') },
    ]
  },
  {
    path: '/govt',
    component: () => import('layouts/GovtLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Govt/index.vue') },
      { path: 'projects', component: () => import('pages/Govt/Projects/index.vue') },
      { path: 'projects/add', component: () => import('pages/Govt/Projects/AddProjects.vue') },
      { path: 'projects/detail', component: () => import('pages/Govt/Projects/Detail.vue') },
      { path: 'projects/update', component: () => import('pages/Govt/Projects/Update.vue') },
      { path: 'Proposals', component: () => import('pages/Govt/Proposals/index.vue') },
      { path: 'Proposals/detail', component: () => import('pages/Govt/Proposals/Detail.vue') },
    ]
  },
  {
    path: '/exec',
    component: () => import('layouts/ExecutingAgencyLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ExecutingAgenices/index.vue') },
      { path: 'projects', component: () => import('pages/ExecutingAgenices/projects/index.vue') },
      { path: 'projects/detail', component: () => import('pages/ExecutingAgenices/projects/Detail.vue') },
      { path: 'proposals', component: () => import('pages/ExecutingAgenices/proposals/index.vue') },
      { path: 'proposals/detail', component: () => import('pages/ExecutingAgenices/proposals/Detail.vue') },
      { path: 'proposals/add', component: () => import('pages/ExecutingAgenices/proposals/AddProposal.vue') },
      { path: 'proposals/update', component: () => import('pages/ExecutingAgenices/proposals/UpdateProposal.vue') },
    ]
  }
  // Always leave this as last one,
  // but you can also remove it
  // {
  //   path: '*',
  //   component: () => import('pages/Error404.vue')
  // }
]

export default routes
