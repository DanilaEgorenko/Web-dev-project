<template>
    <main>
        <banner-component/>
        <h2>Каталог</h2>
        <short-catalog-component/>
        <form action=""></form>
        <recently-bought-component/>
    </main>
</template>

<script>
import BannerComponent from '@/components/BannerComponent.vue';
import RecentlyBoughtComponent from '@/components/RecentlyBoughtComponent.vue';
import ShortCatalogComponent from '@/components/ShortCatalogComponent.vue'

export default {
    name: "main-page",
    components: { BannerComponent, RecentlyBoughtComponent, ShortCatalogComponent }
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