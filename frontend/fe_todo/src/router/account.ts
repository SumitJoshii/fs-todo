import { RouteRecordRaw } from 'vue-router';

export default (): RouteRecordRaw[] => [
  {
    path: '',
    redirect: { name: 'account/LoginUser' },
  },
  {
    path: 'login',
    name: 'account/LoginUser',
    component: () => import('pages/account/LoginUser.vue'),
  },
];
