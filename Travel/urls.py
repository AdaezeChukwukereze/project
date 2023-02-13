from django.urls import path
from .views import Home, Detail

urlpatterns = [
    path("",Home.as_view(), name="home"),
    path("<int:pk>/",Detail.as_view(),name= "detail"),
]