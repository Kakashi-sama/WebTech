from django.urls import path
from customer import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.login, name= 'login'),
    path('signup/',views.signup, name= 'signup'),
    path('main/',views.main,name='main'),
]
