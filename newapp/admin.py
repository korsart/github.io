from django.contrib import admin

from .models import User, Books, Tegs

class Useradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')

class Booksadmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'time_create', 'time_update')

admin.site.register(User, Useradmin)
admin.site.register(Books, Booksadmin)
admin.site.register(Tegs)