from django.contrib import admin
from .models import Patient
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')


admin.site.register(Patient, AuthorAdmin)

