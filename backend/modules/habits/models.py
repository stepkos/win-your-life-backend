from django.db import models

from modules.authentication.models import CustomUser
from modules.core.models import BaseModel


class Habit(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class Day(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.date}"

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)

        if is_new:
            for habit in Habit.objects.filter(user=self.user):
                TaskForDay.objects.create(day=self, content=habit.content)


class TaskForDay(BaseModel):
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name="tasks")
    is_done = models.BooleanField(default=False)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.day} - {self.content}"
