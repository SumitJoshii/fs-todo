<template>
  <q-page style="min-height: calc(100vh-200px) !important">
    <div v-if="list.length === 0">
      <div class="absolute-center">
        <i
          class="fa-solid fa-square-check"
          style="display: inline-block; font-size: 30px"
        ></i>
        <p
          class="q-mb-xs q-mt-md q-ml-sm text-h4"
          style="display: inline-block"
        >
          Create List~!
        </p>
      </div>
    </div>
    <div v-else class="q-pa-md">
      <q-list bordered separator class="list-style">
        <q-item
          v-for="item in list"
          :key="item.title"
          v-ripple
          :to="{ name: 'TaskList', params: { listId: item.id } }"
        >
          <!-- @click="redirectTaskPage(item)" -->
          <!-- '../tasklist/tasks/' -->
          <div class="q-mr-lg">
            <q-checkbox
              v-model="item.is_important"
              checked-icon="star"
              unchecked-icon="star_border"
              indeterminate-icon="star_border"
              @click="importantList(item)"
            />
          </div>
          <q-item-section>{{ item.list_name }}</q-item-section>
          <q-item-section>
            <div style="text-align: right">
              <q-btn
                class="q-mr-md button-style"
                color="primary"
                icon="edit"
                @click.prevent="showEditForm(item)"
              />
              <q-btn
                class="q-mr-md button-style"
                color="negative"
                icon="delete"
                @click.prevent="deletePrompt(item)"
              />
            </div>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
    <div class="add-button q-pa-md q-gutter-sm">
      <q-btn round color="primary" icon="add" @click="showAddForm" />
    </div>
    <q-dialog v-model="showEditModal">
      <q-card>
        <p class="q-pa-md q-mb-xs text-center">Edit List.</p>
        <hr />
        <q-card-section>
          <q-input v-model="selectedList.list_name" label="List Name" />
        </q-card-section>
        <q-card-section>
          <q-btn
            label="Update"
            @click="
              editList();
              showNotifEdit();
            "
          />
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="showAddModal">
      <q-card>
        <p class="q-pa-md q-mb-xs text-center">Add new List.</p>
        <hr />
        <q-card-section>
          <q-input v-model="newList.list_name" label="List Name" />
        </q-card-section>
        <q-card-section>
          <q-btn
            label="Add"
            @click="
              addList();
              showNotifAdd();
            "
          />
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="showDeleteModal">
      <q-card style="width: 200px">
        <p class="text-center q-mt-lg">Really Delete?</p>
        <hr />

        <q-card-section class="align-center">
          <q-btn
            class="q-mb-sm q-pa-sm"
            label="Yes"
            style="width: 100%; color: red"
            @click="
              deleteList(delList);
              showNotifDelete();
            "
          />
          <q-btn
            class="q-pa-sm"
            label="No"
            style="width: 100%; color: green"
            @click="closeCard"
          />
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import useListApi from 'src/api/list';
import { useQuasar } from 'quasar';
// import { useRouter } from 'vue-router';
// import { store } from 'quasar/wrappers';

// const router = useRouter();
const $q = useQuasar();
// $q.dark.set(true);

const listApi = useListApi();

const list = ref([]);
const showEditModal = ref(false);
const showAddModal = ref(false);
const showDeleteModal = ref(false);
const selectedList = ref();
const newList = ref({
  user_id: localStorage.getItem('id'), //!!!!!!!!!!!
  list_name: '',
  is_important: false,
});
const delList = ref();

onMounted(async () => {
  const id = localStorage.getItem('id');
  const response = await listApi.list(id);
  list.value = response;
  console.log(response);
});

// const redirectTaskPage = (item) => {
//   console.log('Kya aapke toothpaste me namak hai?');
//   router.push({ name: 'tasks', params: { listId: item.id } });
// };

const showEditForm = async (data) => {
  showEditModal.value = true;
  selectedList.value = data;
};

const showAddForm = async () => {
  showAddModal.value = true;
};

const editList = async () => {
  await listApi.editList(selectedList.value);
  showEditModal.value = false;
};

const addList = async () => {
  const response = await listApi.addList(newList.value);
  if (response.errors) {
    showAddModal.value = false;
    return;
  }
  showAddModal.value = false;
  list.value.push(response);
  newList.value.list_name = '';
};

const deletePrompt = async (data) => {
  showDeleteModal.value = true;
  delList.value = data;
};

const deleteList = async (data) => {
  await listApi.deleteList(data.id);
  list.value = list.value.filter((item) => item.id !== data.id); //To make dynamic USE FILTER
  showDeleteModal.value = false;
};

const showNotifAdd = async () => {
  $q.notify({
    message: 'List Added Successfully.',
    color: 'green',
  });
};

const showNotifEdit = async () => {
  $q.notify({
    message: 'List Edited Successfully.',
    color: 'blue',
  });
};

const showNotifDelete = async () => {
  $q.notify({
    message: 'List Deleted Successfully.',
    color: 'red',
  });
};

const closeCard = () => {
  showDeleteModal.value = false;
};

const importantList = async (item) => {
  await listApi.editList(item);
};
</script>

<style scoped>
.add-button {
  /* border: 2px blue dashed; */
  position: absolute;
  right: 0px;
  bottom: 10px;
  /* judaad */
}
.list-style {
  max-height: 515px;
  height: fit-content;
  width: 50%;
  min-width: 350px;
  overflow-y: auto;
  margin: 0 auto;
  border-radius: 15px;
  border-width: 5px;
}

.button-style {
  display: inline-block;
  border-radius: 15px;
  width: 15px !important;
  height: 15px !important;
}
</style>
