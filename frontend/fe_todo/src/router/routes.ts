import useAccountRoutes from './account';
import useTaskRoutes from './task';
import useListRoutes from './list';
import { RouteRecordRaw } from 'vue-router';
// import testPartTwoRoutes from './testPartTwo';

const routes: RouteRecordRaw[] = [
  {
    path: '',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'Home', component: () => import('pages/HomePage.vue') },
    ],
  },
  {
    path: '/account/',
    component: () => import('layouts/AccountLayout.vue'),
    children: useAccountRoutes(),
  },
  {
    path: '/list/',
    component: () => import('layouts/MainLayout.vue'),
      children: useListRoutes(),
  },
  {
    path: '/tasklist/:listId/',
    name:'tasks',
    component: () => import('layouts/MainLayout.vue'),
      children: useTaskRoutes(),
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
