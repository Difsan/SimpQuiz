<template>
    <div class="logIn_user">
      <div class="container_logIn_user">
        <h2><strong>Entrar</strong></h2>
        <!--se agrega el escucha para que llame la funcion-->
        <form v-on:submit.prevent="verifyUser">
          <input type="text" v-model="user.nickname" placeholder="nickname" />
          <br />
          <!--submit para que al dar click envie la info del formulario-->
          <button type="submit"><strong>Jugar</strong></button>
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
  margin: 0 0 0 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_logIn_user {
  border: 3px solid #0f0f10;
  border-radius: 10px;
  display: flex;
  height: 40%;
  width: 25%;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logIn_user h2 {
  font-family: 'Simpson';
  font-size: 70px;
  color: #0f0f10;
  box-sizing: border-box;
  display: flex;

}

.logIn_user form {
  width: 90%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logIn_user input {
  height: 40px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;
  border: 1px solid #0f0f10;
  border-radius: 10px;
  display: flex;
  font-family: 'Simpson';
  font-size: 30px;
  text-align: center;
}

.logIn_user button {
  width: 100%;
  height: 40px;
  color: #0f0f10;
  background: #db5293;
  border: 1px solid #0f0f10;
  border-radius: 10px;
  margin: 5px 0;
  align-items: center;
  font-family: 'Simpson';
  font-size: 30px;
}

.logIn_user button:hover {
  color: #156d8e;
  background: #ecc54d;
  border: 1px solid #156d8e;
}
</style>