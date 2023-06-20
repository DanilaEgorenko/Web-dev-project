<template>
    <div>
        <ul class='chat-list'>
            <router-link v-for='chat in chats' v-bind:key='chat.id' :to='"/chat/" + chat.id'>Chat with user {{ chat.user }}</router-link>
        </ul>
        <form class='form'>
            <label class='form__label' for="email_to">Почта получателя</label>
            <input class='form__input' type="email" name="user" id="email_to" v-model='email_to' placeholder='emaxple@mail.ru' required>
            <label class='form__label' for="text">Текст сообщения</label>
            <input class='form__input' type="text" name="text" id="text" v-model='text' placeholder='Ваше сообщение' required>
            <input class='form__submit' type="button" @click='startChat()' value='Начать чат'>
            <p v-if='form_error' style='color: red'>{{ form_error }}</p>
        </form>
        
    </div>
</template>

<script>
import Cookies from 'js-cookie';

export default {
    
    name: 'chat-page',
    data() {
        return {
            chats: [],
            email_to: '',
            text: '',
            email: localStorage.getItem('email'),
            form_error: '',
            chatId: '',
        }
    },
    mounted() {
        const url = this.$api + "chats/";
        fetch(url, {
            headers: {
                "Authorization": "Bearer " + Cookies.get('jwt'),
            }
        })
        .then(
            res => {
                return res.json();
            }
        )
        .then(
            data => {
                this.chats = data;
            }
        )
    },
    methods: {
        startChat() {
            const url = this.$api + "chats/";
            fetch(url, {
                method: 'POST',
                headers: {
                    "Authorization": "Bearer " + Cookies.get('jwt'),
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    'email': this.email_to,
                    'text': this.text
                })
            })
            .then(
                res => {
                    return res.json();
                }
            )
            .then(
                data => {
                    if (data.success) {
                        this.$router.push('/chat/' + data.chat_id);
                    }
                    else {
                        this.form_error = data.error;
                    }
                }
            )
        }
    }
}

</script>

<style lang="scss" scoped>
@import '@/assets/scss/variables';

.form {
    display: flex;
    flex-direction: column;
    width: 400px;
    margin-left: auto;
    margin-right: auto;
    gap: 10px;

    &__input, &__submit {
        height: 30px;
    }

    &__submit {
        background-color: $light-pink;
        border: 1px solid $pink;
    }

    &__submit:active {
        background-color: $pink;
    }
}

.chat-list {
    border: solid 1px $pink;
    padding: 10px;
    width: fit-content;
    margin: 50px auto 50px auto;
}
</style>