from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()

# router.register(r'list', PostViewSet)

urlpatterns=[
    path('list-all/', PostListAllAPIView.as_view()),
    path('list-certified/', PostListCertifiedAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
    path('retrieve/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('update<int:pk>/', PostUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', PostDestroyAPIView.as_view()),
]