<template>
  <main>
    <form class="signin" action="" v-if="!username">
      <h2>Войти в аккаунт</h2>
      <div class="signin__choices">
        <div class="signin__choice">
          <input type="radio" id="contactChoice1" name="signin" v-model='signInMethod' value="phone" checked>
          <label for="contactChoice1">Через телефон</label>
        </div>
        <div class="signin__choice">
          <input type="radio" id="contactChoice2" name="signin" v-model='signInMethod' value="email">
          <label for="contactChoice2">Через email</label>
        </div>
      </div>
      <div class="signin__form">
        <input v-if='signInMethod === "email"' type="email" inputmode="email" placeholder="example@mail.ru">
        <input v-else-if='signInMethod === "phone"' type="phone" inputmode="tel" placeholder="+7 (___) ___ __ __">
        <input type="password" placeholder="Введите пароль">
        <div class="signin__form-checkbox">
          <input type="checkbox" id="remember_me" name="remember_me" checked>
          <label for="remember_me">Запомнить меня</label>
        </div>
      </div>
      <div class="signin__actions">
        <button class="signin__actions-button" type="submit">Войти</button>
        <a href="#" class="signin__actions-forgot">Забыли пароль?</a>
        <a href="#" class="signin__actions-registration">Зарегистрироваться</a>
      </div>
      <a class="login-with-google-btn" href='http://localhost:8000/google-sign-in'>Войти через Google</a>
    </form>
    <div v-else>
      <p>{{ username }}</p>
      <p>{{ email }}</p>
      <input type="button" value='Выйти из аккаунта' @click='logout()'>
    </div>
  </main>
</template>

<script>
import Cookies from 'js-cookie';

export default {
  name: 'signin-page',
  data() {
    return {
      signInMethod: "phone",
      username: localStorage.getItem('username'),
      email: localStorage.getItem('email'),
    }
  },
  methods: {
    logout() {
      Cookies.remove('jwt');
      localStorage.removeItem('username');
      localStorage.removeItem('email');
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
.login-with-google-btn {
    transition: background-color .3s, box-shadow .3s;
    text-decoration: none;
    cursor: pointer;
      
    padding: 12px 16px 12px 42px;
    margin-bottom: 20px;
    border: none;
    border-radius: 3px;
    box-shadow: 0 -1px 0 rgba(0, 0, 0, .04), 0 1px 1px rgba(0, 0, 0, .25);
    
    color: #757575;
    font-size: 14px;
    font-weight: 500;
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen,Ubuntu,Cantarell,"Fira Sans","Droid Sans","Helvetica Neue",sans-serif;
    
    background-image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj48cGF0aCBkPSJNMTcuNiA5LjJsLS4xLTEuOEg5djMuNGg0LjhDMTMuNiAxMiAxMyAxMyAxMiAxMy42djIuMmgzYTguOCA4LjggMCAwIDAgMi42LTYuNnoiIGZpbGw9IiM0Mjg1RjQiIGZpbGwtcnVsZT0ibm9uemVybyIvPjxwYXRoIGQ9Ik05IDE4YzIuNCAwIDQuNS0uOCA2LTIuMmwtMy0yLjJhNS40IDUuNCAwIDAgMS04LTIuOUgxVjEzYTkgOSAwIDAgMCA4IDV6IiBmaWxsPSIjMzRBODUzIiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNNCAxMC43YTUuNCA1LjQgMCAwIDEgMC0zLjRWNUgxYTkgOSAwIDAgMCAwIDhsMy0yLjN6IiBmaWxsPSIjRkJCQzA1IiBmaWxsLXJ1bGU9Im5vbnplcm8iLz48cGF0aCBkPSJNOSAzLjZjMS4zIDAgMi41LjQgMy40IDEuM0wxNSAyLjNBOSA5IDAgMCAwIDEgNWwzIDIuNGE1LjQgNS40IDAgMCAxIDUtMy43eiIgZmlsbD0iI0VBNDMzNSIgZmlsbC1ydWxlPSJub256ZXJvIi8+PHBhdGggZD0iTTAgMGgxOHYxOEgweiIvPjwvZz48L3N2Zz4=);
    background-color: white;
    background-repeat: no-repeat;
    background-position: 12px 11px;
  }
  .login-with-google-btn:hover {
    box-shadow: 0 -1px 0 rgba(0, 0, 0, .04), 0 2px 4px rgba(0, 0, 0, .25);
  }
  
  .login-with-google-btn:active {
    background-color: #eeeeee;
  }
main
{
  display: flex;
  justify-content: center;
}

.signin
{
  display: grid;
  place-content: center;
  justify-items: center;
  box-shadow: 6px 7px 11px rgba(0, 0, 0, 0.25);
  padding: 0 108px;
}

.signin__choices
{
  display: flex;
  gap: 40px;
  margin: 20px 30px 0 30px;
}

.signin__choices input
{
  display: none;
}

.signin__form
{
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
  width: 100%;
}

.signin__form-checkbox
{
  display: flex;
  gap: 20px;
}

.signin__actions
{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 13px;
  margin-top: 20px;
  margin-bottom: 62px;
}

.signin__choices input+label
{
  text-decoration: underline;
  color: black;
}

.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  margin: 0 auto;
  width: 80%;
  max-width: 1200px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

.title {
  font-size: 36px;
  font-weight: bold;
  color: #333;
  text-align: center;
  margin-bottom: 50px;
}

.subtitle {
  font-size: 24px;
  font-weight: bold;
  color: #555;
  margin-bottom: 30px;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 20px;
  font-weight: bold;
  color: white;
  background-color: #f00;
  border: none;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button:hover {
  transform: scale(1.1);
  background-color: #f55;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 50px;
}

.input-label {
  display: inline-block;
  font-size: 18px;
  font-weight: bold;
  color: #777;
  margin-bottom: 10px;
}

.input-text {
  display: block;
  padding: 10px;
  font-size: 16px;
  color: #555;
  border: 2px solid #ddd;
  border-radius: 5px;
  transition: all 0.2s ease-in-out;
}

.input-text:focus {
  outline: none;
  border-color: #f00;
  box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
}

.checkbox-label {
  display: inline-block;
  font-size: 16px;
  font-weight: bold;
  color: #777;
}

.checkbox {
  display: inline-block;
  margin-right: 10px;
  width: 20px;
  height: 20px;
  border: 2px solid #ddd;
  border-radius: 5px;
  transition: all 0.2s ease-in-out;
}

.checkbox:checked {
  background-color: #f00;
  border-color: #f00;
}

.radio-label {
  display: inline-block;
  font-size: 16px;
  font-weight: bold;
  color: #777;
}

.radio-group {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.radio {
  display: inline-block;
  margin-right: 10px;
}
.random-class {
  background: linear-gradient(45deg, red, blue, yellow, green);
  border: 5px dotted purple;
  box-shadow: 10px 10px 20px rgba(0,0,0,0.5);
  transform: rotate(45deg);
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
  font-size: 50px;
  font-weight: bold;
  color: white;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 10px;
  word-spacing: 20px;
  line-height: 1.5;
  text-decoration: underline;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  filter: grayscale(100%) blur(5px);
  cursor: crosshair;
  opacity: 0.5;
  transition: all 1s ease-in-out;
}

.random-class:hover {
  background: linear-gradient(45deg, yellow, green, red, blue);
  border: 5px dotted red;
  box-shadow: 10px 10px 30px rgba(0,0,0,0.7);
  transform: rotate(-45deg);
  text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
  font-size: 60px;
  font-weight: bolder;
  color: black;
  letter-spacing: 20px;
  word-spacing: 30px;
  line-height: 2;
  text-decoration: line-through;
  text-overflow: clip;
  overflow: visible;
  filter: grayscale(50%) blur(2px);
  cursor: pointer;
  opacity: 1;
}
.body {
  background-color: pink;
  background-image: url('https://dummyimage.com/300x300/000/fff');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
  font-family: Arial, sans-serif;
}

.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  margin: 0 auto;
  width: 80%;
  max-width: 1200px;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

.title {
  font-size: 36px;
  font-weight: bold;
  color: #333;
  text-align: center;
  margin-bottom: 50px;
}

.subtitle {
  font-size: 24px;
  font-weight: bold;
  color: #555;
  margin-bottom: 30px;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 20px;
  font-weight: bold;
  color: white;
  background-color: #f00;
  border: none;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.button:hover {
  transform: scale(1.1);
  background-color: #f55;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 50px;
}

.input-label {
  display: inline-block;
  font-size: 18px;
  font-weight: bold;
  color: #777;
  margin-bottom: 10px;
}

.input-text {
  display: block;
  padding: 10px;
  font-size: 16px;
  color: #555;
  border: 2px solid #ddd;
  border-radius: 5px;
  transition: all 0.2s ease-in-out;
}

.input-text:focus {
  outline: none;
  border-color: #f00;
  box-shadow: 0 0 10px rgba(255, 0, 0, 0.3);
}

.checkbox-label {
  display: inline-block;
  font-size: 16px;
  font-weight: bold;
  color: #777;
}

.checkbox {
  display: inline-block;
  margin-right: 10px;
  width: 20px;
  height: 20px;
  border: 2px solid #ddd;
  border-radius: 5px;
  transition: all 0.2s ease-in-out;
}

.checkbox:checked {
  background-color: #f00;
  border-color: #f00;
}

.radio-label {
  display: inline-block;
  font-size: 16px;
  font-weight: bold;
  color: #777;
}

.radio-group {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.radio {
  display: inline-block;
  margin-right: 10px;
}
/* Немного стилей для кнопки */
.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

/* Стили для карточки */
.card {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  padding: 16px;
  margin: 16px;
}

.h1 {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  color: #333;
}

ul {
  list-style-type: none;
}

button
{
  background: #EA7EA0;
  border-radius: 26px;
  padding: 14px 90px;
  border: 0;
  color: white;
}

input
{
  background: #EBEBEB;
  border: 0;
  padding: 11px 0;
  padding-left: 32px;
}

.signin__choices input:checked+label
{
  color: grey;
  text-decoration: none;
}

.signin__choices input:not(:checked)+label:hover
{
  cursor: pointer;
}
</style>