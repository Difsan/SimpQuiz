<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Entrar</h2>
      <!--se agrega el escucha para que llame la funcion-->
      <form v-on:submit.prevent="verifyUser">
        <input type="text" v-model="user.nickname" placeholder="nickname" />
        <br />
        <!--submit para que al dar click envie la info del formulario-->
        <button type="submit">Jugar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogIn",

  data: function () {
    return {
      user: {
        nickname: "",
        puntaje_Total: 0
      },
    };
  },

  methods: {
    processLogInUser: function () {
      axios.post(
        "https://simpquiz-be.herokuapp.com/participante/",
        this.user, {
        headers: {},
      })
        .then((result) => {
          let dataLogIn = {
            id: result.data.id,
            nickname: this.user.nickname,
            puntaje_Total: result.data.puntaje_Total
          }

          this.$emit('completedLogIn', dataLogIn)
        })
        .catch((error) => {
          console.log(error);
        });
    },

    verifyUser: function () {
      axios.get(
        `https://simpquiz-be.herokuapp.com/participante/filter/${this.user.nickname}/`,
        {
          headers: {},
        })
        .then((result) => {
          let arrayR = result.data;
          if (arrayR.length === 0) {
            console.log("Usuario no existe");
            this.processLogInUser();
          }
          else if (arrayR.length === 1) {
            console.log("Usuario existente");
            let dataLogIn = {
              id: arrayR[0].id,
              nickname: this.user.nickname,
              puntaje_Total: arrayR[0].puntaje_Total
            }
            console.log(dataLogIn);
            this.$emit('completedLogIn', dataLogIn)
          }
        })
    },
  }
}
</script>

<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_logIn_user {
  border: 3px solid #2e89eb;
  border-radius: 10px;
  width: 25%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logIn_user h2 {
  color: #283747;
}

.logIn_user form {
  width: 70%;
}

.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #2e89eb;
}

.logIn_user button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #2e89eb;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
}

.logIn_user button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>