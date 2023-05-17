<template>
    <main class="bascket-page">
        <product-component 
            v-for="product in products" 
            v-bind:key="product.id"
            v-bind:product="product"
            @add-count="AddCount"
            @reduce-count="ReduceCount"
        />
        <div class="bascket-page__bascket-footer bascket-footer">
            <p class="bascket-footer__description">
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
            </p>
            <div class="bascket-footer__promocode">
                <label class="bascket-footer__label-promocode" for="promocode">Введите промокод</label>
                <input class="bascket-footer__input-promocode" id="promocode" type="text">
            </div>
            <h2 class="bascket-footer__amount"><span>Итого</span> <span>{{ total_amount }}</span></h2>
            <button class="bascket-footer__pay">Оплатить</button>
        </div>
    </main>
</template>

<script>
import ProductComponent from '@/components/ProductComponent.vue';
export default{
    name: 'basket-page',
    data() {
        return {
            products: [
                {id: 1, title: 'Заголовок', description: 'Текст Текст Текст Текст Текст Текст Текст Текст', 
                    price: 9999, count: 1, src: 'aerrings-cross-shaped.png'},
                {id: 2, title: 'Заголовок', description: 'Текст Текст Текст Текст Текст Текст Текст Текст', 
                    price: 9999, count: 1, src: 'aerrings-cross-shaped.png'},
            ],
        }
    }, 
    computed:{
        total_amount: function () {
            let sum = 0;
            this.products.forEach((item) => {
                sum += item.price * item.count;
            })
            return sum;
        }
    },
    methods: {
        AddCount(id) {
            this.products.find(x => x.id == id).count += 1
        },
        ReduceCount(id) {
            this.products.find(x => x.id == id).count -= 1
        }
    },
    components: {
        ProductComponent,
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/variables';


.bascket-page{
    margin: 50px 3% 0 3%;
}
.bascket-footer{
    display: grid;
    margin-top: 5%;
    padding: 2% 2% 0 2%;
    background: $light-pink;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: repeat(3, 1fr);
    &__description{
        grid-column: span 2;
    }
    &__promocode{
        display: flex;
        flex-direction: column;
    }
    &__input-promocode{
        margin-top: 1%;
        width: 30%;
        height: 30%;
        border: none;   
    }
    &__amount+&__pay{
        grid-column: 2;
    }
    &__amount{
        display: flex;
        justify-content: space-around;
    }
    &__pay{
        width: 80%;
        height: 60%;
        background-color: $pink;
        border: none;
        border-radius: 26px;
        color: #FFFFFF;
        justify-self: center;
    }
}
</style>