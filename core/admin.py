from django.contrib import admin
from .models import *


class ModuloInline(admin.TabularInline):
    model = Modulo
    extra = 0


class CursoAdmin(admin.ModelAdmin):
    inlines = [ModuloInline]


admin.site.register(Curso, CursoAdmin)
admin.site.register(FaqGeral)
admin.site.register(Feedbacks)