<template>
    <div class="product-element">
        <!-- <input class="product-element__checkbox" type="checkbox" checked> -->
        <img class="product-element__image" v-bind:src="'@/assets/img/' + product.src" alt="Картинка товара">
        <h3 class="product-element__title">{{ product.title }}</h3>
        <p class="product-element__description">{{ product.description }}</p>
        <div class="product-element__counter">
            <button class="product-element__button" @click="reduceCount">-</button>
            <p class="product-element__count">{{ product.count }}</p>
            <button class="product-element__button" @click="addCount">+</button>
        </div>
        
        <p class="product-element__sum">{{ price_sum }} ₽</p>
    </div>
</template>

<script>
export default{
    name: 'product-component',
    props: {
        product: Object,
    },
    data() {
        return {}
    },
    computed:{
        price_sum: function () {
            return this.product.count * this.product.price;
        }
    },
    methods: {
        addCount(){
            this.$emit('add-count', this.product.id)
        },
        reduceCount(){
            if (this.product.count - 1 != 0){
                this.$emit('reduce-count', this.product.id)
            }
        }
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/variables';

.product-element{
    display: grid;
    margin-top: 1.5%;
    grid-template-columns: 1fr 4fr repeat(2, 0.7fr);
    grid-template-rows: repeat(2, 1fr);
    margin-left: auto;
    margin-right: auto;
    width: $large-width;
    &__image{
        margin-left: 5%;
        margin-top: 5%;
        grid-row: span 2;
    }
    &__title{}
    &__description{
        grid-row: 2;
        grid-column: 2;
    }
    &__counter{
        display: flex;
        grid-column: 4;
    }
    &__button{
        background: none;
        border: none;
    }
    &__count{
        background-color: $grey;
        width: 30%;
        text-align: center;
        line-height: 30px;
    }    
    &__sum{
        grid-column: 5;
    }
}
</style>