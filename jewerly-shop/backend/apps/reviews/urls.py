from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
]