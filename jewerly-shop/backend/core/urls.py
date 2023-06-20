from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import urls as auth_urls
from .router import router
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import TemplateView
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from apps.users.views import authenticate_code, get_user, check_jwt, LoginView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    patterns=[
        path('api/', include(router.urls)),
    ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include(auth_urls)),
    path('api/reviews/', include('apps.reviews.urls')),
    path(
    'swagger-ui/',
    TemplateView.as_view(
        template_name='swaggerui/swaggerui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ),
    name='swagger-ui'),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    # path('social-auth/', include('social_django.urls', namespace='social')),
    path('google-sign-in/', views.signInWithGoogle, name='google-sign-in'),
    path('test/', views.read_request, name='test'),
    path('', views.my_view),
    path('logout/', views.out, name='logout'),
    path('frontend/', views.frontend, name='frontend'),
    path('api/authenticate-code/', authenticate_code, name='authenticate-code'),
    path('api/get_user/', get_user, name='get-user'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/check-jwt/', check_jwt, name='get-user'),
]