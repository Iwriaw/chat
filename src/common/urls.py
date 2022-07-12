from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from chat.views import test
api_urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('test/', test)
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns))
]
