from django.urls import path

from todolist_app.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]