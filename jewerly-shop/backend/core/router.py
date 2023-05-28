from rest_framework.routers import DefaultRouter
from apps.goods.views import GoodViewSet
from apps.orders.views import OrderViewSet
    
router = DefaultRouter()

router.register('goods', GoodViewSet, basename='Goods')
router.register('orders', OrderViewSet, basename='Orders')
