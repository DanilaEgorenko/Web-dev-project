<template>
    <ul>
        <li v-for='message in messages' v-bind:key="message">
            {{ message }}
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