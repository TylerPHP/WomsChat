<template>
  <div>
    <h1>Чат на vue js</h1>
    <button v-if="!auth" @click="goLogin">Вход</button>
    <div v-if="auth">
      <button @click="logout" :title="title">Выход</button>
      <Room/>
    </div>
  </div>
</template>

<script>
  import Room from '@/components/Room'

  export default {
    name: "Home",
    data() {
      return {
        title: 'Удалить токен для входа'
      }
    },
    components: {
      Room
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
      }
    },
  }
</script>

<style scoped>

</style>
