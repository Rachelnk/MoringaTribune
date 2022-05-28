from django.contrib import admin
from django.test import tag
from . models import Article, Editor , tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Editor)
admin.site.register(tags)