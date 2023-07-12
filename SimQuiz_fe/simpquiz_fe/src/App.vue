<template>
  <div class="container-sm" >
    <div :style="image" id="app" class="app">

      <div class="navbar navbar-expand-lg">
        <h1><strong>SimpQuiz</strong></h1>
        <nav>
          <button v-if="!is_auth" v-on:click="loadRanking"><strong>Ranking Puntos</strong></button>
        </nav>
      </div>

      <div class="main-component">

        <router-view v-on:loadLogIn="loadLogIn" v-on:completedLogIn="completedLogIn" v-on:logOut="logOut">
        </router-view>
      </div>

      <div class="footer">
        <h2><strong>Desarrollado por: Diego Sánchez</strong></h2>
      </div>
    </div>
    </div>
  

</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      is_auth: false,
      image: { backgroundImage: "url(https://wallpaperaccess.com/full/535125.jpg)" }
    }

  },

  components: {},
  methods: {

    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "ronda" });
    },

    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },

    loadRanking: function () {
      this.$router.push({ name: "ranking" });
    },

    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("userId", data.id);
      localStorage.setItem("user_nickname", data.nickname);
      localStorage.setItem("puntaje_Total", data.puntaje_Total);
      console.log("Autenticacion Exitosa");
      this.verifyAuth();
    },

    logOut: function () {
      localStorage.clear();
      console.log("Sesion Cerrada");
      this.verifyAuth();
    }
  },

  created: function () {
    this.verifyAuth(),
      this.image
  }
}
</script>


<style>
@font-face {
  font-family: 'Simpson';
  src: url(./assets/Simpsonfont.ttf) format('truetype');
  font-style: normal;
  font-weight: 100;
}

body {
  margin: 0 0 0 0;

}

.app {
  width: 100%;
  height: 100%;
  /*style to the background image */
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}

.navbar {
  margin: 0%;
  padding: 0;
  width: 100%;
  /*del total vertical solo acupar el 10%*/
  height: 10vh;
  /*como minimo 100 pixeles de altura*/
  min-height: 100px;
  color: #0f0f10;
  /*acomode al reajuste de la pantalla*/
  display: flex;
  /*contenido justificado con espacio igual entre los elementos*/
  justify-content: space-between;
  align-items: center;
}

.navbar h1 {
  font-family: 'Simpson';
  width: 10%;
  text-align: center;
  display: flex;
  font-size: 120px;

}

.navbar nav {
  height: 100%;
  width: 100%;
  display: flex;
  /*Todoslos espacios iguales, incluso los de espacio desde borde navegador */
  justify-content: right;
  
  /*centrar items en vertical*/
  align-items: center;
}

.navbar nav button {
  color: #0f0f10;
  font-size: 40px;
  background: #40a6bb;
  border: 1px solid #0f0f10;
  /*redondear las esquinas */
  border-radius: 80px;
  /*Espacio entre botones*/
  padding: 10px 20px;
  display: flex;
  font-family: 'Simpson';
}

.navbar nav button:hover {
  color: #156d8e;
  background: #ecc54d;
  border: 1px solid #156d8e;
}

.main-component {
  /*vh= 1% de lo que mide la pagina verticalmente, altura */
  /*vw= 1% de lo que mide la pagina horizontal, ancho */
  height: 80vh;
  margin: 0%;
  padding: 0%;
  display: flex;
}

.footer {
  margin: 0 0 0 0;
  padding: 0;
  /*del componente padre como aqui el apdre tiene el 75%, pues es el
  100% de ese 75 */
  width: 100%;
  height: 10vh;
  color: #121b32;
}

.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Simpson';
  font-size: 30px;

}
</style>
