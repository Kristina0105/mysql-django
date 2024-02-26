from django.contrib import admin
from django.urls import path, include

from cities.urls import url_rlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(url_rlist))
]
