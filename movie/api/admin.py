from django.contrib import admin
from .models import Movie, CustomUser
 
class MovieList(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'rating')
    list_filter = ('name', 'year', 'rating')
    search_fields = ('name', 'description')
    ordering = ['year']
 
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username"]
 
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Movie, MovieList)

