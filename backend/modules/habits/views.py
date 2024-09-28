from django.utils import timezone
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.habits.models import Habit, Day, TaskForDay
from modules.habits.serializers import (
    HabitSerializer,
    DaySerializer,
    TaskForDaySerializer,
)


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CurrentDay(APIView):

    def get(self, request):

        current_day, created = Day.objects.get_or_create(
            user=request.user, date=timezone.now().date()
        )

        instance = DaySerializer(current_day)
        return Response(instance.data)


class TaskRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = TaskForDaySerializer

    def get_queryset(self):
        return TaskForDay.objects.filter(day__user=self.request.user)
