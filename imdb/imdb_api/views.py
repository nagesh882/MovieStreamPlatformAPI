from django.shortcuts import render, HttpResponse
from .models import StreamPlatform, WatchList, Review
from .serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watchlist': reverse('movie-list', request=request, format=format),
        'streamplatform': reverse('stream-platform', request=request, format=format),
        'reviewlist': reverse('review-list', request=request, format=format)
    })


@api_view(['GET', 'POST'])
def movie_list(request, format=None):
    if request.method == "GET":
        movie_list = WatchList.objects.all()
        serializer = WatchListSerializer(movie_list, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data has been created !!!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_detail(request, pk, format=None):
    try:
        movie_platform = WatchList.objects.get(pk=pk)
    except movie_platform.ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WatchListSerializer(movie_platform, context={'request':request})
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = WatchListSerializer(movie_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data completely Updated !!!'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = WatchListSerializer(movie_platform, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Partially Updated !!!'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        movie_platform.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def stream_list(request, format=None):
    if request.method == "GET":
        stream_list = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stream_list, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data has been created !!!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def stream_detail(request, pk, format=None):
    try:
        stream_platform = StreamPlatform.objects.get(pk=pk)
    except stream_platform.ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StreamPlatformSerializer(stream_platform, context={'request':request})
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data completely Updated !!!'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = StreamPlatformSerializer(stream_platform, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Partially Updated !!!'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        stream_platform.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    


class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
