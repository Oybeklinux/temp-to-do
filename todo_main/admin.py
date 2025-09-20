from django.contrib import admin
from .models import Tasks

class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "is_done", "created_at"]
    list_filter = ["is_done"]
# Register your models here.

admin.site.register(Tasks, TaskAdmin)