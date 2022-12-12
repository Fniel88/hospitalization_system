<template>
    <div class="registrar_personal">
        <div class="container_registrar_personal">
            <form v-on:submit.prevent="proccessPersonalRe">
                <label id="personal_rol">
                    <input type="text" v-model="personal.rol" placeholder="Rol que desempeña" required>
                </label>
                <label id="personal_especialidad">
                    <input type="text" v-model="personal.especialidad" placeholder="Especialidad" required>
                </label>
                <label id="personal_id_username"> 
                    <input type="text" v-model="personal.id_UserName" placeholder="ID Usuario" required>
                </label>
                <button type="submit">Registrar Personal</button> 
            </form>    
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default { 
    data:function(){
        return{
            personal:{
                rol: "",
                especialidad: "",
                id_UserName: ""   
            }
        }
    },

    methods: {
        proccessPersonalRe: function(){
            axios.post("http://127.0.0.1:8000/personal/", this.personal, {headers: {}})
            .then((result)=>{
                console.log(result.status)
                alert("Registro Exitoso")
                location.reload()
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
.registrar_personal{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_registrar_personal {
    border: 3px solid #26ad80;
    border-radius: 5px;
    width: 20%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.registrar_personal h2
{
    color: #69b99a;
}
.registrar_personal form
{
    width: 50%;
}
.registrar_personal input
{
height: 40px;
width: 110%;
box-sizing: border-box;
padding: 5px 5px;
margin: 5px 0;
border: 1px solid #234d3b;
}
.registrar_personal button
{
width: 100%;
height: 50px;
color: #E5E7E9;
background: #30696d;
border: 1px solid #E5E7E9;
border-radius: 5px;
padding: 10px 25px;
margin: 5px 0 25px 0;
font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;

}
.registrar_personal button:hover
{
color: #E5E7E9;
background: rgba(197, 185, 21, 0.63);
border: 1px solid #283747;
}
</style>