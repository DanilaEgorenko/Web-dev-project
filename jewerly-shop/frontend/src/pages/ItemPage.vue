<template>
    <main>
        <item-card-component/>
        <reviews-component/>
    </main>
</template>

<script>
import ItemCardComponent from '@/components/ItemCardComponent.vue';
import ReviewsComponent from '@/components/ReviewsComponent.vue';

export default {
    name: "item-page",
    components: { ItemCardComponent, ReviewsComponent }
}
</script>

<style lang='scss'>
@import '@/assets/scss/variables';

.button {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background-color: $pink;
    height: 60px;
    border: none;
    border-radius: 30px;
    padding: 0 75px 0 75px;
    width: fit-content;
    color: white;
    text-decoration: none;

    &:hover {
        cursor: pointer;
    }

    &:active {
        background-color: $active-color;

    }

    &--icon {
        background: none;
        height: 80px;
        width: 80px;
        padding: 0;
        border-radius: 100%;
    }
}
</style>