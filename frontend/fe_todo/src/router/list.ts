import { RouteRecordRaw } from 'vue-router';

export default (): RouteRecordRaw[] => [
  {
    path: 'lists/',
    redirect: { name: 'list/UserList' },
  },
  {
    path: 'user-list',
    name: 'list/UserList',
    component: () => import('pages/list/UserList.vue'),
  },
];
