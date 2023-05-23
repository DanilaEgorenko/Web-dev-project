<template>
    <transition name="modal-fade">
        <div class="modal-backdrop" @click="closeModal">
            <div class="delete-modal" @click="closeModal">
                <button class="delete-modal__close-button" @click="closeModal">X</button>
                <h2 class="delete-modal__header">Подтверждение</h2>
                <p class="delete-modal__text">Вы уверены, что хотите удалить {{ buyProduct.title }} из корзины?</p>
                <div class="delete-modal__buttons">
                    <button class="delete-modal__delete-button" @click="deleteProduct">Удалить</button>
                    <button class="delete-modal__cancel-button" @click="closeModal">Отмена</button>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default{
    name: "delete-product-modal",
    props: { 
        buyProduct: Object,
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

<style lang="scss" scoped>
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
    height: 40%;
    left: 25%;
    top: 25%;
    background-color: $main-light-text;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    &__close-button{
        color: red;
    }
    &__text{
        align-self: center;
    }
    &__buttons{
        display: flex;
        justify-content: space-around;
        margin-bottom: 25px;
    }
    &__cancel-button{
        background-color: $grey;
        color: $main-light-text;
        border: none;
        border-radius: 26px;
        width: 20%;
        padding: 10px 0 10px 0;
        &:hover{
            background-color: #949090;
        }
    }
    &__delete-button{
        background-color: red;
        color: $main-light-text;
        border: none;
        border-radius: 26px;
        width: 20%;
        padding: 10px 0 10px 0;
        &:hover{
            background-color: rgb(184, 6, 6);
        }
    }
}
</style>