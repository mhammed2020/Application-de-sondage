from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Sondage Admin"
admin.site.site_title = "Sondage Admin zone"
admin.site.index_title = "Bienvenue a l'administration"



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)