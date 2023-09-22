from django.urls import path
from .views import ListTodos, DetailTodos

urlpatterns = [
    path('<int:pk>', DetailTodos.as_view()),
    path('', ListTodos.as_view()),

]
