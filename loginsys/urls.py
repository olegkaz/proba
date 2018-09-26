from django.urls import path, re_path, include
from loginsys import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
]
