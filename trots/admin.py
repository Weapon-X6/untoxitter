from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Profile, Trot


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
    list_filter = ["username"]


class TrotAdmin(admin.ModelAdmin):
    model = Trot
    list_filter = ["user"]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Trot, TrotAdmin)
