from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase

from project_manager.models import Project, Position, TaskType, Task, Worker


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_test_password = "test1234"
        cls.position1 = Position.objects.create(name="Python Developer")
        cls.position2 = Position.objects.create(name="QA")

        cls.user_test = get_user_model().objects.create_user(
            username="test566",
            password=cls.user_test_password,
            first_name="test_first",
            last_name="test_last",
            position=cls.position1,
        )

        cls.tasktype1 = TaskType.objects.create(name="Bug")
        cls.tasktype2 = TaskType.objects.create(name="New feature")

        worker1 = Worker.objects.create(
            username="test111", password="1234test", position=cls.position1
        )
        worker2 = Worker.objects.create(
            username="test222", password="4321test", position=cls.position2
        )

        cls.task1 = Task.objects.create(
            name="chat_develop", task_type=cls.tasktype1, deadline=date.today()
        )
        cls.task1.assigness.add(worker1)
        cls.task2 = Task.objects.create(
            name="Refactoring", task_type=cls.tasktype2, deadline=date.today()
        )
        cls.task2.assigness.add(worker2)

        cls.project1 = Project.objects.create(name="Something interesting", tasks=cls.task1, deadline=date.today())
        cls.project1.assigness.add(worker1)

        return super().setUpTestData()

    def test_position_model(self):
        self.assertEqual(str(self.position1), self.position1.name)

    def test_task_type_model(self):
        self.assertEqual(str(self.tasktype1), self.tasktype1.name)

    def test_worker_model(self):
        self.assertEqual(
            str(self.user_test), f"{self.user_test.username} {self.user_test.position}"
        )
        self.assertTrue(self.user_test.check_password(self.user_test_password))

    def test_task_model(self):
        self.assertEqual(str(self.task1), f"{self.task1.name} {self.task1.priority}")

    def test_project_model(self):
        self.assertEqual(str(self.project1), f"{self.project1.name} {self.project1.deadline}")
