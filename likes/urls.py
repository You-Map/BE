from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/<int:id>/', views.LikeCreateDeleteTmp.as_view(), name='likes'),
]
