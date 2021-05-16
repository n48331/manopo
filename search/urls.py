from django.urls import path
from . import views

urlpatterns = [
    path('names', views.index,name = 'index'),
    path('documents/<str:name>/<str:house>/', views.documents,name = 'docs'),
    path("logout",views.logout,name="logout"),
    path('base', views.base,name = 'base'),

    
    
]
