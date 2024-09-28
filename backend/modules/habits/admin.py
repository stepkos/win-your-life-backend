from django.contrib import admin
from modules.habits.models import Habit, Day, TaskForDay


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = "user", "content", "updated_at"


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = "user", "date", "updated_at"


@admin.register(TaskForDay)
class TaskForDayAdmin(admin.ModelAdmin):
    list_display = "day", "is_done", "content", "updated_at"
    list_filter = "is_done", "day"
    search_fields = "content", "day"
