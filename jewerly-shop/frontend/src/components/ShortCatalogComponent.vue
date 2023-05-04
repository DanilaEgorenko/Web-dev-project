<template>
    <div class='short-catalog'>
        <ul class='short-catalog__list'>
            <li class='short-catalog__item'>
                <img class='short-catalog__item-img' src="@/assets/img/earrings.png" alt="earrings">
                <a class='short-catalog__item-link' href="#">Серьги</a>
            </li>
            <li class='short-catalog__item'>
                <img class='short-catalog__item-img' src="@/assets/img/suspension.png" alt="earrings">
                <a class='short-catalog__item-link' href="#">Подвески</a>
            </li>
            <li class='short-catalog__item'>
                <img class='short-catalog__item-img' src="@/assets/img/bracelet.png" alt="earrings">
                <a class='short-catalog__item-link' href="#">Браслеты</a>
            </li>
            <li class='short-catalog__item'>
                <img class='short-catalog__item-img' src="@/assets/img/rings.png" alt="earrings">
                <a class='short-catalog__item-link' href="#">Кольца</a>
            </li>
        </ul>
        <section class='about-us'>
            <h2 class='about-us__title'>Наша история</h2>
            <p class='about-us__text'>Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст</p>
            <a class='about-us__button button' href='#'>О нас</a>
            <img src="@/assets/img/suspension-from-view-the-cross.jpg" alt="suspension" class='about-us__front-img'/>
            <img src="@/assets/img/earrings-heart-shaped.png" alt="suspension" class='about-us__back-img'/>
        </section>
    </div>
</template>

<script>
export default {
    name: 'short-catalog-component'
}
</script>

<style lang='scss'>
@import '@/assets/scss/variables';

$img-height: 380px;

.short-catalog {
    background-color: $light-pink;
    width: 100%;
    padding-top: 50px;
    padding-bottom: 300px;
    overflow: hidden;
    position: relative;

    &__list {
        display: flex;
        margin-left: $large-width-margin;
        width: $large-width;
        justify-content: space-between;
    }

    &__item {
        width: 24%;
    }

    &__item-link {
        text-decoration: none;
        text-align: center;
        display: inline-block;
        width: 100%;
        margin-top: 10px;
        font-size: 20px;
        color: $main-dark-text;
        z-index: 2;
        position: relative;
    }

    &__item-img {
        width: 100%;
        height: $img-height;
        object-fit: contain;
        z-index: 2;
        position: relative;
    }

    .about-us {
        width: $large-width / 2 + 25px;
        margin-top: 200px;
        margin-left: $large-width-margin;
        background-color: white;
        padding: 50px;
        position: relative;

        &__title {
            text-align: left;
            font-size: 40px;
            line-height: 45px;
            font-weight: 500;
        }

        &__text {
            font-size: 16px;
            line-height: 18px;
        }

        &__button {
            margin-top: 50px;
        }

        &__back-img {
            position: absolute;
            top: 0;
            z-index: 2;
            left: $large-width / 2 + 250px;
        }

        &__front-img {
            position: absolute;
            left: $large-width / 2 + 75px;
            z-index: 3;
            top: 250px;
        }
    }

    &::after {
        content: '';
        right: 0;
        top: $img-height + 100px;
        z-index: 0;
        display: block;
        position: absolute;
        height: 950px;
        width: 60%;
        background-image: url('@/assets/img/white-star.svg');
        background-repeat: no-repeat;
        background-size: contain;
        background-position: right;
    }
}
</style>