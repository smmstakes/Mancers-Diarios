from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Diario

class DiarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','titulo', 'data')
    list_filter = ('data', 'usuario')

admin.site.register(Diario, DiarioAdmin)
admin.site.unregister(Group)

