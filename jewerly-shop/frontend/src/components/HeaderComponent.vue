<template>
    <header class='header'>
        <img src='@/assets/logo.png' class='header__logo' alt="logo">
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
                <button class='button button--icon'>
                    <img src='@/assets/profile-icon.svg' alt="profile-icon">
                </button>
            </li>
            <li class='header__btn-item'>
                <button class='button button--icon'>
                    <img src='@/assets/shopping-card-icon.svg' alt="shopping-cart-icon">
                </button>
            </li>
            <li class='header__btn-item'>
                <button class='button button--icon'>
                    <img src='@/assets/heart-icon.svg' alt="favourites-icon">
                </button>
            </li>
        </ul>
    </header>
</template>

<script>
export default {
    name: 'header-component'
}
</script>