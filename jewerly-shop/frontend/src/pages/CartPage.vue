<template>
    <main class="cart-page">
        <product-component 
            v-for="product in products" 
            v-bind:key="product.id"
            v-bind:product="product"
            @add-count="AddCount"
            @reduce-count="ReduceCount"
            @delete-product="DeleteProduct"
        />
        <div class="cart-page__cart-footer cart-footer">
            <p class="cart-footer__description">
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
                Текст Текст Текст Текст Текст Текст Текст Текст Текст 
            </p>
            <div class="cart-footer__promocode">
                <label class="cart-footer__label-promocode" for="promocode">Введите промокод</label>
                <input class="cart-footer__input-promocode" id="promocode" type="text">
            </div>
            <h2 class="cart-footer__amount"><span>Итого</span> <span>{{ total_amount }}</span></h2>
            <button class="cart-footer__pay">Оплатить</button>
        </div>
    </main>
</template>

<script>
import ProductComponent from '@/components/ProductComponent.vue';
export default{
    name: 'cart-page',
    data() {
        return {
            products: [
                {id: 1, title: 'Заголовок', description: 'Текст Текст Текст Текст Текст Текст Текст Текст', 
                    price: 9999, count: 1, src: 'https://egelge.com/upload/images/50563_465455_05.jpg'},
                {id: 2, title: 'Заголовок', description: 'Текст Текст Текст Текст Текст Текст Текст Текст', 
                    price: 9999, count: 1, src: 'https://egelge.com/upload/images/50563_465455_05.jpg'},
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
            this.products.find(x => x.id == id).count += 1;
        },
        ReduceCount(id) {
            this.products.find(x => x.id == id).count -= 1;
        },
        DeleteProduct(id) {
            this.products.pop(this.products.find(x => x.id == id));
        }
    },
    components: {
        ProductComponent,
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/variables';


.cart-page{
    margin: 50px 3% 0 3%;
}
.cart-footer{
    display: grid;
    margin-top: 5%;
    padding: 2% 2% 0 2%;
    margin-left: auto;
    margin-right: auto;
    width: calc(#{$large-width} - 4%);
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