from django.contrib import admin

from .models import Choice, Question

@admin.register(Choice, Question)
class PollsAdmin(admin.ModelAdmin):
    pass

