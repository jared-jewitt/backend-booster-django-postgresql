from django.contrib import admin

from src.v1.models.user import User
from src.v1.models.post import Post


class UserAdmin(admin.ModelAdmin):
    fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    fields = "__all__"


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
