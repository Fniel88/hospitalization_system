<template>
    <div class="registrar_familiar">
        <div class="container_registrar_familiar">
            <form v-on:submit.prevent="proccessFamiliarRe">
                <label id="familiar_parentesco">
                    <input type="text" v-model="familiar.parentesco" placeholder="Parentesco al paciente" required>
                </label>
                <label id="familiar_correo">
                    <input type="text" v-model="familiar.correo" placeholder="Correo Electronico" required>
                </label>
                <label id="familiar_id_paciente"> 
                    <input type="text" v-model="familiar.id_Paciente" placeholder="ID Paciente" required>
                </label>
                <label id="familiar_id_username"> 
                    <input type="text" v-model="familiar.id_UserName" placeholder="ID Usuario" required>
                </label>
                <button type="submit">Registrar Familiar</button> 
            </form>    
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default { 
    data:function(){
        return{
            familiar:{
                parentesco: "",
                corroe: "",
                id_PSalud: "",
                id_UserName: ""   
            }
        }
    },

    methods: {
        proccessFamiliarRe: function(){
            axios.post("http://127.0.0.1:8000/familiar/", this.familiar, {headers: {}})
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
.registrar_familiar{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_registrar_familiar {
    border: 3px solid #26ad80;
    border-radius: 5px;
    width: 20%;
    height: 85%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.registrar_familiar h2
{
    color: #69b99a;
}
.registrar_familiar form
{
    width: 50%;
}
.registrar_familiar input
{
height: 40px;
width: 110%;
box-sizing: border-box;
padding: 5px 5px;
margin: 5px 0;
border: 1px solid #234d3b;
}
.registrar_familiar button
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
.registrar_familiar button:hover
{
color: #E5E7E9;
background: rgba(197, 185, 21, 0.63);
border: 1px solid #283747;
}
</style>