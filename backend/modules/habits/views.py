from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from modules.habits.models import Habit
from modules.habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
