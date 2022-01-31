from api.models import Follow, User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_filter = ('username', 'email')


admin.site.register(Follow)
admin.site.register(User, UserAdmin)
