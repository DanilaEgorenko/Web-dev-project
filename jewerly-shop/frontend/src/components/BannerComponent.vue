<template>
    <div class='banner'>
        <h1 class='banner__title'>Новая коллекция</h1>
        <a href='#' class='button banner__link'>Посмотреть</a>
    </div>
</template>

<style lang='scss'>
@import '@/assets/scss/variables';

.banner {
    background-size: cover;
    width: $large-width - 124px;
    background: linear-gradient(0deg, rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.15)), url('@/assets/img/necklace-мiew-from-the-back.png');
    margin: 50px auto 0 auto;
    padding: 64px 64px 64px 64px;
    background-size: cover;

    &__title {
        font-family: 'Cormorant Unicase';
        text-transform: uppercase;
        font-weight: lighter;
        font-size: 96px;
        width: calc($large-width / 2);
        color: $main-light-text;
        margin: 0;
    }

    &__link {
        margin: 75px 150px 0 auto;
    }
}
</style>