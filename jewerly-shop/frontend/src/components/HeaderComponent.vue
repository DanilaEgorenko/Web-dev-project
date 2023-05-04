<template>
    <header class='header'>
        <img src='@/assets/logo.svg' class='header__logo' alt="logo">
        <nav class='header__nav'>
            <ul class='header__nav-list'>
                <li class='header__nav-item'>О нас</li>
                <li class='header__nav-item'>Магазины</li>
                <li class='header__nav-item'>Контакты</li>
                <li class='header__nav-item'>Доставка и возврат</li>
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