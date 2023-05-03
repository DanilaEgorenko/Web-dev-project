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