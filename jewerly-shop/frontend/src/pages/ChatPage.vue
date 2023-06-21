<template>
    <main>
        <h2>Чат с {{ user_to }} ({{ email_to }})</h2>
        <chat-component :chatId=chatId></chat-component>
        <form class='form'>
            <label class='form__label' for="text">Текст сообщения</label>
            <input class='form__input' type="text" name="text" id="text" v-model='text' placeholder='Ваше сообщение' required>
            <input class='form__submit' type="button" @click='startChat()' value='Начать чат'>
            <p v-if='form_error' style='color: red'>{{ form_error }}</p>
        </form>
    </main>
</template>

<script>
import ChatComponent from '@/components/ChatComponent.vue';
import Cookies from 'js-cookie';

export default {
    
    name: 'chat-page',
    data() {
        return {
            chatId: this.$route.params.id,
            email_to: '',
            user_to: '',
            text: '',
            form_error: '',
        }
    },
    components: { ChatComponent },
    mounted() {
        const url = this.$api + "chats/" + this.chatId + "/";
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
                this.user_to = data.recipient_name; 
                this.email_to = data.recipient_email;
            }
        );
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
                        this.chatId = data.chat_id;
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

    &__label {
        display: none;
    }

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