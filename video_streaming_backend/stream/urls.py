from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('createbuck/', views.create_bucket),
    path('addvid/', views.add_video),
    path('getvid/', views.getVideo),
    
]