from django.shortcuts import render
from django.http import HttpResponse
from . import stream_minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

# from django.http import JsonResponse
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.


# @api_view(["GET"])
# @csrf_exempt
# @permission_classes([])
# def welcome(request):
#     content = {"message": "Welcome to the Bookstore!"}
#     return JsonResponse(content)

def index(request):
    return HttpResponse("Home Page")

def create_bucket(request):
    
    
    my_response = "Working"
    try:
        stream_minio.createBucket("dallasbucket")
    except BucketAlreadyOwnedByYou as err:
        my_response = err.message
    except BucketAlreadyExists as err:
        my_response = err
    except ResponseError as err:
        my_response = err
    return HttpResponse(my_response)


def add_video(request):
    etag = stream_minio.addObjectTobucket(r"C:\Users\Akshay Shenvi\Downloads\Sample.mp4","dallasbucket")
    print(etag)
    return HttpResponse("Working")

def getVideo(request):
    
    obj = stream_minio.getObjectList(r"C:\Users\Akshay Shenvi\Downloads\Sample.mp4", "dallasbucket")
   
    return HttpResponse(obj)