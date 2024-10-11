<template>
  <q-page>
    <div class="text-h4 q-mb-xs q-pa-md">
      Making a to-do list can <br />
      have many benefits, including:
    </div>

    <div>
      <ul>
        <div>
          <i class="fa-solid fa-square-check" style="display: inline-block"></i>
          <p class="q-mb-xs q-mt-md q-ml-sm" style="display: inline-block">
            Planning
          </p>
        </div>
        <li class="q-ml-lg">
          To-do lists help you plan your day by keeping track of important tasks
          and setting realistic goals.
        </li>

        <div>
          <i class="fa-solid fa-square-check" style="display: inline-block"></i>
          <p class="q-mb-xs q-mt-md q-ml-sm" style="display: inline-block">
            Organization
          </p>
        </div>
        <li class="q-ml-lg">
          To-do lists help you stay organized and efficient by providing a clear
          outline of your tasks and helping you avoid multitasking.
        </li>

        <div>
          <i class="fa-solid fa-square-check" style="display: inline-block"></i>
          <p class="q-mb-xs q-mt-md q-ml-sm" style="display: inline-block">
            Prioritizing
          </p>
        </div>
        <li class="q-ml-lg">
          To-do lists help you keep your priorities in order and reduce your
          workload by dividing tasks into smaller steps and focusing on the most
          important ones.
        </li>
      </ul>
    </div>
    <div style="text-align: center">
      <q-btn class="q-pa-sm q-mr-sm" color="primary" @click="showGuestForm"
        >Make a List!</q-btn
      >
      <q-btn
        class="q-pa-sm q-mr-sm"
        color="green"
        :to="{ name: 'account/LoginUser' }"
        >Login.</q-btn
      >
    </div>
    <q-dialog v-model="showGuestModal">
      <q-card>
        <p class="q-pa-md q-mb-xs text-center">Guest User Login.</p>
        <hr />
        <q-card-section>
          <q-input v-model="guestUser.username" label="User Name" />
        </q-card-section>
        <q-card-section>
          <q-btn label="Continue" @click="addGuestUser(guestUser)" />
          <!-- :to="{ name: 'list/UserList' }" -->
        </q-card-section>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import useAccountStore from 'src/stores/account';

import userHelperApi from '/src/api/account';

const accountStore = useAccountStore();
const router = useRouter();
const guestUser = ref({
  username: '',
  password: 'test@123',
  email: 'deleteuser@tonight.com',
});
const showGuestModal = ref(false);

const userApi = userHelperApi();

const showGuestForm = async () => {
  showGuestModal.value = true;
};
const addGuestUser = async () => {
  const response = await userApi.addUser(guestUser.value);
  console.log(response);

  try {
    await accountStore.loginUser(
      guestUser.value.username,
      guestUser.value.password
    );
    router.push({ name: 'list/UserList' });
  } catch (error) {
    console.error(error);
  }
};
</script>

<style></style>
