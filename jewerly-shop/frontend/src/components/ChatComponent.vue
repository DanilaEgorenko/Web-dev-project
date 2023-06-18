<template>
    <ul class='messages'>
        <li class='message-box' v-for='message in messages' v-bind:key="message">
            <p>{{ message.user }}</p>
            <p>{{ message.text }}</p>
        </li>
    </ul>
</template>

<script>
export default {
    name: 'chat-component',
    data() {
        return {
            messages: []
        }
    },
    mounted() {
        // fetch(this.$api, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json;charset=utf-8'
        //     },
        //     body: JSON.stringify(user),
        // })
        const chatId = this.$route.params.id
        const url = this.$api + "/messages?chat_id=" + chatId;
        fetch(url)
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