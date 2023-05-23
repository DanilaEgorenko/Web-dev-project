<template>
    <div class="buyProduct-element">
        <!-- <input class="buyProduct-element__checkbox" type="checkbox" checked> -->
        <img class="buyProduct-element__image" v-bind:src="'@/assets/img/' + buyProduct.src" alt="Картинка товара">
        <h3 class="buyProduct-element__title">{{ buyProduct.title }}</h3>
        <p class="buyProduct-element__description">{{ buyProduct.description }}</p>
        <div class="buyProduct-element__counter">
            <button class="buyProduct-element__button" @click="reduceCount">-</button>
            <p class="buyProduct-element__count">{{ buyProduct.count }}</p>
            <button class="buyProduct-element__button" @click="addCount">+</button>
        </div>
        
        <p class="buyProduct-element__sum">{{ price_sum }} ₽</p>
    </div>
</template>

<script>
export default{
    name: 'buyProduct-component',
    props: {
        buyProduct: Object,
    },
    data() {
        return {}
    },
    computed:{
        price_sum: function () {
            return this.buyProduct.count * this.buyProduct.price;
        }
    },
    methods: {
        addCount(){
            this.$emit('add-count', this.buyProduct.id)
        },
        reduceCount(){
            if (this.buyProduct.count - 1 != 0){
                this.$emit('reduce-count', this.buyProduct.id)
            }
        }
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/variables';

.buyProduct-element{
    display: grid;
    margin-top: 1.5%;
    grid-template-columns: 1fr 4fr repeat(2, 0.7fr);
    grid-template-rows: repeat(2, 1fr);
    &__image{
        margin-left: 5%;
        margin-top: 5%;
        grid-row: span 2;
    }
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