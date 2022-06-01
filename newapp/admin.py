from django.contrib import admin

from .models import Authors, Books, Tegs

class Authorsadmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name')

class Booksadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'time_create', 'time_update')

admin.site.register(Authors, Authorsadmin)
admin.site.register(Books, Booksadmin)
admin.site.register(Tegs)