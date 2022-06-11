<template>
    <div class="ranking">
        <div class="container_rank">
            <table>
                <tr>
                    <td><strong>Usuario</strong></td>
                    <td><strong>Puntaje</strong></td>
                </tr>
                <tr v-for="usuario in usuarios" :key="usuario.id">
                    <td>{{ usuario.nickname }}</td>
                    <td>{{ usuario.puntaje_Total }}</td>
                </tr>
            </table>
            <div>
                <button v-on:click="loadLogIn">
                    <strong>Regresar</strong>
                </button>
            </div>
        </div>

    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: "Ranking",

    data: function () {
        return {
            usuarios: [
            ],
        }
    },

    methods: {
        loadLogIn: function () {
            this.$router.push({ name: "logIn" });
        },

        getRankingList: function () {
            axios.get(`https://simpquiz-be.herokuapp.com/participante/all/`,
                { headers: {} })
                .then((result) => {
                    this.usuarios = result.data;
                    this.OrderPuntajesTotales();
                })
                .catch((error) => {

                })
        },

        OrderPuntajesTotales: function () {
            let newA = [];
            for (let i = 0; i < this.usuarios.length; i++) {
                if (this.usuarios[i].puntaje_Total === 0) {
                    continue;
                }
                newA.push(this.usuarios[i]);
            }
            this.usuarios = newA;
            this.usuarios.sort(function (a, b) {
                return b.puntaje_Total - a.puntaje_Total;
            }).then((result) => {
                this.usuarios = result.data;
                console.log(this.usuarios)
            })
                .catch((error) => {
                })
        },

    },
    created: async function () {
        this.getRankingList();
        
    }
}

</script>

<style>
.ranking {
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container_rank {
    border: 3px solid #2e89eb;
    border-radius: 10px;
    width: 25%;
    height: 60%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.ranking button {
  width: 100%;
  height: 40px;
  color: #e5e7e9;
  background: #2e89eb;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.ranking button:hover {
  color: #e5e7e9;
  background: crimson;
  border: 1px solid #283747;
}
</style>