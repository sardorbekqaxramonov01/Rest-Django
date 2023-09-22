from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import *
from .serializers import TodoSerializers

class ListTodos(ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializers
class DetailTodos(RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializers