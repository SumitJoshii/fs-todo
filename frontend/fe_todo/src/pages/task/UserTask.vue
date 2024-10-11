<template>
  <q-page style="min-height: calc(100vh-200px) !important">
    <!-- If No Tasks! -->
    <div v-if="task.length === 0">
      <div class="absolute-center">
        <i
          class="fa-solid fa-square-check"
          style="display: inline-block; font-size: 30px"
        ></i>
        <p
          class="q-mb-xs q-mt-md q-ml-sm text-h4"
          style="display: inline-block"
        >
          No pending tasks~!
        </p>
      </div>
    </div>

    <div v-else class="q-pa-md">
      <q-list bordered separator class="task-style">
        <q-item
          v-for="item in task"
          :key="item.title"
          clickable
          v-ripple
          router-link
        >
          <q-checkbox
            class="q-mr-lg"
            v-model="item.is_complete"
            @click="status(item)"
          />
          <!-- :style="item.is_complete ? 'green' : 'red'" -->

          <q-item-section
            :class="{
              'checked-class': item.is_complete,
              'unchecked-class': !item.is_complete,
            }"
            @click="showDetailsForm(item)"
            >{{ item.title }}</q-item-section
          >
          <q-item-section>
            <div style="text-align: right">
              <q-btn
                class="q-mr-md button-style"
                color="primary"
                icon="edit"
                @click="showEditForm(item)"
              />
              <!-- :color="editColor" -->
              <q-btn
                class="q-mr-md button-style"
                color="negative"
                icon="delete"
                @click="deletePrompt(item)"
              />
            </div>
          </q-item-section>
        </q-item>
      </q-list>
    </div>
    <div class="add-button q-pa-md q-gutter-sm">
      <q-btn round color="primary" icon="add" @click="showAddForm" />
    </div>

    <q-dialog v-model="showAddModal">
      <q-card>
        <p class="q-pa-md q-mb-xs text-center">Add new Task.</p>
        <hr />
        <q-card-section>
          <q-input v-model="newtask.title" label="Task Name" maxlength="50" />
        </q-card-section>
        <q-card-section>
          <q-input
            v-model="newtask.description"
            label="Task Description"
            maxlength="100"
          />
        </q-card-section>
        <q-card-section>
          <q-btn label="Add" @click="addTask()" />
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="showEditModal">
      <q-card>
        <p class="q-pa-md q-mb-xs text-center">Edit Task.</p>
        <hr />
        <q-card-section>
          <q-input
            v-model="selectedTask.title"
            label="Task Name"
            maxlength="50"
          />
        </q-card-section>
        <q-card-section>
          <q-input
            v-model="selectedTask.description"
            label="Description"
            maxlength="100"
          />
        </q-card-section>
        <q-card-section>
          <q-btn label="Update" @click="editTask()" />
        </q-card-section>
      </q-card>
    </q-dialog>
    <q-dialog v-model="showDeleteModal">
      <q-card style="width: 200px">
        <p class="text-center q-mt-md">Really Delete?</p>
        <hr />

        <q-card-section class="align-center">
          <q-btn
            class="q-mb-sm q-pa-sm"
            label="Yes"
            style="width: 100%; color: red"
            @click="
              deleteTask(delTask);
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
    <q-dialog v-model="showDetailsModal">
      <q-card style="width: 250px">
        <p class="q-pa-md q-mb-xs text-center">Task Details.</p>
        <hr />
        <q-card-section>
          <q-field label="Task Name" stack-label>{{
            selectedTask.title
          }}</q-field>
        </q-card-section>
        <q-card-section>
          <q-field label="Task Description" stack-label>{{
            selectedTask.description
          }}</q-field>
        </q-card-section>
        <q-card-section>
          <q-btn label="Ok" @click="closeDetailsForm()" />
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>
<script setup>
import { useQuasar } from 'quasar';
import { onMounted, ref } from 'vue';
import useTaskApi from 'src/api/task';
import { useRoute } from 'vue-router';

const $q = useQuasar();
const taskapi = useTaskApi();
const task = ref([]);
const showAddModal = ref(false);
const showEditModal = ref(false);
const showDetailsModal = ref(false);
const showDeleteModal = ref(false);
const delTask = ref();
// const editColor = $q.dark.isActive ? 'green' : 'primary';

const route = useRoute();
const listId = route.params.listId;
console.log(route);

const selectedTask = ref();

const newtask = ref({
  list_id: listId,
  title: '',
  description: '',
  is_complete: false,
});

onMounted(async () => {
  const response = await taskapi.task(listId);
  task.value = response;
  console.log(task.value);
});

const showAddForm = async () => {
  showAddModal.value = true;
};

const showEditForm = async (data) => {
  showEditModal.value = true;
  selectedTask.value = data;
};

const addTask = async () => {
  const response = await taskapi.addTask(newtask.value);

  if (response.errors) {
    showAddModal.value = false;
    return;
  }
  showAddModal.value = false;
  task.value.push(response);
  newtask.value.title = '';
  newtask.value.description = '';

  showNotifAdd();
};

const editTask = async () => {
  await taskapi.editTask(selectedTask.value);
  showEditModal.value = false;
  showNotifEdit();
};

const showDetailsForm = async (item) => {
  showDetailsModal.value = true;
  selectedTask.value = item;
};

const closeDetailsForm = async () => {
  showDetailsModal.value = false;
};

const deletePrompt = async (data) => {
  showDeleteModal.value = true;
  delTask.value = data;
};

const deleteTask = async (delTask) => {
  await taskapi.deleteTask(delTask.id);
  console.log('Item Deleted!');
  task.value = task.value.filter((item) => item.id != delTask.id);
  showDeleteModal.value = false;
};

const closeCard = () => {
  showDeleteModal.value = false;
};

const status = async (item) => {
  await taskapi.editTask(item);
};

const showNotifAdd = async () => {
  $q.notify({
    message: 'Task Added Successfully.',
    color: 'green',
  });
};

const showNotifEdit = async () => {
  $q.notify({
    message: 'Task Edited Successfully.',
    color: 'blue',
  });
};

const showNotifDelete = async () => {
  $q.notify({
    message: 'Task Deleted Successfully.',
    color: 'red',
  });
};

// const taskCompleteStyle = (item) => ({
//   backgroundColor: item.is_complete ? 'green' : 'red',
// });
</script>
<style scoped>
.add-button {
  /* border: 2px blue dashed; */
  position: absolute;
  right: 0px;
  bottom: 10px;
  /* judaad */
}

.checked-class {
  text-decoration: line-through;
  color: rgb(220, 3, 3);
}
/* .unchecked-class {
  color: black;
} */

.task-style {
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
  border-radius: 20px;
  width: 35px;
  height: 35px;
}
</style>
