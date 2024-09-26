from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone_number", "gender")
    list_display_links = ("id", "username")
    search_fields = ("username", "email", "phone_number")
    list_per_page = 5
