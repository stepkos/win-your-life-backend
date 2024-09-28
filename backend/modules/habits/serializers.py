from rest_framework import serializers
from modules.habits.models import Habit, Day, TaskForDay


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["id", "content", "updated_at"]


class TaskForDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskForDay
        fields = ["id", "content", "is_done"]


class DaySerializer(serializers.ModelSerializer):
    tasks = TaskForDaySerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ["id", "date", "tasks"]
