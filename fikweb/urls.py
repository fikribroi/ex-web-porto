from django.contrib import admin
from django.urls import path, include

handler404 = 'porto.views.error404'
handler500 = 'porto.views.error500'
urlpatterns = [
    path('ini-sangat-rahasia/', admin.site.urls),
    path('', include('porto.urls')),
]