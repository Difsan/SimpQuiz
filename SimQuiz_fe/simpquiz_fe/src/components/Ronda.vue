<template>
  <div class="rondas">
    <div class="container_rondas">
      <h1>
        <span> {{ pregunta.pregunta }} </span>
      </h1>
      <div v-for="rta in respuestas" :key="rta.id" class="container_button">
        <button v-on:click="loadNextRonda(rta.correcta)" type="submit">{{ rta.respuesta }}</button>
      </div>
      <button v-on:click="ProcesslogOut()" type="submit">Salir</button>

    </div>

  </div>

</template>

<script>
import axios from 'axios';
export default {
  name: "Ronda",

  data: function () {
    return {
      respuestas: [],
      rtaCorrecta: {},
      // se usa para crear una participacion
      participacionIn: {
        // por defecto tiene que ser 1
        ronda: 1,
        participanteId: localStorage.getItem("userId"),
        preguntaId: 1,
        puntaje_Ronda: 0
      },

      participante: {
        nickname: localStorage.getItem("user_nickname"),
        puntaje_Total: parseInt(localStorage.getItem("puntaje_Total"))
      },

      // info que ssale al crear una participacion
      partiOut: {
        id: 0,
        ronda: 0,
        puntaje_Ronda: 0,
      },
      preguntas: [],
      pregunta: {
        id: 0,
        pregunta: "",
        level: {
          id: 0,
          nivel: 0,
          puntaje: 0
        }
      }
    };
  },

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;
      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "ronda" });
    },

    getPreguntasXCatergoria: async function () {
      axios.get(
        `https://simpquiz-be.herokuapp.com/preguntas/filter/${this.participacionIn.ronda}/`,
        {
          headers: {},
        })
        .then((result) => {
          this.preguntas = result.data;
          let rand = Math.floor(Math.random() * this.preguntas.length);
          let rValue = this.preguntas[rand];

          this.pregunta = rValue;

          this.participacionIn.preguntaId = this.pregunta.id;

          if (this.participacionIn.ronda === 1) {
            this.CrearParticipacion();
          }
          else {
            this.UpdateParticipacion();
          }

        })
        .catch((error) => {
          console.log(error);
        });
    },

    CrearParticipacion: function () {
      axios.post(
        "https://simpquiz-be.herokuapp.com/participacion/",
        this.participacionIn,
        {
          headers: {},
        }).then((result) => {
          console.log("Participacion creada con exito");
          this.partiOut.id = result.data.id;
          this.partiOut.ronda = result.data.ronda;
          this.partiOut.puntaje_Ronda = result.data.puntaje_Ronda;
          this.getRtasXpregunta();
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getRtasXpregunta: function () {
      axios.get(
        `https://simpquiz-be.herokuapp.com/respuestas/filter/${this.participacionIn.preguntaId}/`,
        {
          headers: {},
        }).then((result) => {
          this.respuestas = result.data;
          for (let i = 0; i < this.respuestas.length; i++) {
            if (this.respuestas[i].correcta) {
              this.rtaCorrecta = this.respuestas[i];
            }
          }
          console.log("RTA correcta" + this.rtaCorrecta);
        }
        ).catch((error) => {
          console.log(error);
        });
    },

    loadNextRonda: function (correcta) {
      if (correcta) {

        alert("Respesta correcta");
        this.participacionIn.puntaje_Ronda += this.pregunta.level.puntaje;

        this.participacionIn.ronda++;
        if (this.participacionIn.ronda < 6) {
          this.getPreguntasXCatergoria();
        } else {
          alert("felicitaciones terminaste el juego con: " + this.participacionIn.puntaje_Ronda + "Puntos");
          this.UpdateParticipacion();
          //this.logOut();
        }
      }
      else {
        alert("Respuesta incorrecta, " + localStorage.getItem("user_nickname") + ", perdiste");
        if (this.participacionIn.puntaje_Ronda === 0) this.DeleteParticipacion();
        this.logOut();
      }
    },


    UpdateParticipacion: function () {

      if (this.participacionIn.ronda > 5) this.participacionIn.ronda = 5;
      axios.put(`https://simpquiz-be.herokuapp.com/participacion/update/${this.partiOut.id}/`,
        this.participacionIn,
        { headers: {} })
        .then((result) => {
          console.log("Participacion Actualizada");
          if (this.participacionIn.puntaje_Ronda === 15000) this.ActualizarPuntajeTotal();

          this.getRtasXpregunta();

        })
        .catch((error) => {

        })
    },

    ActualizarPuntajeTotal: function () {
      this.participante.puntaje_Total += this.participacionIn.puntaje_Ronda;
      axios.put(`https://simpquiz-be.herokuapp.com/participante/update/${localStorage.getItem("userId")}/`,
        this.participante,
        { headers: {} })
        .then((result) => {
          console.log("Puntaje total Actualizado");

          this.logOut();
        })
        .catch((error) => {

        })
    },

    ProcesslogOut: function () {

      if (this.participacionIn.puntaje_Ronda != 0) this.ActualizarPuntajeTotal();
      this.logOut();
    },

    logOut: function () {
      localStorage.clear();
      console.log("Sesion Cerrada");
      this.verifyAuth();
    },

    DeleteParticipacion: function () {
      axios.delete(`https://simpquiz-be.herokuapp.com/participacion/remove/${this.partiOut.id}/`,
        { headers: {} })
        .then((result) => {
          console.log("Participacion borrada exitosamente");

        })
        .catch((error) => {

        })

    },


  },

  created: async function () {
    this.getPreguntasXCatergoria();
    this.getRtasXpregunta();
    this.verifyAuth();
  }
};
</script>

<style>
.rondas {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_rondas {
  border: 3px solid #2e89eb;
  border-radius: 10px;
  width: 25%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.rondas h1 {
  font-size: 50px;
  color: #283747;
}

.rondas span {
  color: rgb(0, 0, 0);
  font-weight: bold;
}

.rondas container_button {
  display: flex;
  flex-direction: column;
  float: left;
}

.rondas button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #2e89eb;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.rondas button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>