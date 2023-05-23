from rest_framework.routers import DefaultRouter
from apps.goods.views import GoodViewSet
    
router = DefaultRouter()

router.register('goods', GoodViewSet, basename='Goods')
