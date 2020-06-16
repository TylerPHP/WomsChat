<template>
  <mu-container>
    <mu-appbar style="width: 100%;" color="primary">
      Чат на vue js
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout" :title="title">Выход</mu-button>
    </mu-appbar>
    <mu-row class="margin-down">
      <Room v-if="auth" @openDialog="openDialog"/>
      <Dialog v-if="dialog.show" :id="dialog.id"/>
    </mu-row>
  </mu-container>
</template>

<script>
  import Room from '@/components/rooms/Room'
  import Dialog from '@/components/rooms/Dialog'

  export default {
    name: "Home",
    components: {
      Room,
      Dialog
    },
    data() {
      return {
        title: 'Удалить токен для входа',
        dialog: {
          id: '',
          show: false,
        }
      }
    },
    computed: {
      auth() {
        if (sessionStorage.getItem("auth_token")) {
          return true
        }
      }
    },
    methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        sessionStorage.removeItem("auth_token")
        window.location = '/'
      },
      openDialog(id) {
        this.dialog.id = id
        this.dialog.show = true
      }
    },
  }
</script>

<style scoped>
  .margin-down {
    margin: 55px 15px;
  }
</style>
