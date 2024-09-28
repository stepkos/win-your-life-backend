from rest_framework import serializers
from modules.habits.models import Habit, Day, TaskForDay


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class TaskForDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskForDay
        fields = '__all__'
