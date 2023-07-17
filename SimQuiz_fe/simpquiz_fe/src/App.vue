<template>
  <div class="container-sm">
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
        <h2><strong>Desarrollado por: Diego Sánchez </strong>
          <a href="https://github.com/Difsan" target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" class="bi bi-github"
              viewBox="0 0 16 16">
              <path
                d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z" />
            </svg>
          </a>
          <a href="https://www.linkedin.com/in/difru/" target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="black" class="bi bi-linkedin"
              viewBox="0 0 16 16">
              <path
                d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z" />
            </svg>
          </a>

        </h2>

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

.footer h2 a {
  margin: 0 8px;
  display: flex;
}
</style>
