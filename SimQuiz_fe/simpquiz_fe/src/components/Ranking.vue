<template>
    <div class="ranking">
        <div v-if="loaded" class="container_rank">
            <h1> <strong>Top 10</strong></h1>

            <table>
                <tr>
                    <th><strong>Posición</strong></th>
                    <th><strong>Usuario</strong></th>
                    <th><strong>Puntaje</strong></th>
                </tr>

                <tr v-for="(usuario, index) in usuarios" :key="usuario.id">
                    <td v-if="index < 10">{{ index + 1 }}</td>
                    <td v-if="index < 10">{{ usuario.nickname }}</td>
                    <td v-if="index < 10">{{ usuario.puntaje_Total }}</td>
                </tr>
            </table>


            <div class="container_button">
                <button v-on:click="loadMainPage">
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
            loaded: false,
        }
    },

    methods: {
        loadMainPage: function () {
            this.$emit("loadLogIn");
        },

        getRankingList: function () {
            axios.get(`https://simpquiz-be.herokuapp.com/participante/all/`,
                { headers: {} })
                .then((result) => {
                    this.usuarios = result.data;
                    this.loaded = true;
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
            }).then(
                console.log(this.usuarios)

            )
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
    margin: 0 0 0 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container_rank {
    border: 3px solid #0f0f10;
    border-radius: 10px;
    display: flex;
    height: 40%;
    width: 30%;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: 'Simpson';
    font-size: 30px;
}

.container_rank h1 {
    display: flex;
    font-family: 'Simpson';
    font-size: 60px;
    color: #0f0f10;
    box-sizing: border-box;
    display: flex;
}

.container_rank table {
    margin: 5px 2px 2px 5px;
    height: 50%;
    width: 70%;
    box-sizing: border-box;
}

.container_rank tr:nth-child(even) {
    background-color: #3d7a8a;
}

.container_rank tr:nth-child(odd) {
    background-color: #5ab4ca;
}

.container_rank td:nth-child(2) {
    text-align: center;
}

.container_rank td:nth-child(3) {
    text-align: right;
}

.ranking button {
    height: 40px;
    color: #0f0f10;
    background: #db5293;
    border: 1px solid #0f0f10;
    font-family: 'Simpson';
    font-size: 30px;
}

.container_button {
    display: flex;
    justify-content: center;
    align-items: center;
}

.ranking button:hover {
    color: #156d8e;
    background: #ecc54d;
    border: 1px solid #156d8e;
}
</style>