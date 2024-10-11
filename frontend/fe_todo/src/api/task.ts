import { api } from 'src/boot/axios';
import { useApiHelper } from 'src/utils/api';
import { TaskData } from 'src/models/task';
// import { ListData } from 'src/models/list';

export default () => {
    const apihelper = useApiHelper({
        api: api,
        baseUrl: '/api/',
    });
    return {
        task: (id: string) =>
            apihelper.get(`tasks/list/${id}/`) as Promise<TaskData[]>,
        addTask: (data: TaskData) =>
            apihelper.post('tasks/', data),
        editTask: (data: TaskData) =>
            apihelper.put(`tasks/${data.id}/`,data),
        deleteTask: (id:string) =>
            apihelper.delete(`tasks/${id}/`),
    };
}