from django.db import models

from modules.core.models import BaseModel

from django.contrib.auth.models import User


class Habit(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class Day(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.date}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.save()
            for habit in Habit.objects.filter(user=self.user):
                TaskForDay.objects.create(day=self, content=habit.content)

        super().save(*args, **kwargs)


class TaskForDay(BaseModel):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.day} - {self.content}"
