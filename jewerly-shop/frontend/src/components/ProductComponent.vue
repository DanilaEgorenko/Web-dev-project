<template>
    <div class="product-element">
        <!-- <input class="product-element__checkbox" type="checkbox" checked> -->
        <img class="product-element__image" v-bind:src="product.src" alt="Картинка товара">
        <h3 class="product-element__title">{{ product.title }}</h3>
        <p class="product-element__description">{{ product.description }}</p>
        <div class="product-element__counter">
            <button class="product-element__button" @click="reduceCount">-</button>
            <p class="product-element__count">{{ product.count }}</p>
            <button class="product-element__button" @click="addCount">+</button>
        </div>
        
        <p class="product-element__sum">{{ price_sum }} ₽</p>
        <delete-product-modal 
            v-bind:product="product"
            v-show="isVisibleModal"
            @close="closeModal"
            @delete="deleteProduct"/>
    </div>
</template>

<script>
import DeleteProductModal from './DeleteProductModal.vue';
export default{
    name: 'product-component',
    props: {
        product: Object,
    },
    data() {
        return {
            isVisibleModal: false,
        }
    },
    computed:{
        price_sum: function () {
            return this.product.count * this.product.price;
        }
    },
    methods: {
        addCount(){
            this.$emit('add-count', this.product.id);
        },
        reduceCount(){
            if (this.product.count - 1 != 0){
                this.$emit('reduce-count', this.product.id);
            }
            else {
                this.isVisibleModal = !this.isVisibleModal;
            }
        },
        closeModal() {
            this.isVisibleModal = !this.isVisibleModal;
        },
        deleteProduct() {
            this.$emit('delete-product', this.product.id)
            this.closeModal();
        }
    },
    components: {
        DeleteProductModal
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/variables';

.product-element{
    display: grid;
    margin-top: 1.5%;
    grid-template-columns: 1fr 4fr repeat(2, 0.7fr);
<<<<<<< HEAD
    grid-template-rows: repeat(2, 1fr);
    margin-left: auto;
    margin-right: auto;
    width: $large-width;
=======
    grid-template-rows: 0.5fr 1fr;
    grid-gap: 25px;
>>>>>>> cbb8599 (Add the BEST MODAL WINDOW)
    &__image{
        margin-left: 5%;
        margin-top: 5%;
        width: 100%;
        height: 100%;
        object-fit:scale-down;
        grid-row: span 2;
    }
    &__title{
        margin-left: 2%;
    }
    &__description{
        margin-left: 2%;
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