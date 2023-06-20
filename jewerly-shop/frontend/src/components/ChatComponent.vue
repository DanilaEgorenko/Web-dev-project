<template>
    <ul class='messages'>
        <li class='message-box' v-for='message in messages' v-bind:key="message.text + message.user + Math.random()">
            <p>{{ message.user }}</p>
            <p>{{ message.text }}</p>
        </li>
    </ul>
</template>

<script>
import Cookies from 'js-cookie';

export default {
    name: 'chat-component',
    data() {
        return {
            messages: []
        }
    },
    props: ['chatId'],
    mounted() {
        const url = this.$api + "chats/" + this.chatId + "/messages/";
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
                this.messages = data;
            }
        )
    }
}
</script>

<style lang='scss'>
@import '@/assets/scss/variables';

.messages {
    margin-left: auto;
    margin-right: auto;
    width: $large-width;
    display: flex;
    flex-direction: column;
    gap: 5px;
}
.message-box {
    background-color: grey;
    border-radius: 15px;
    display: block;
    width: fit-content;
    max-width: 300px;
    padding: 10px;
}
</style>