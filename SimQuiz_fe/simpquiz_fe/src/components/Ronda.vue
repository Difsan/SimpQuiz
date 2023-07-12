<template>
  <div class="rondas">
    <div v-if="loaded" class="container_rondas">
      <div class="container_info">
        <div class="nume_pregunta">
          <h4><strong>{{ contador }}/{{ this.maxCategoria }}</strong></h4>
          <p> <strong><small>Pregunta</small></strong></p>
        </div>

        <div class="puntaje_ronda">
          <h4><strong>{{ this.participacionIn.puntaje_Ronda }}</strong></h4>
          <p> <strong><small>Puntos</small></strong></p>
        </div>

      </div>
      <h1>
        <span> {{ pregunta.pregunta }} </span>
      </h1>
      <div v-for="(rta, index) in respuestas" :key="rta.id" class="container_button">
        <button v-on:click="loadNextRonda(rta.correcta)" id="rt" type="submit">
          <h3>{{ index + 1 }}. {{ rta.respuesta }}</h3>
        </button>
      </div>
      <div class="container_outbutton">
        <button class="out_button" v-on:click="ProcesslogOut()" type="submit">Salir</button>
      </div>

    </div>



  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: "Ronda",

  data: function () {
    return {
      contador: 0,
      maxCategoria: 0,
      loaded: false,
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

      // info que sale al crear una participacion
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

    getPreguntasXCatergoria: function () {
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
          this.loaded = false;
          if (this.participacionIn.ronda === 1) {
            this.CrearParticipacion();
            this.contador++;
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
          this.loaded = true;
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

        }
      }
      else {
        alert("Respuesta incorrecta, " + localStorage.getItem("user_nickname") + ", perdiste");
        if (this.participacionIn.puntaje_Ronda === 0) this.DeleteParticipacion();
        this.contador = 0;
        this.$emit("logOut");
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
          this.contador++;
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

          this.$emit("logOut");
        })
        .catch((error) => {

        })
    },

    ProcesslogOut: function () {
      if (this.participacionIn.puntaje_Ronda != 0) this.ActualizarPuntajeTotal();
      else this.DeleteParticipacion();
    },

    DeleteParticipacion: function () {
      axios.delete(`https://simpquiz-be.herokuapp.com/participacion/remove/${this.partiOut.id}/`,
        { headers: {} })
        .then((result) => {
          console.log("Participacion borrada exitosamente");
          this.$emit("logOut");

        })
        .catch((error) => {

        })

    },

    getAllCategories: function () {
      axios.get(
        `https://simpquiz-be.herokuapp.com/categorias/all/`,
        {
          headers: {},
        }).then((result) => {
          result.data.sort(
            function (a, b) {
              return b.nivel - a.nivel;
            }
          )
          this.maxCategoria = result.data[0].nivel;

        }

        ).catch()
    }


  },

  created: function () {
    this.getAllCategories();
    this.getPreguntasXCatergoria();

  }

};
</script>

<style>
.rondas {
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container_rondas {
  border: 3px solid #0f0f10;
  border-radius: 10px;
  width: 20%;

}


.rondas h1 {
  font-family: 'Simpson';
  box-sizing: border-box;
  font-size: 50px;
  color: #0f0f10;
  display: flex;
}

.rondas h3 {
  box-sizing: border-box;
  text-align: left;
  display: flex;
}

.container_button {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
}

.container_rondas button {
  color: #0f0f10;
  background: #db5293;
  border: 1px solid #0f0f10;
  border-radius: 10px;
  margin: 5px 2px 2px 2px;
  font-family: 'Simpson';
  font-size: 30px;
}

.container_outbutton {
  display: flex;
  float: right;
}

.container_outbutton button {
  background: rgb(201, 5, 5);
  justify-content: center;
  align-items: center;
  display: flex;
}

.container_info {
  display: flex;
  justify-content: space-between;
  margin: 0 auto;
  font-family: 'Simpson';
  font-size: 20px;


}




.nume_pregunta {
  width: 40%;
  text-align:left; 
}


.puntaje_ronda {
  width: 30%;
  text-align:right; 
}


.container_rondas button:hover {
  color: #156d8e;
  background: #ecc54d;
  border: 1px solid #156d8e;
}
</style>