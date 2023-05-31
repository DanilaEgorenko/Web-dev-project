<template>
    <form class="lead-form" method='get'>
        <img class='lead-form__img' src="@/assets/img/heart-shaped-pendants.png" alt="heart-shaped-pendants">
        <h2 class=lead-form__title>Остались вопросы?</h2>
        <p class="lead-form__subtitle">Мы свяжемся с вами лично!</p>
        <label for="lead-form-email">Ваша почта</label>
        <input v-model='email' name="email" type="email" id="lead-form-email" class='lead-form__text-input' placeholder='Ваша почта'>
        <label for="lead-form-name">Ваше имя</label>
        <input type="text" v-model='name' name="name" id="lead-form-name" class='lead-form__text-input' placeholder='Ваше имя'>
        <input type="input" value="Оставить заявку" class="lead-form__submit button" v-on:click='sendCta()'>
    </form>
</template>

<script>
export default {
    name: 'lead-form-component',
    data() {
        return {
            email: '',
            name: ''
        }
    },
    methods: {
        sendCta() {
            if (!this.email && !this.name) {
                console.log(this.email)
                return
            }
            const data = {
                'email': this.email,
                'name': this.name
            }
            fetch('http://localhost:8000/api/cta/', {
                method: 'post', 
                body: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then(response => response.json())
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

$form-height: 450px;

.lead-form {
    position: relative;
    width: $large-width;
    margin: 150px auto 0 auto;
    display: flex;
    flex-direction: column;
    height: $form-height;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: space-between;

    &__text-input {
        border: none;
        width: calc(50% - 25px);
        margin-left: 25px;
        background-color: $grey;
        height: 60px;
        padding-left: 40px;
    }

    &__title, &__subtitle {
        text-align: left;
        margin-left: 25px;
        margin-bottom: 0;
        margin-top: 0;
    }

    &__text-input:nth-child(5) {
        margin-top: 40px;
    }

    &__submit {
        margin: 40px auto 0 auto;
    }

    &__img {
        width: 50%;
        height: $form-height;
        object-fit: cover;
    }

    &__img, input, &__title, &__subtitle {
        position: relative;
        z-index: 10;
    }

    &::before {
        content: '';
        position: absolute;
        left: calc(0px - #{$large-width-margin});
        top: -200px;
        z-index: 0;
        display: block;
        height: 180%;
        width: 800px;
        background-image: url('@/assets/img/pink-star.svg');
        background-repeat: no-repeat;
        background-size: contain;
        background-position: left;
    }

    label {
        display: none;
    }
}
</style>