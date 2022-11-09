from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class TransactionAdmin(admin.StackedInline):
    model = Transaction
    extra = 0


class ProfileLine(admin.ModelAdmin):
    inlines = [TransactionAdmin]


admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileLine)


