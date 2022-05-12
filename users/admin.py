from django.contrib import admin
from .models import CustomUser
# Register your models here.

class AdminCustomUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

admin.site.register(CustomUser,AdminCustomUser)