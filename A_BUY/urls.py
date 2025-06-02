from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include, re_path

schema_view = get_schema_view(
   openapi.Info(
      title="A-Buy API",
      default_version='v1',
      description="API documentation for A-Buy",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/gigs/', include('gigs.urls')),
    path('api/subscriptions/', include('subscriptions.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/chats/', include('chats.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/support/', include('support.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
