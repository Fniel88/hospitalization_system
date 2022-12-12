<template>
    <div class="greetings">
        <form v-on:submit.prevent="processLookUser">
            <h1>¡Bienvenido <span>{{username}} a HEC</span>!</h1>
        </form>
    </div>
</template>

<script>
export default {
    data:function(){
        return{
            username: localStorage.getItem('username') || "none" ,
        }
    }
}
</script>

<style>
.greetings{
    margin: 0;
    padding: 0%;
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
.greetings h1{
    font-size: 50px;
    color: #000000;
}
.greetings span{
    color: rgb(45, 117, 75);
    font-weight: bold;
}
</style>