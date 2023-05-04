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
            <h2>Наша история</h2>
            <p>Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст</p>
            <a class='button' href='#'>О нас</a>
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

.short-catalog {
    background-color: $light-pink;
    width: 100%;
    padding-top: 50px;
    padding-bottom: 50px;

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
    }

    &__item-img {
        width: 100%;
    }
}
</style>