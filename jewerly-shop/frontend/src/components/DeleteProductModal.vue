<template>
    <transition name="modal-fade">
        <div class="modal-backdrop" @click="closeModal">
            <div class="delete-modal" @click="closeModal">
                <button class="delete-modal__close-button" @click="closeModal">X</button>
                <h2 class="delete-modal__header">Подтверждение</h2>
                <p class="delete-modal__text">Вы уверены, что хотите удалить {{ product.title }} из корзины?</p>
                <button class="delete-modal__delete-button" @click="deleteProduct">Удалить</button>
                <button class="delete-modal__cancel-button" @click="closeModal">Отмена</button>
            </div>
        </div>
    </transition>
</template>

<script>
export default{
    name: "delete-product-modal",
    props: { 
        product: Object,
    },
    methods: {
        closeModal() {
            this.$emit('close')
        },
        deleteProduct(){
            this.$emit('delete')
        }
    }
}
</script>

<style lang="scss">
@import '@/assets/scss/variables';
.modal-fade-enter,
.modal-fade-leave-active {
    opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity .5s ease
}

.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}

.delete-modal{
    position: absolute;
    width: 50%;
    height: 50%;
    left: 25%;
    top: 25%;
    background-color: $main-light-text;
    &__close-button{
        color: red;
    }
}
</style>