from django.contrib import admin

from .models import Choice, Question


class ChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Choice, ChoiceAdmin)


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
