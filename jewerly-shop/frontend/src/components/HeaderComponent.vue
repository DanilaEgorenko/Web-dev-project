<template>
    <header class='header'>
        <router-link class='header__logo-link' k to="/">
            <img src='@/assets/img/logo.png' class='header__logo-img' alt="logo">
        </router-link>
        <nav class='header__nav'>
            <ul class='header__nav-list'>
                <li class='header__nav-item'><a href='#' class='header__link'>О нас</a></li>
                <li class='header__nav-item'><a href='#' class='header__link'>Магазины</a></li>
                <li class='header__nav-item'><a href='#' class='header__link'>Контакты</a></li>
                <li class='header__nav-item'><a href='#' class='header__link'>Доставка и возврат</a></li>
            </ul>
        </nav>
        <ul class='header__btn-list'>
            <li class='header__btn-item'>
                <router-link class='button button--icon' to="/signin">
                    <img src='@/assets/img/profile-icon.svg' alt="profile-icon">
                </router-link>
            </li>
            <li class='header__btn-item'>
                <router-link class='button button--icon' to="/basket">
                    <img src='@/assets/img/shopping-card-icon.svg' alt="shopping-cart-icon">
                </router-link>
            </li>
            <li class='header__btn-item'>
                <button class='button button--icon'>
                    <img src='@/assets/img/heart-icon.svg' alt="favourites-icon">
                </button>
            </li>
        </ul>
    </header>
</template>

<script>
export default {
    name: 'header-component',
}
</script>

<style lang='scss'>
@import '@/assets/scss/variables';

.header {
    width: $large-width;
    display: flex;
    justify-content: space-between;
    margin: 20px auto 20px auto;
    height: 80px;

    &__nav-list {
        display: flex;
        height: 100%;
        margin: 0;
        justify-content: space-between;
        align-items: center;
        gap: 40px;
    }

    &__btn-list {
        height: 100%;
        margin: 0;
    }

    &__btn-item {
        height: 100%;
        display: inline-block;
    }

    &__link {
        text-decoration: none;
        color: $main-dark-text;
    }

    &__logo-link {

    }

    &__logo-img {
        height: 100%;
    }
}
</style>