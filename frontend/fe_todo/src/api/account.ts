import { api } from 'src/boot/axios';
import { useApiHelper } from 'src/utils/api';
import { User, LoginData, TokenResponse } from 'src/models/account';

export default () => {
  const apihelper = useApiHelper({
    api: api,
    baseUrl: '/api/',
  });

  return {
    login: (data: LoginData) =>
      apihelper.post('login_user/', data) as Promise<TokenResponse>,
    getUser: (id: string) =>
      apihelper.get(`users/${id}`),
    addUser: (data : User) =>
      apihelper.post('users/', data)
  };
};
