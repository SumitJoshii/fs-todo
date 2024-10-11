import { RouteRecordRaw } from 'vue-router';

export default (): RouteRecordRaw[] => [
  // {
  //   path: '',
  //   redirect: { name: 'TaskList' },
  // },
  {
    path: '',
    name: 'TaskList',
    component: () => import('pages/task/UserTask.vue'),
    // props: route => ({ listId: route.params.listId }),
  },
];