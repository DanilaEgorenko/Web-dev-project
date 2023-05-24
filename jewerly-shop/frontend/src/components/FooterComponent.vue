<template>
    <footer class='footer'>
        <ul class='footer__list'>
            <li class="footer__list-item footer__list-item--title">
                Каталог
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Серьги</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Колье</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Подвески</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Браслеты</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Кольца</a>
            </li>
        </ul>
        <ul class='footer__list'>
            <li class="footer__list-item footer__list-item--title">
                Меню
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">О нас</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Магазины</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Контакты</a>
            </li>
            <li class="footer__list-item">
                <a class='footer__link' href="#">Доставка и возврат</a>
            </li>
        </ul>
        <div class='footer__contacts'>
            <a href="#" class='footer__contacts-number'>+7(912)999-99-99</a>
            <a href="#" class='footer__contacts-email'>plantext@gmail.com</a>
            <a href="#" class='footer__contacts-icon footer__contacts-icon--telegram'></a>
            <a href="#" class='footer__contacts-icon footer__contacts-icon--facebook'></a>
            <a href="#" class='footer__contacts-icon footer__contacts-icon--whatsapp'></a>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'footer-component'
}
</script>

<style lang='scss'>
@import '@/assets/scss/variables';

.footer {
    width: $large-width - 200px;
    margin: 75px auto 0 auto;
    background-color: $light-pink;
    padding: 80px 100px 50px 100px;
    display: flex;
    gap: 50px;

    &__list {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-start;
        gap: 5px;
        width: 300px;
    }

    &__list-item {
        &--title {
            font-size: 20px;
            line-height: 22px;
        }

        &:nth-child(2) {
            margin-top: 20px;
        }
    }

    &__list:nth-child(2n) {
        flex-grow: 1;
    }

    &__link {
        font-size: 16px;
        line-height: 18px;
        text-decoration: none;
        color: $main-dark-text;
    }

    &__link:hover {
        text-decoration: underline;
    }

    &__contacts {
        display: grid;
        grid-template-areas: 'number number number'
        'email email email'
        'telegram facebook whatsapp';
        grid-template-columns: 50px 50px auto;
        grid-template-rows: 50px 50px 50px;
    }

    &__contacts-icon {
        display: inline-block;
        width: 26px;
        height: 26px;
        background-repeat: no-repeat;

        &--facebook {
            grid-area: facebook;
            background-image: url('@/assets/img/facebook-icon.svg');
        }

        &--telegram {
            grid-area: telegram;
            background-image: url('@/assets/img/telegram-icon.svg');
        }

        &--whatsapp {
            grid-area: whatsapp;
            background-image: url('@/assets/img/whatsapp-icon.svg');
        }

        &--whatsapp, &--facebook, &--telegram {
            background-size: contain;
        }
    }

    &__contacts-number, &__contacts-email {
        display: block;
        font-size: 20px;
        text-decoration: none;
        color: $main-dark-text;
        line-height: 20px;

    }

    &__contacts-number:hover, &__contacts-email:hover {
        text-decoration: underline;
        
    }

    &__contacts-number::before, &__contacts-email::before {
        display: inline-block;
        content: '1';
        font-size: 0;
        line-height: 40px;
        height: 30px;
        width: 30px;
        background-size: bottom;
        background-repeat: no-repeat;
        margin-right: 20px;
    }

    &__contacts-email::before {
        background-image: url('@/assets/img/email-icon.svg');
    }

    &__contacts-email {
        grid-area: email;
    }

    &__contacts-number {
        grid-area: number;
    }

    &__contacts-number::before {
        background-image: url('@/assets/img/phone-icon.svg');
    }

    @media (max-width: 767px) {
    flex-direction: column;
    align-items: center;
    padding: 40px 20px;
    width: 100%;

    &__list {
        width: 100%;
        max-width: 300px;
    }

    &__list:nth-child(2n) {
        flex-grow: 0;
        margin-top: 20px;
    }
}
}


</style>