import { defineStore } from 'pinia';
import useListApi from 'src/api/list';
import { ListResponse } from 'src/models/list';
import { ref } from 'vue';

export default defineStore('list', () => {
    const listApi = useListApi();
    // const lists: ListResponse[] = []; //Ref in vue
    const lists = ref<ListResponse[]>([]);

    const userList = async () => {
        // const data = {
        //     listName: listName,
        // };
        const id = localStorage.getItem('id');
        if (!id) {
            return;
        }
        const response = await listApi.list(id);
        lists.value = response;
        console.log('Retrieval Successful!');
    };

    return{
        lists,//Variable
        userList,//Action
    };
})