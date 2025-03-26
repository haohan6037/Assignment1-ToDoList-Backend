from django.urls import path
from rest_framework import routers

from todolist_app.views import *

router = routers.DefaultRouter()
# router.register('notes', TaskViewSet, basename='notes')
urlpatterns = router.urls
urlpatterns.append(path('register/', RegisterView.as_view(), name='register'))
urlpatterns.append(path('login/', LoginView.as_view(), name='login'))
urlpatterns.append(path('logout/', LogoutView.as_view(), name='logout'))
urlpatterns.append(path('user/', UserView.as_view(), name='user'))
