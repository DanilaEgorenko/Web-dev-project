<template>
    <main>
        <banner-component/>
        <h2>Каталог</h2>
        <short-catalog-component/>
        <lead-form-component/>
        <recently-bought-component/>
    </main>
</template>

<script>
import BannerComponent from '@/components/BannerComponent.vue';
import RecentlyBoughtComponent from '@/components/RecentlyBoughtComponent.vue';
import ShortCatalogComponent from '@/components/ShortCatalogComponent.vue'
import LeadFormComponent from '@/components/LeadFormComponent.vue';
import Cookies from "js-cookie";

export default {
    name: "main-page",
    components: { BannerComponent, RecentlyBoughtComponent, ShortCatalogComponent, LeadFormComponent },
    mounted() {
        const auth_code = this.$route.query.code;
        if (auth_code !== undefined) {
            this.validate_code(auth_code);
        }
    },
    methods: {
        validate_code(code) {
            const data = {
                'code': code,
            }

            fetch(this.$api + 'authenticate-code/', {
                method: 'post',
                body: JSON.stringify(data),
                headers: {
                    'content-type': 'application/json'
                },
            })
            .then((res) => res.json())
            .then((data) => {
                if (data.token !== undefined) {
                    Cookies.set('jwt', data.token);
                    this.$root.$emit('loginWithJWT');
                }
                location.href = '/';
            })
            .catch((err) => {
                console.log(err);
            })
        }
    }
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