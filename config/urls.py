from django.contrib import admin  # Correct import
from django.urls import path, include
# from accounts import *  # This line may be causing the issue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'))
]