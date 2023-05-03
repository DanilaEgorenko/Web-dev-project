<template>
    <main>
        <banner-component/>
        <h2>Каталог</h2>
        <div></div>
        <form action=""></form>
        <!-- <recently-bought></recently-bought> -->
    </main>
</template>

<script>
import BannerComponent from '@/components/BannerComponent.vue';

export default {
    name: "MainPage",
    comments: {
        BannerComponent
    },
    components: { BannerComponent }
}
</script>