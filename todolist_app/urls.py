from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from todolist_app.views import *

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),  # 让所有自动生成的 REST 路由生效
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('delete_user/', DeleteUserView.as_view(), name='delete_user'),
]