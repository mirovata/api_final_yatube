from django.contrib import admin

from posts.models import Comment, Group, Post, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'description')
    search_fields = ('description',)
    list_filter = ('slug',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'created')
    search_fields = ('author__username',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_diplay = ('user', 'following')


admin.site.empty_value_display = 'Не задано'
