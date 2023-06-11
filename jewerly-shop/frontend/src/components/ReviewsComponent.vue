<template>
    <form class="review-form">
        <h2 class=review-form__title>Отзывы</h2>
        <h3 class="review-form__subtitle">Добавьте свой отзыв!</h3>
        <label class="review-form__label visually-hidden">Текст отзыва</label>
        <input type="textarea" v-model="text" class='review-form__text-input' placeholder='Ваш отзыв'>
        <input type='button' class="button" @click="submitReview" value='Отправить отзыв'>
    </form>
</template>

<script>
const axios = require('axios');

export default {
    name: 'reviews-component',
    data() {
        return {
            name: '',
            text: '',
            product: '',
            created_at: new Date(),
            rate: 5
        };
    },
    methods: {
        submitReview() {
            const reviewData = {
                user_id: 1,
                text: this.text,
                good_id: 1,
                created_at: new Date(),
                rate: 5
            };

            // Отправьте данные на сервер
            axios.post('http://localhost:8000/api/reviews/ ', reviewData)
            .then(response => {
                console.log(response.data.message);
            })
            .catch(error => {
                // Обработайте ошибку, если необходимо
                console.error(error);
            });
        }
    }
};
</script>

<style lang="scss" scoped>
@import '@/assets/scss/variables';

$form-height: 450px;

</style>