from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

api_urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns))
]
