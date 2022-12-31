from django.contrib import admin
from .models import Post,Comment, Reply

# Register your models here.
class ReplysInline(admin.TabularInline):
    """
    Used to show 'existing' Comment replys inline below associated comment
    """
    model = Reply
    max_num=0

class CommentsInline(admin.TabularInline):
    """
    Used to show 'existing' Post comments inline below associated Posts
    """
    model = Comment
    max_num=0
    list_display = ('user','description')
    inlines = [ReplysInline]
    
class PostAdmin(admin.ModelAdmin):
    """Administration object for Post models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of Post instances in Post view (inlines)
    """
    list_display = ('title', 'user', 'date')
    list_filter = ('date','user')
    inlines = [CommentsInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)

