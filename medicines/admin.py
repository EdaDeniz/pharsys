from django.contrib import admin
from .models import Medicine
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'medicine_code', 'medicine_price')


admin.site.register(Medicine, AuthorAdmin)

