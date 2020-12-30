from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Sondage Admin"
admin.site.site_title = "Sondage Admin zone"
admin.site.index_title = "Bienvenue a l'administration"



admin.site.register(Question)
admin.site.register(Choice)
