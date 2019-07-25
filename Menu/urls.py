from django.urls import path
from Menu import views

urlpatterns = [
    path('main/',views.main, name='main'),
]
