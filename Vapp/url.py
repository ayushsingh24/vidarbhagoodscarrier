from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    path('booking/', views.book,name="booking"),
    path('owner/', views.owner,name="owner"),

]