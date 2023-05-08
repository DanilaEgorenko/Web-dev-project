<template>
  <main>
    <form class="signin" action="">
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
    </form>
  </main>
</template>

<script>
export default {
  name: 'signin-page',
  data() {
    return {
      signInMethod: "phone"
    }
  },
}
</script>

<style scoped>
main {
  display: flex;
  justify-content: center;
}

.signin {
  display: grid;
  place-content: center;
  justify-items: center;
  box-shadow: 6px 7px 11px rgba(0, 0, 0, 0.25);
  padding: 0 108px;
}

.signin__choices {
  display: flex;
  gap: 40px;
  margin: 20px 30px 0 30px;
}

.signin__choices input {
  display: none;
}

.signin__form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 20px;
  width: 100%;
}

.signin__form-checkbox {
  display: flex;
  gap: 20px;
}

.signin__actions {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 13px;
  margin-top: 20px;
  margin-bottom: 62px;
}

.signin__choices input+label {
  text-decoration: underline;
  color: black;
}

button {
  background: #EA7EA0;
  border-radius: 26px;
  padding: 14px 90px;
  border: 0;
  color: white;
}

input {
  background: #EBEBEB;
  border: 0;
  padding: 11px 0;
  padding-left: 32px;
}

.signin__choices input:checked+label {
  color: grey;
  text-decoration: none;
}

.signin__choices input:not(:checked)+label:hover {
  cursor: pointer;
}
</style>