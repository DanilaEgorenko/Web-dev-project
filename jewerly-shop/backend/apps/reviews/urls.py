from django.urls import path
from .views import ReviewCreateView, get_good, get_user

urlpatterns = [
    path('', ReviewCreateView.as_view(), name='review-create'),
    path('user/1/', get_user),
    path('good/1/', get_good),
]