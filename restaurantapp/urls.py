from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginpage/', views.loginPage, name='loginpage'),
    path('registerpage/', views.registerPage, name='registerpage'),
    path('logoutpage/', views.logoutPage, name='logoutpage'),
    path('detail/<int:id>/', views.cuisineDetail, name='detail'),

]
