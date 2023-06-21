<template>
    <main class="catalog-page">
        <banner-component/>
        <section class="catalog-page__container">
            <h2 class="catalog-page__title">Каталог</h2>
            <p class="catalog-page__bread-crumbs bread-crumbs">
                <router-link to="/" class="bread-crumbs__main">Главная</router-link> 
                /
                <router-link to="catalog" class="bread-crumbs__catalog">Каталог</router-link>
            </p>
            <div class="catalog-page__catalog catalog">
                <div class="catalog__wrapper">
                    <div class="catalog__selects">
                        <select class="catalog__select" @change="filterByMaterial($event.target.value)">
                            <option
                                class="catalog__option"
                                value="all"
                                selected
                                >
                                Фильтр
                            </option>
                            <option
                                value="gold"
                                class="catalog__option"
                                >
                                Золото
                            </option>
                            <option
                                value="silver"
                                class="catalog__option"
                                >
                                Серебро
                            </option>
                        </select>
                        <select class="catalog__select" @change="filterByMinMax">
                            <option
                                value="all"
                                class="catalog__option"
                                selected
                                >
                                Сортировка
                            </option>
                            <option
                                value="cheap"
                                class="catalog__option"
                                >
                                От самых дешёвых
                            </option>
                            <option
                                value="expensive" 
                                class="catalog__option"
                                >
                                От самых дорогих
                            </option>
                        </select>
                    </div>

                    <div class="catalog__list-and-products">
                        <ul class="catalog__list">
                            <div class="catalog-list__main catalog-main">
                                <h3 class="catalog-main__title">Каталог</h3>
                                <ul class="catalog-main__list">
                                    <li class="catalog-main__item">
                                        <button
                                        class="catalog-main__button"
                                        @click="filterByCategory('all')"
                                        :class="{ 'current-category': selectedCategory === 'all' }"
                                        >Все</button>
                                    </li>
                                    <li class="catalog-main__item">
                                        <button
                                        class="catalog-main__button"
                                        @click="filterByCategory('earrings')"
                                        :class="{ 'current-category': selectedCategory === 'earrings' }"
                                        >Серьги</button>
                                    </li>
                                    <li class="catalog-main__item">
                                        <button
                                        class="catalog-main__button"
                                        @click="filterByCategory('necklaces')"
                                        :class="{ 'current-category': selectedCategory === 'necklaces' }"
                                        >Колье</button>
                                    </li>
                                    <li class="catalog-main__item">
                                        <button
                                        class="catalog-main__button"
                                        @click="filterByCategory('pendants')"
                                        :class="{ 'current-category': selectedCategory === 'pendants' }"
                                        >Подвески</button>
                                    </li>
                                    <li class="catalog-main__item">
                                        <button
                                        class="catalog-main__button"
                                        @click="filterByCategory('bracelets')"
                                        :class="{ 'current-category': selectedCategory === 'bracelets' }"
                                        >Браслеты</button>
                                    </li>
                                    <li class="catalog-main__item">
                                        <button
                                        class="catalog-main__button"
                                        @click="filterByCategory('rings')"
                                        :class="{ 'current-category': selectedCategory === 'rings' }"
                                        >Кольца</button>
                                    </li>
                                </ul>
                            </div>
                            <div class="catalog-list__price catalog-price">
                                <h3 class="catalog-price__title">Цена</h3>
                                <p class="catalog-price__selected-price">от {{ selectedPrice }} &#8381;</p>
                                <input
                                    class="catalog-price__slider"
                                    type="range"
                                    min=1000
                                    max=991000
                                    step=10000
                                    v-model="selectedPrice"
                                    @input="filterByPrice"
                                >
                            </div>
                            <div class="catalog-list__color catalog-color">
                                <h3 class="catalog-color__title">Цвет</h3>
                                <div class="catalog-color__colors">
                                    <label class="catalog-color__label" v-for="color in colors" :key="color">
                                        <input
                                            class="catalog-color__checkbox"
                                            @click="filterByColor"
                                            type="checkbox"
                                            :value="color"
                                            v-model="selectedColors"
                                        > 
                                        {{ color }}
                                    </label>
                                </div>
                            </div>
                            <div class="catalog-list__brand catalog-brand">
                                <h3 class="catalog-brand__title">Бренд</h3>
                                <div class="catalog-brand__brands">
                                    <label class="catalog-brand__label" v-for="brand in brands" :key="brand">
                                        <input
                                            class="catalog-brand__checkbox"
                                            @click="filterByBrand"
                                            type="checkbox"
                                            :value="brand"
                                            v-model="selectedBrands"
                                        > 
                                        {{ brand }}
                                    </label>
                                </div>
                            </div>
                        </ul>
                        <div class="catalog__products">
                            <div class="catalog-list__no-items" v-show="displayedProducts.length === 0">
                                <p>Не удалось найти подходящих товаров</p>
                            </div>
                            <catalog-product-component
                                v-for="product in displayedProducts" 
                                v-bind:key="product.id"
                                v-bind:product="product"
                            />
                        </div>
                    </div>
                    <div class="catalog__pages">
                        <div class="catalog__page" v-for="pageNumber in totalPages" :key="pageNumber">
                            <a
                            @click="changePage(pageNumber)"
                            :class="{ 'current-page': isCurrentPage(pageNumber) }"
                            >
                                {{ pageNumber }}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<script>
import BannerComponent from '@/components/BannerComponent.vue';
import CatalogProductComponent from '@/components/CatalogProductComponent.vue';

export default {
    name: 'catalog-page',
    data() {
        return {
            products: [],
            currentPage: 1,
            pageSize: 6,
            selectedCategory: 'all',
            selectedMaterial: 'all',
            selectedPrice: 1000,
            selectedMinMax: 'all',
            colors: ['grey', 'yellow'],
            selectedColors: [],
            brands: ['SOKOLOV', 'Tiffany & Co.'],
            selectedBrands: [],
        };
    },
    computed: {
        displayedProducts() {
            let filteredProducts = this.products;

            if (this.selectedCategory !== 'all') {
                filteredProducts = this.products.filter(product => product.category === this.selectedCategory);
            }

            if (this.selectedMaterial !== 'all') {
                filteredProducts = filteredProducts.filter(product => product.material === this.selectedMaterial);
            }

            filteredProducts = filteredProducts.filter(product => product.price >= parseInt(this.selectedPrice, 10));

            if (this.selectedMinMax === 'cheap') {
                filteredProducts = filteredProducts.sort((a, b) => a.price - b.price);
            } else if (this.selectedMinMax === 'expensive') {
                filteredProducts = filteredProducts.sort((a, b) => b.price - a.price);
            }

            const startIndex = (this.currentPage - 1) * this.pageSize;
            const endIndex = startIndex + this.pageSize;

            if (this.selectedColors.length > 0) {
                filteredProducts = filteredProducts.filter(product => {
                    return this.selectedColors.includes(product.color);
                });
            }

            if (this.selectedBrands.length > 0) {
                filteredProducts = filteredProducts.filter(product => {
                    return this.selectedBrands.includes(product.brand);
                });
            }

            return filteredProducts.slice(startIndex, endIndex);
        },
        totalPages() {
            let filteredProducts = this.products;

            if (this.selectedCategory !== 'all') {
                filteredProducts = this.products.filter(product => product.category === this.selectedCategory);
            }

            if (this.selectedMaterial !== 'all') {
                filteredProducts = filteredProducts.filter(product => product.material === this.selectedMaterial);
            }

            if (this.selectedColors.length > 0) {
                filteredProducts = filteredProducts.filter(product => {
                    return this.selectedColors.includes(product.color);
                });
            }

            if (this.selectedBrands.length > 0) {
                filteredProducts = filteredProducts.filter(product => {
                    return this.selectedBrands.includes(product.brand);
                });
            }

            return Math.ceil(filteredProducts.length / this.pageSize);
        },
        
    },
    methods: {
        changePage(pageNumber) {
            this.currentPage = pageNumber;
        },
        isCurrentPage(pageNumber){
            return pageNumber === this.currentPage;
        },
        filterByCategory(category) {
            this.selectedCategory = category;
            this.currentPage = 1;
        },
        filterByMaterial(material) {
            this.selectedMaterial = material;
            this.currentPage = 1;
        },
        filterByPrice(){
            this.currentPage = 1;
        },
        filterByMinMax(event){
            this.selectedMinMax = event.target.value;
            this.currentPage = 1;
        },
        filterByColor(){
            this.currentPage = 1;
        },
        filterByBrand(){
            this.currentPage = 1;
        },
    },
    mounted() {
        fetch("http://127.0.0.1:8000/api/goods/")
            .then(response => response.json())
            .then(data => {
                this.products = data
            });
    },
    components: {
        BannerComponent,
        CatalogProductComponent,
    }
};
</script>

<style lang="scss" scoped>
    @import '@/assets/scss/variables';

    .current-page, .current-category{
        color:grey
    }

    button {
        border: none;
        background: none;
        cursor: pointer;
    }

    a {
        cursor: pointer;
    }

    .catalog-page__title {
        margin-bottom: 0px;
    }

    .bread-crumbs {
        text-align: center;
    }

    .catalog__selects {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
    }

    .catalog__select {
        min-width: 233px;
        min-height: 43px;
        border: none;
    }

    .catalog {
        margin: 0 auto;
        background-color: $light-pink;
        min-height: 944px;
        max-width: 1440px;
    }

    .catalog__wrapper {
        padding: 17px 80px 32px 80px;
    }

    .catalog__select:first-child{
        margin-right: 21px;
    }

    .catalog__select {
        padding-left: 5px;
    }

    .catalog__list-and-products {
        margin-top: 34px;
        display: grid;
        grid-template-areas:
            "list products products products";
    }

    .catalog__list {
        margin: 0;
        grid-area: list;
        background-color: $main-light-text;
        max-width: 257px;
        min-height: 684px;
        padding: 48px 0px 0px 42px;
    }

    .catalog-main__title {
        margin-top: 0px;
    }

    .catalog__products{
        grid-area: products;
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        grid-template-rows: repeat(auto-fill, minmax(345px, 1fr));
        grid-column-gap: 20px;
        grid-row-gap: 43px;
    }

    .catalog__pages {
        display: flex;
        flex-direction: row;
        justify-content: center;
    }

    .catalog__page {
        margin: 54px 5px 0px 5px;
    }

    input[type="range"]::-webkit-slider-runnable-track {
        background-color: pink; /* Установите желаемый цвет фона для трека слайдера */
        border-radius: 25px;
    }

    .catalog-price__slider {
        border-radius: 25px;
    }

    .catalog-color__colors, .catalog-brand__brands {
        display: flex;
        flex-direction: column;
    }

    .catalog-color__label, .catalog-brand__label {
        margin-top: 10px;
    }

    .catalog-color__label:first-child, .catalog-brand__label:first-child {
        margin-top: 0px;
    }
</style>