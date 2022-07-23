from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Task
from .serializers import TaskSerializer
from api import serializers

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Task List': '/task-list/',
        'Detail View': '/task-detail/pk',
        'Create Task': '/task-create/',
        'Update Task': '/task-update/pk',
        'Delete Task': '/task-delete/pk',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item was Deleted')
