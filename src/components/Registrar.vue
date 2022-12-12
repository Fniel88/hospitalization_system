<template>
    <div class="registrar_paciente">
        <div class="container_registrar_paciente">
            <form v-on:submit.prevent="proccessPacienteRe">
                <label id="paciente_direccion">
                    <input type="text" v-model="paciente.direccion" placeholder="Direccion de Residencia" required>
                </label>
                <label id="paciente_ciudad">
                    <input type="text" v-model="paciente.ciudad" placeholder="Ciudad de Residencia" required>
                </label>
                <label id="paciente_fecha_nacimiento"> 
                    <input type="date" v-model="paciente.fecha_nacimiento" placeholder="AAAA/MM/DD" required>
                </label>
                <label id="paciente_IDPersonal"> 
                    <input type="text" v-model="paciente.id_PSalud" placeholder="Personal encargado" required>
                </label>
                <label id="user_Nombres">
                    <input type="text" v-model="paciente.id_UserName" placeholder="ID Usuario" required>
                </label>
                <button type="submit">Registrar Paciente</button> 
            </form>    
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default { 
    data:function(){
        return{
            paciente:{
                direccion: "",
                ciudad: "",
                fecha_nacimiento: "",
                id_PSalud: "",
                id_UserName: ""   
            }
        }
    },

    methods: {
        proccessPacienteRe: function(){
            axios.post("http://127.0.0.1:8000/paciente/", this.paciente, {headers: {}})
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
.registrar_paciente{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_registrar_paciente {
    border: 3px solid #26ad80;
    border-radius: 5px;
    width: 20%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.registrar_paciente h2
{
    color: #69b99a;
}
.registrar_paciente form
{
    width: 50%;
}
.registrar_paciente input
{
height: 40px;
width: 110%;
box-sizing: border-box;
padding: 5px 5px;
margin: 5px 0;
border: 1px solid #234d3b;
}
.registrar_paciente button
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
.registrar_paciente button:hover
{
color: #E5E7E9;
background: rgba(197, 185, 21, 0.63);
border: 1px solid #283747;
}
</style>