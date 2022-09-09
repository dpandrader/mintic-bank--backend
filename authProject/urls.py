from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp.views.usercreateview import UserCreateView
from authApp.views.userdetailview import UserDetailView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('create_user/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    
]
