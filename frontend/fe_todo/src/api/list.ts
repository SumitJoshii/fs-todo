import { api } from 'src/boot/axios';
import { useApiHelper } from 'src/utils/api';
import { ListData } from 'src/models/list';

export default () => {
    const apihelper = useApiHelper({
        api: api,
        baseUrl: '/api/',
    });
    return {
        list: (id:string) =>
            apihelper.get(`lists/user/${id}/`) as Promise<ListData[]>,
        addList: (data: ListData) =>
            apihelper.post('lists/', data),
        editList: (data: ListData) =>
            apihelper.put(`lists/${data.id}/`,data),
        deleteList: (id:string) =>
            apihelper.delete(`lists/${id}/`),
    };
}