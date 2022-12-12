<template>
    <div class="signUp_user">
        <div class="container_signUp_user">
            <form v-on:submit.prevent="proccessSignUp">
                <label id="user_Username">
                    <input type="text" v-model="user.username" placeholder="Username" required>
                </label>
                <label id="user_Passowrd">
                    <input type="text" v-model="user.password" placeholder="Contraseña" required>
                </label>
                <label id="user_Perfil"> 
                    <input type="text" v-model="user.perfil" placeholder="Perfil" required>
                </label>
                <label id="user_Nombres">
                    <input type="text" v-model="user.nombre" placeholder="Nombres" required>
                </label>
                <label id="user_Apellidos">
                    <input type="text" v-model="user.apellidos" placeholder="Apellidos" required>
                </label>
                <label id="user_telefono">
                    <input type="text" v-model="user.telefono" placeholder="Telefono" required>
                </label>
                <label id="user_Genero">
                    <input type="text" v-model="user.genero" placeholder="Genero" required>
                </label>
                <button type="submit">Registrarse</button>
            </form>    
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default { 
    data:function(){
        return{
            user:{
                username: "",
                password: "",
                perfil: "",
                nombre: "",
                apellidos:"",
                telefono:"",
                genero:""  
            }
        }
    },

    methods: {
        proccessSignUp: function(){
            axios.post("http://127.0.0.1:8000/user/",
                this.user,
                {headers: {}}
            )
                .then((result) => {
                    let dataSignUp = {
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh,
                    }
                    this.$emit('completedSignUp', dataSignUp)
                })
                .catch((error) => {
                    console.log(error)
                    alert("ERROR: Fallo en el registro.");
                });
        }    
    }
}
</script>

<style>
.signUp_user{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_signUp_user {

    border: 3px solid #26ad80;
    border-radius: 5px;
    width: 20%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.signUp_user h2
{
    color: #69b99a;
}
.signUp_user form
{
    width: 50%;
}
.signUp_user input
{
height: 20px;
width: 100%;
box-sizing: border-box;
padding: 10px 20px;
margin: 5px 0;
border: 1px solid #234d3b;
}
.signUp_user button
{
width: 100%;
height: 40px;
color: #E5E7E9;
background: #30696d;
border: 1px solid #E5E7E9;
border-radius: 5px;
padding: 10px 25px;
margin: 5px 0 25px 0;
font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;

}
.signUp_user button:hover
{
color: #E5E7E9;
background: rgba(197, 185, 21, 0.63);
border: 1px solid #283747;
}
</style>