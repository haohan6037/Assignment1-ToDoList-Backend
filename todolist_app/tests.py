from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        task = Task.objects.create(title="Test Task", description="desc", status="todo", user=user)
        self.assertEqual(task.title, "Test Task")