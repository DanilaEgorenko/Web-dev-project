<template>
    <div>
        <ul v-if='!chatId'>
            <li v-for='chat_id in chat_ids' v-bind:key='chat_id'>{{ chat_id }}</li>
        </ul>
        <chat-component v-else></chat-component>
        <form class='form' >
            <label class='form__label' for="email_to">Почта получателя</label>
            <input class='form__input' type="email" name="user" id="email_to" v-model='email_to' placeholder='emaxple@mail.ru' required>
            <label class='form__label' for="text">Текст сообщения</label>
            <input class='form__input' type="text" name="text" id="text" v-model='text' placeholder='Ваше сообщение' required>
            <input class='form__submit' type="button" @click='startChat()' value='Начать чат'>
        </form>
        
    </div>
</template>

<script>
import ChatComponent from '@/components/ChatComponent.vue';
import Cookies from 'js-cookie';

export default {
    
    name: 'chat-page',
    data() {
        return {
            chatId: false,
            chat_ids: [],
            email_to: '',
            text: '',
            email: localStorage.getItem('email'),
        }
    },
    components: { ChatComponent },
    mounted() {
        this.chatId = this.$route.params.id;

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
                this.chat_ids = data;
            }
        )
        
        // const url = this.$api + "/messages?chat_id=" + chatId;
        // fetch(url)
        // .then(
        //     res => {
        //         return res.json();
        //     }
        // )
        // .then(
        //     data => {
        //         this.messages = data;
        //     }
        // )
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
                    console.log(data);
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
</style>