from rest_framework.routers import DefaultRouter
from apps.goods.views import GoodViewSet
from apps.orders.views import OrderViewSet, CTAViewSet
from apps.articles.views import ArticleViewSet
from apps.chat_messages.views import MessageViewSet
    
router = DefaultRouter()

router.register('goods', GoodViewSet, basename='Goods')
router.register('orders', OrderViewSet, basename='Orders')
router.register('cta', CTAViewSet, basename='cta')
router.register('article', ArticleViewSet, basename='Article')
router.register('messages', MessageViewSet, basename='Messages')
