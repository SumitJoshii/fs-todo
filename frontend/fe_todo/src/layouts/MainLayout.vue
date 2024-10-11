<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> ToDo List </q-toolbar-title>

        <q-toggle
          v-model="modeSwitch"
          checked-icon="star"
          color="purple"
          unchecked-icon="cloud"
          @click="themeStatus"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <div class="q-pa-md">
        <q-avatar class="q-pa-xs" style="display: inline-block">
          <img src="https://cdn.quasar.dev/img/avatar.png" />
        </q-avatar>
        <p style="display: inline-block; margin: 15px 0px 0px 30px">
          {{ user?.username }}
          <!-- Wew, use '?' -->
        </p>
        <hr class="q-mt-md" />
      </div>

      <q-list>
        <q-item-label class="q-pa-md"> Related Links </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
        <q-item>
          <q-item-section>
            <q-item-label></q-item-label>
            <q-item-label caption>App Ver. 1.0</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useQuasar } from 'quasar';
import accountApi from 'app/src/api/account';
import EssentialLink, {
  EssentialLinkProps,
} from 'components/EssentialLink.vue';

const $q = useQuasar();
const status = ref(false);
const userApi = accountApi();

const themeStatus = async () => {
  status.value = !status.value;
  $q.dark.set(status.value);
};

defineOptions({
  name: 'MainLayout',
});

const modeSwitch = ref(false);
const user = ref();

onMounted(async () => {
  const uid = localStorage.getItem('id');
  if (!uid) return;
  const response = await userApi.getUser(uid);
  user.value = response;
  console.log(user.value);
});

const linksList: EssentialLinkProps[] = [
  {
    title: 'Github',
    caption: 'github.com/SumitJoshii',
    icon: 'code',
    link: 'https://github.com/SumitJoshii',
  },
  {
    title: 'Developer',
    caption: 'Connect with the Dev Team',
    icon: 'web',
    link: '',
  },
];

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
