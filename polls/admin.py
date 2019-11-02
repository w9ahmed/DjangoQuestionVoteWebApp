from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

# admin.site.register([models.Question, models.Choice])
