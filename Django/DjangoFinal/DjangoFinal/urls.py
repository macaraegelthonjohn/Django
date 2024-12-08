from django.contrib import admin
from django.urls import path
from .views import index, Fui
from . import views # Ensure the Fui view is imported correctly

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', index, name='index'),  # The home page or index
    path('get-started/', Fui, name='Fui'),
    path('get-started/Herb.html', views.herb_page, name='herb_page'), 
     path('get-started/Fui.html', views.fui_page, name='fui_page'), # Correct route for Fui.html
]
