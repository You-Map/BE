from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from likes.serializers import LikeSerializer
from likes.models import Like
from posts.models import Post
from django.contrib.auth import get_user_model

# Create your views here

class LikeCreateDeleteTmp(generics.CreateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.kwargs['id'])
        post = Post.objects.get(pk=self.kwargs['pk'])

        print(user)
        print(post)
        
        return Like.objects.filter(user=user, post=post)

    def retrieve(self, request, *args, **kwargs):
        try: 
            post = Post.objects.get(pk=self.kwargs['pk'])
            if self.get_queryset().exists():
                return Response(data={'like': True}, status=status.HTTP_200_OK)
            else:
                return Response(data={'like': False}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(data={'like': False}, status=status.HTTP_200_OK)

        # instance = self.get_object()
        # serializer = self.get_serializer(instance)
        # return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Toggle 'like'
        # Update 'likes' on the related post
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post = Post.objects.get(pk=self.kwargs['pk'])
        if self.get_queryset().exists():
            self.get_queryset().delete()
            post.likes -= 1
            post.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer.save(user=get_user_model().objects.get(id=self.kwargs['id']), post=Post.objects.get(pk=self.kwargs['pk']))
        
        post.likes += 1
        post.save()
        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        if self.get_queryset().exists():
            self.get_queryset().delete()
            post.likes -= 1
            post.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)