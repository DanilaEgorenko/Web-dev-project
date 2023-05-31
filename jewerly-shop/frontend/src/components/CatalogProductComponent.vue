<template>
    <div class="product-element">
        <img class="product-element__image" v-bind:src="'http://127.0.0.1:8000' + product.src" alt="Картинка товара">
        <div class="product-element__title-and-price">
            <h4 class="product-element__title">{{ product.title }}</h4>
            <p class="product-element__price">{{ product.price }} &#8381;</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'catalog-product-component',
    props: {
        product: Object,
    },
    data() {
        return {}
    },
}   
</script>

<style lang="scss" scoped>
@import '@/assets/scss/variables';
    
    h4, p {
        margin: 0
    }

    .product-element {
        display: flex;
        flex-direction: column;
        max-width: max-content;
        max-height: 345px;
    }

    .product-element__image {
        max-width: max-content;
        max-height: 304px;
    }

    .product-element__title-and-price {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        background-color: $main-light-text;
        box-sizing: border-box;
        margin: 0 auto;
        min-height: 41px;
        min-width: -webkit-fill-available;
        padding-left: 16px;
        padding-right: 13px;
    }

</style>