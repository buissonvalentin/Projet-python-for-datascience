from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('model/', include('model.urls')),
    path('admin/', admin.site.urls),
]
