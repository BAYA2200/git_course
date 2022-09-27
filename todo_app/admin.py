from django.contrib import admin
from .models import Todo
admin.site.register(Todo)
# Register your models here

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)