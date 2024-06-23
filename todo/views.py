
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Todo
from todo.serializers  import TodoSerializer
from django.core import serializers
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] #permissions.IsAuthenticated kann in den klammern stehen, dann muss man eingeloggt sein

    def create(self, request):
        todo = Todo.objects.create(title= request.POST.get('title', ''), 
                                  description= request.POST.get('description', ''),
                                  user= request.user,
                                )
        serialized_obj = serializers.serialize('json', [todo, ]) 
        return HttpResponse(serialized_obj, content_type='application/json')