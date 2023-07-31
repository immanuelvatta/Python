from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('<str:name>', views.hello_name),
    path('test/', views.test),
    path('bears', views.example_method),                        # would only match localhost:8000/bears
    path('bears/<int:my_val>', views.example_method_two),       # would match localhost:8000/bears/23
    path('bears/<str:name>/poke', views.example_method_three),  # would match localhost:8000/bears/pooh/poke
    path('<int:id>/<str:color>', views.one_more),               # would match localhost:8000/17/brown
    path('another_route', views.another_method),
    path("redirected_route", views.redirected_method),
]
