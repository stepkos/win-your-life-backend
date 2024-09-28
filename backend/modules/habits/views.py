from django.utils import timezone
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.habits.models import Habit, Day, TaskForDay
from modules.habits.serializers import HabitSerializer, DaySerializer, TaskForDaySerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CurrentDay(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):

        current_day = Day.objects.filter(
            user=request.user,
            date=timezone.now().date()
        )

        instance = DaySerializer(current_day)
        return Response(instance.data)