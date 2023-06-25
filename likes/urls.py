from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/<int:id>/', views.LikeCreateDeleteTmp.as_view(), name='likes'),
    # path('', views.LikeCreateDelete.as_view({'get':'retrieve', 'delete':'destroy','post':'create'}), name='likes'), 
    # path('', views.LikeCreateDelete.as_view(), name='likes'), 
]
