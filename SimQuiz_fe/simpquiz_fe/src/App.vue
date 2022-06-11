<template>
  <div id="app" class="app">
    <div class="header">
      <h1>SimpQuiz</h1>
      <nav>
        <button v-if="!is_auth" v-on:click="loadRanking">Ranking Puntos</button>
        
      </nav>
    </div>

    <div class="main-component">
      <router-view
       v-on:completedLogIn="completedLogIn"
       v-on:logOut="logOut"
      ></router-view>
    </div>

    <div class="footer">
      <h2>Desarrollado por: Diego Sanchez</h2>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function(){
    return{
      is_auth: false
    }

  },

  components:{},
  methods:{
    
    verifyAuth: function(){
      this.is_auth = localStorage.getItem("isAuth") || false;
      if(this.is_auth ==  false)
       this.$router.push({name: "logIn"});
       else
       this.$router.push({name: "ronda"});
    },

    loadLogIn: function(){
      this.$router.push({name: "logIn"});
    },

    loadRanking: function(){
      this.$router.push({name: "ranking"});
    },

    completedLogIn: function(data){
      localStorage.setItem("isAuth", true);
      localStorage.setItem("userId", data.id);
      localStorage.setItem("user_nickname", data.nickname);
      localStorage.setItem("puntaje_Total", data.puntaje_Total);
      console.log("Autenticacion Exitosa");
      this.verifyAuth();
    },

    logOut: function(){
      localStorage.clear();
      console.log("Sesion Cerrada");
      this.verifyAuth();
    }
  },

  created: function(){
    this.verifyAuth()
  }
}
</script>


<style>
body{
  margin: 0 0 0 0;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  /*del total vertical solo acuper el 10%*/
  height: 10vh;
  /*como minimo 100 pixeles de altura*/
  min-height: 100px;

  background-color: #2e89eb;
  color: #e5e7e9;

  /*acomode al reajuste de la pantalla*/
  display: flex;
  /*contenido justificado con espacio igual entre los elementos*/
  justify-content: space-between;
  align-items: center;
}
.header h1 {
  width: 20%;
  text-align: center;
}
.header nav {
  height: 100%;
  width: 20%;
  display: flex;
  /*Todoslos espacios iguales, incluso los de espacio desde borde navegador */
  justify-content: space-around;
  /*centrar items en vertical*/
  align-items: center;
  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: #2e89eb;
  border: 1px solid #e5e7e9;
  /*redondear las esquinas */
  border-radius: 5px;
   /*Espacio entre botones*/
  padding: 10px 20px;
}
.header nav button:hover {
  color: #283747;
  background: crimson;
  border: 1px solid #283747;
}
.main-component {
  /*vh= 1% de lo que mide la pagina verticalmente, alrtura */
  /*vw= 1% de lo que mide la pagina horizontal, ancho */
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #fdfefe;
}

.footer {
  margin: 0;
  padding: 0;
  /*del componente padre como aqui el apdre tiene el 75%, pues es el
  100% de ese 75 */
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #2e89eb;
  color: #e5e7e9;
}
.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
