from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view
def apiOverview(request):
    api_urls = {
        'Task List': '/task-list/',
        'Detail View': '/task-detail/',
        'Update Task': '/task-update/',
        'Create Task': '/task-create/',
        'Delete Task': '/task-delete/',
    }
    return Response(api_urls)
