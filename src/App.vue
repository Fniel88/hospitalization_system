<template>
  <div id="app" class="app">

    <div class="header">

      <h1>Hospitalizacion en casa</h1>
      <nav>
        <button v-if="is_auth" v-on:click="loadRegistrar">Paciente</button>
        <button v-if="is_auth" v-on:click="loadPersonal">Personal de Salud</button>
        <button v-if="is_auth" v-on:click="loadFamiliar">Familiar</button>
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
        <button v-if="is_auth" v-on:click="loadLook">Consultar</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>
  
    <div class="main-component">
      <router-view
      v-on:completedLogIn="completedLogIn"
      v-on:completedSignUp="completedSignUp"
      v-on:logOut = "logOut"
      >
      </router-view>
    </div>
  
    <div class="footer">
      <h2>Lo mejor para tu salud</h2>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'App',

  data: function(){
      return{
        is_auth: false
      } 
  },

  components: {
  },
  methods:{
    veryAuth: function(){
      this.is_auth= localStorage.getItem("isAuth") || false;
      if(this.is_auth== false)
        this.$router.push({name:"logIn"});
      else
        this.$router.push({name:"home"});
    },
  loadLogIn: function(){
    this.$router.push({name:"logIn"})
  },
  loadSignUp: function(){
    this.$router.push({name:"signUp"})
  },

  completedLogIn: function(data){
      localStorage.setItem("isAuth",true);
      localStorage.setItem("username",data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autentificación exitosa");
      this.veryAuth();
  },
  completedSignUp: function(data) {
    alert("Registro Exitoso");
    this.completedLogIn(data);
    this.$router.push({name:"home"});
  },
  loadHome: function() {
    this.$router.push({name:"home"});
  },

  logOut: function() {
    localStorage.clear();
    alert("Sesion Cerrada");
    this.veryAuth();
  },
  loadLook: function() {
    this.$router.push({name:"look"});
  },
  loadRegistrar: function() {
    this.$router.push({name:"registrar"});
  },
  loadPersonal: function() {
    this.$router.push({name:"personal"});
  },
  loadFamiliar: function() {
    this.$router.push({name:"familiar"});
  }
  },
  created: function(){
    this.veryAuth()
  }

}
</script>
<style>

body{
  margin: 0 0 0 0;
  height: 500px;
  background-image: url("https://clinic-cloud.com/wp-content/uploads/2015/05/medicina-preventiva.jpg");
  background-repeat:no-repeat;
  background-position-x:center;
  background-position-y: center;
  background-size: 2000px;
}

.header{
  margin: 0;
  padding: 0;
  width:100%;
  height: 10vh;
  min-height: 100px;
  background-color: #26ad80;
  color: #E5E7E9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1{
  width: 50%;
  text-align: center;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.header nav button
{
  color: #E5E7E9;
  background: #30696d;
  border: 5px solid #103a0349;
  border-radius: 5px;
  padding: 10px 30px;
  font-family: sans-serif;
}

.header nav button:hover
{
  color: #283747;
  background: #E5E7E9;
  border: 1px solid #E5E7E9;
}

.main-component
{
  height: 65vh;
  margin: 0%;
  padding: 0%;
  background: #fefdfda8;
}

.footer
{
  margin:0;
  padding:0;
  width: 100%;
  height: 5vh;
  min-height: 100px;
  background-color: #26ad80;
  color: #E5E7E9;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.footer h2{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>