from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('results', views.results),
    path('go_back',views.go_back)
]