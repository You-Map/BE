from django.urls import path
from .views import UserView, RegisterUserView, LoginView, LogoutView

urlpatterns = [
    path('user/', UserView.as_view(), name='user'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
]