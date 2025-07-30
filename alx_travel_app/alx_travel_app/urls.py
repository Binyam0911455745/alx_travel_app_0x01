# alx_travel_app_0x01/alx_travel_app/alx_travel_app/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions # For drf-yasg
from drf_yasg.views import get_schema_view # For drf-yasg
from drf_yasg import openapi # For drf-yasg

# Import the router from your listings app's urls.py
# NOTE: The path should be relative to your project's root for Python imports.
# Since your 'listings' app is at alx_travel_app_0x01/alx_travel_app/listings,
# and this urls.py is at alx_travel_app_0x01/alx_travel_app/alx_travel_app,
# the import should be from the 'parent' of this directory, then 'listings.urls'.
from listings.urls import router # <--- NEW IMPORT

# Schema for Swagger/OpenAPI documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Alx Travel App API",
      default_version='v1',
      description="API for managing travel listings and bookings",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@alxtravel.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # <--- NEW: Include listings API URLs here

    # URLs for Swagger/OpenAPI documentation
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
