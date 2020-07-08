from django.contrib import admin
from .models import Post

admin.site.register(Post)


class PatientAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'created_date']

    class Meta:
        model = Post
