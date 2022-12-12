<template>
    <div class="look_user">
        <div class="container_look_user">
        <form v-if="loaded1" v-on:submit.prevent="processLookUser">
            <h2>Consultar</h2>
            <label id="user_username">
                   <input type="text" v-model="user.username" placeholder="ID Usuario" required> 
            </label>
            <br>
            <button type="submit"> CONSULTAR </button>  
        </form>
        <div v-if="loaded" class="information">
        <h3>Información de usuario</h3>
        <h5> Username: <span>{{username}}</span></h5>
        <h5> Perfil: <span>{{perfil}}</span></h5>
        <h5> Nombres: <span>{{nombre}}</span></h5>
        <h5> Apellidos : <span>{{apellidos}}</span></h5>
        <h5> Telefono : <span>{{telefono}}</span></h5>
        <h5> Genero : <span>{{genero}}</span></h5>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data:function(){
            return{
                loaded1:true,
                user:{
                    username:""
                },
                loaded: false,
                username: "",
                perfil: "",
                nombre:"",
                apellidos:"",
                telefono:"",
                genero:""
            }
    },

    methods: {
            processLookUser: function(){
                axios.get(`http://127.0.0.1:8000/usuarioconsulta/${this.user.username}/`,{headers: {}})
                .then((result) => {
                    this.username = result.data.username;
                    this.perfil =  result.data.perfil;
                    this.nombre = result.data.nombre;
                    this.apellidos = result.data.apellidos;
                    this.telefono = result.data.telefono;
                    this.genero = result.data.genero;
                    this.loaded = true;
                    this.loaded1 = false;
                    }).catch((error) => {
                        if(error.response.status == "404")
                            alert("ERROR 404: No se pudo encontrar");
                    });
                    }
            }   
}
</script>

<style>
    .look_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .container_look_user {
        border: 2px solid #26ad80;
        border-radius: 10px;
        width: 80%;
        height: 60%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .container_look_user h2
    {
        font-family: sans-serif;
        justify-content: center;
        align-items: center;
        color: #26ad80;
        flex-direction: column;
        display: flex;
    }
    .look_user h5{
        color: #56ac1c;
        font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    }
    
    .look_user form{
        width: 80%;
        font-style:inherit;
        font-size: medium;
    }
    .look_user input{
        height: 20px;
        width: 100%;
        box-sizing: border-box;
        padding: 20px 30px;
        margin: 5px 0;
        border: 1px solid #234d3b;
    }
    .look_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #30696d;
        border: 1px solid #E5E7E9;
        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
    }
    .look_user button:hover{
        color: #E5E7E9;
        background: rgba(197, 185, 21, 0.63);
        border: 1px solid #283747;
    }
    .information{
        margin: 0;
        padding: 0%;
        width: 80%;
        height: 80%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }
    .information h3
    {
        color: #2c5779;
    }
    .information h5
    {
        font-size: 20px;
        padding : 30px;
        color: #15db57;
    }
    .information span
    {
        color: rgb(129, 37, 141);
        font-weight: bold;
    }
</style>