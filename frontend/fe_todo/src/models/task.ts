import { ListData } from './list';

export type TaskData = {
    id: number,
    list: ListData,
    list_id: number,
    title: string,
    description: string,
}