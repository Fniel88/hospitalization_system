<template>
    <div class="logIn_user">
        <div class="container_logIn_user">
            <h2>Iniciar Sesión</h2>

            <form v-on:submit.prevent="processLogInUser" >
                <input type="text" v-model="user.username" placeholder="Username">
                <br>
                <input type="password" v-model="user.password" placeholder="Password">
                <br>
                <button type="submit">Iniciar Sesion</button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    
    export default {
        name: "LogIn",
    
        data: function(){
            return {
                user: {
                    username:"",
                    password:""
                }
            }
        },
    
        methods: {
            processLogInUser: function(){
                axios.post(
                    "http://127.0.0.1:8000/login/",
                    this.user,
                    {headers: {}}
                )
                    .then((result) => {
                        let dataLogIn = {
                            username: this.user.username,
                            token_access: result.data.access,
                            token_refresh: result.data.refresh,
                        }
        
                        this.$emit('completedLogIn', dataLogIn)
        
                    })
                    .catch((error) => {
                        if (error.response.status == "401")
                            alert("ERROR 401: Credenciales Incorrectas.");
                    });
            }
        }
    }
</script>

<style>
.logIn_user{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.container_logIn_user {
    border: 2px solid #26ad80;
    border-radius: 10px;
    width: 30%;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.logIn_user h2{
    color: #56ac1c;
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}

.logIn_user form{
    width: 70%;
}
.logIn_user input{
    height: 20px;
    width: 100%;
    box-sizing: border-box;
    padding: 20px 30px;
    margin: 5px 0;
    border: 1px solid #234d3b;
}
.logIn_user button{
    width: 100%;
    height: 40px;
    color: #E5E7E9;
    background: #30696d;
    border: 1px solid #E5E7E9;
    border-radius: 5px;
    padding: 10px 25px;
    margin: 5px 0;
}
.logIn_user button:hover{
    color: #E5E7E9;
    background: rgba(197, 185, 21, 0.63);
    border: 1px solid #283747;
}
</style>