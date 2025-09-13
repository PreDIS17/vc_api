from django.contrib import admin
from .models import User, Theme, Post, Comment, ReactionType, Reaction

admin.site.register(User)
 
@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title','username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','theme','status','date_posted','views')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','parent','published_date')

@admin.register(ReactionType)
class ReactionTypeAdmin(admin.ModelAdmin):
    list_display = ('title','identifier')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user','reaction_type','type','content_type','object_id')
