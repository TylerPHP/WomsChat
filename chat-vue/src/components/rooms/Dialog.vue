<template>
  <div>
    <div class="dialog" v-for="dialog in dialogs">
      <h3>{{ dialog.user.username }}</h3>
      <p>{{ dialog.text }}</p>
      <span>{{ dialog.date }}</span>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'

  export default {
    name: "Dialog",
    props: ["id"],
    data() {
      return {
        dialogs: '',
      }
    },
    created() {
      console.log(sessionStorage.getItem('auth_token'))
      $.ajaxSetup({
        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
      })
      this.loadDialog()
    },
    methods: {
      loadDialog() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/chat/dialog/",
          type: "GET",
          data: {
            room: this.id
          },
          success: (response) => {
            this.dialogs = response.data.data
          }
        })
      }
    }
  }
</script>

<style scoped>
  .dialog {
    width: 70%;
    height: 100px;
  }
</style>
