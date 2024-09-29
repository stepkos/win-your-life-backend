from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modules.habits.views import HabitViewSet, CurrentDay, TaskRetrieveUpdateAPIView, ArchiveDayList

router = DefaultRouter()
router.register("habits", HabitViewSet, basename="habits")

urlpatterns = [
    path("", include(router.urls), name="habits"),
    path("current_day/", CurrentDay.as_view(), name="current_day"),
    path("tasks/<str:pk>/", TaskRetrieveUpdateAPIView.as_view(), name="task"),
    path("archive_days/", ArchiveDayList.as_view(), name="archive_days"),
]
