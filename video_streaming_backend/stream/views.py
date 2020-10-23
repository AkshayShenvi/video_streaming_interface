from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the Bookstore!"}
    return JsonResponse(content)