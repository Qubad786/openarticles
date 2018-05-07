from django.contrib import admin

from web.articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    Admin for Article data model.
    """
    list_display = ('headline', 'content', 'status')

    model = Article

    verbose_name = 'Article'
    verbose_name_plural = 'Articles'


admin.site.register(Article, ArticleAdmin)
