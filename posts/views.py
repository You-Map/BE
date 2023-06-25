from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response


class PostListAllAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset=Post.objects.all()
        search_purpose = self.request.query_params.get('purpose')
        queryset = self.filter_queryset(self.get_queryset())
        if (search_purpose is not None) :
            queryset=queryset.filter(purpose=search_purpose)
        return queryset

class PostListCertifiedPurposeAPIView(generics.ListAPIView):
        queryset=Post.objects.all()
        serializer_class = PostSerializer
        
        def list(self, request, *args, **kwargs):
            search_purpose = self.request.query_params.get('purpose')
            queryset = self.filter_queryset(self.get_queryset())
            if (search_purpose is not None):
                queryset=queryset.filter(purpose=search_purpose)
                

            query_list = []
            for i in queryset:
                if i.likes >= 10 :
                    query_list.append(i)
                    
            page = self.paginate_queryset(query_list)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(query_list, many=True)
            return Response(serializer.data)
        
class PostListCertifiedLocationAPIView(generics.ListAPIView):
        queryset=Post.objects.all()
        serializer_class = PostSerializer
        
        def list(self, request, *args, **kwargs):
            search_location = self.request.query_params.get('location')
            queryset = self.filter_queryset(self.get_queryset())
            if (search_location is not None):
                queryset=queryset.filter(location=search_location)
                

            query_list = []
            for i in queryset:
                if i.likes >= 10 :
                    query_list.append(i)
                    
            page = self.paginate_queryset(query_list)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(query_list, many=True)
            return Response(serializer.data)
        
        
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer