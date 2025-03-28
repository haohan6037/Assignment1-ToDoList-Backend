
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task


class SystemViewTest(TestCase):
    def test_full_system(self):
        print("1. register start")
        # mock user
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, 201)  # 201 created
        # get user instance
        self.user = User.objects.get(username='newuser')

        # check if user is created
        self.assertTrue(User.objects.filter(username='newuser').exists())
        print("1. register testing finish " + self.user.username)

        print("2. login testing start")
        # 登录获取token
        response = self.client.post('/api/login/', {'username': 'newuser', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 200)
        # 假设返回token
        self.token = response.json()['token']
        self.assertIsNotNone(self.token)
        print("2. login testing finish " + self.token)


        print("3. view user testing start")
        response = self.client.get('/api/user/', HTTP_AUTHORIZATION='Token ' + self.token)
        # response = self.client.get('/api/user/')
        self.assertEqual(response.status_code, 200)
        print("3. user testing finish"+response.json()['username'])

#     @pytest.mark.run(order=5)
    #     def test_logout_view(self):
    #         print("4.logout testing start")
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
#         response = self.client.get('/api/logout/')
#         self.assertEqual(response.status_code, 200)
#         print("4.logout testing finish")


        print("5. delete user start")
        # delete user clean up
        self.user.delete()
        print("5. delete user finish")


class TaskModelTest(TestCase):
    def test_create_task(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        task = Task.objects.create(title="Test Task", description="desc", status="todo", user=user)
        self.assertEqual(task.title, "Test Task")
        print("6. create task testing finish")
