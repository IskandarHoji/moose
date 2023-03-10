from django.contrib import admin
from .models import Blog, Contact

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','is_published')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','created_at','is_solved')

admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact,ContactAdmin)

