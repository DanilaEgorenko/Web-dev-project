<template>
    <section class="item">
        <img class="item__img" src="@/assets/img/item-img.jpg" alt="Фото товара">
        <div class="item-info">
            <div class="item-info__heading">
                <h2 class="item__heading">Название товара</h2>
                <div class="item__rating">
                    <ul class="item__rating-list">
                        <li>
                            <img src="@/assets/img/rating-icon.svg" alt="">
                        </li>
                        <li>
                            <img src="@/assets/img/rating-icon.svg" alt="">
                        </li>
                        <li>
                            <img src="@/assets/img/rating-icon.svg" alt="">
                        </li>
                        <li>
                            <img src="@/assets/img/rating-icon.svg" alt="">
                        </li>
                        <li>
                            <img src="@/assets/img/rating-icon.svg" alt="">
                        </li>
                    </ul>
                    <p class="item__rating-score">(0)</p>
                </div>
            </div>
            <div class="item-info__list">
                <div class="item-info__color">
                    <h3 class="item-info__color-heading">Выбор цвета</h3>
                    <ul class="item-info__color-choice choice">
                        <li class="choice__item">

                        </li>
                        <li class="choice__item">

                        </li>
                        <li class="choice__item">

                        </li>
                        <li class="choice__item">

                        </li>
                    </ul>
                </div>
                <div class="item-info__size">
                    <h3 class="item-info__size-heading">Размер</h3>
                    <ul class="item-info__size-choice choice">
                        <li class="choice__item">

                        </li>
                        <li class="choice__item">

                        </li>
                        <li class="choice__item">

                        </li>
                        <li class="choice__item">

                        </li>
                    </ul>
                </div>
                <div class="item-info__description">
                    <h3 class="item-info__description-heading">Описание</h3>
                    <p class="item-info__description-text">Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст Текст</p>
                </div>
            </div>
            <p class="item__price">9 999 Р</p>
            <div class="item__buttons">
                <button class="button">В корзину</button>
                <button class="icon-btn"><img src="@/assets/img/fav-icon.svg" alt="В избранное"></button>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'item-card-component'
}
</script>

<style lang="scss" scoped>
@import '@/assets/scss/variables';

$form-height: 450px;

.item {
    margin: 50px auto 0 auto;
    display: flex;
    flex-direction: row;
    max-width: 1088px;

    &__img {
        width: 413px;
        height: 462px;
    }

    &__heading { 
        text-align: start;
        margin: 0;
    }

    &__rating {
        display: flex;
        flex-direction: row;
    }

    &__rating-score {
        margin-left: 3px;
    }

    &__rating-list {
        display: flex;
        flex-direction: row;
    }

    &__price {
        font-weight: 400;
        font-size: 32px;
        line-height: 36px;
        margin: 22px 0px 22px 0px;
    }
}


.item-info {
    margin-left: 100px;
    max-width: 602px;

    &__heading {
        display: flex;
        flex-direction: row;
        align-items: baseline;
        justify-content: space-between;
    }

    &__description-heading {
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 22px;
    }

    &__color-choice {
        display: flex;
        flex-direction: row;
    }

    &__size-heading {
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 22px;
    }

    &__size-choice {
        display: flex;
        flex-direction: row;
    }

    &__color-heading {
        font-style: normal;
        font-weight: 400;
        font-size: 20px;
        line-height: 22px;
    }
}

.choice {
    &__item {
        width: 34px;
        height: 34px;
        background: #D9D9D9;
        border-radius: 50%;
        margin-right: 17px;
        border:1px solid transparent;
    }
    &__item:hover {
    border: 1px solid #000000;
    }
}

.item__buttons {
    display: flex;
    flex-direction: row;
}

.icon-btn {
    background-color: white; 
    border: none;
    cursor: pointer;
    margin-left: 15px;
}

/* Для мобильных устройств */
@media (max-width: 767px) {
        .item {
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            max-width: 100%;
            justify-content: center;
            padding: 20px;
        }

        .item__img {
            width: 100%;
            height: auto;
        }

        .item__heading {
            text-align: start;
            margin: 0;
        }

        .item__rating {
            display: none;
        }

        .item__price {
            font-weight: 400;
            font-size: 24px;
            line-height: 28px;
            margin: 22px 0;
        }


    .item-info {
        margin-left: 0;
        max-width: 100%;
    }

    .item-info__heading {
        flex-direction: column;
        align-items: flex-start;
        justify-content: space-between;
    }

    .item-info__description-heading,
    .item-info__color-heading,
    .item-info__size-heading {
        font-size: 18px;
        line-height: 20px;
    }

    .choice__item {
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }

    .icon-btn {
        margin-left: 0;
    }

}

/* Для планшетов и средних устройств */
@media (min-width: 768px) and (max-width: 991px) {
    .item {
        flex-direction: row;
        max-width: 768px;
    }

    .item__img {
        width: 50%;
        height: auto;
    }

    .item-info {
        margin-left: 50px;
        max-width: 50%;
    }

    .item-info__heading {
        flex-direction: row;
    }

    .item__rating-list {
        margin-left: 10px;
    }

    .item__rating-score {
        font-size: 16px;
    }

    .item-info__list {
        margin-top: 20px;
    }

    .item-info__color-heading,
    .item-info__size-heading,
    .item-info__description-heading {
        font-size: 18px;
    }

    .choice__item {
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }

    .item__buttons {
        flex-direction: column;
        align-items: flex-start;
        margin-top: 20px;
    }

    .icon-btn {
        margin-top: 10px;
    }
}


/* Для настольных компьютеров и больших устройств */
@media (min-width: 992px) {
    .item {
    margin: 50px auto 0 auto;
    display: flex;
    flex-direction: row;
    max-width: 1088px;

    &__img {
        width: 413px;
        height: 462px;
    }

    &__heading { 
        text-align: start;
        margin: 0;
    }

    &__rating {
        display: flex;
        flex-direction: row;
    }

    &__rating-score {
        margin-left: 3px;
    }

    &__rating-list {
        display: flex;
        flex-direction: row;
    }

    &__price {
        font-weight: 400;
        font-size: 32px;
        line-height: 36px;
        margin: 22px 0px 22px 0px;
    }
}
}

</style>