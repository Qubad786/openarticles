import re

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.base import View

from web.accounts.models import UserRole
from web.articles.models import Article, ArticleStatus


class ArticleView(View):

    def get(self, request, article_id):

        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404

        ctx = dict(
            article=article,
            is_article_open=article.status == ArticleStatus.OPEN,
            is_article_in_review=article.status == ArticleStatus.FOR_REVIEW,
            has_approve_access=request.user.role == UserRole.EDITOR
        )

        return render(request, template_name='articles/article.html', context=ctx)

    def post(self, request, article_id):

        help_text = (
            'Link to Google Docs can only indicate the completion of this article '
            'and it will lead to further review of this article.'
        )

        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404

        article.content = request.POST['content']
        docs_link = request.POST['docs_link']
        if 'docs.google.com' in docs_link:
            article.docs_link = docs_link
            article.status = ArticleStatus.FOR_REVIEW
            article.assigned_to = request.user
            help_text = 'Article has been sent for further review.'
        else:
            help_text = 'Article has been saved as draft.'

        article.save()

        ctx = dict(
            article=article,
            is_article_open=article.status == ArticleStatus.OPEN,
            is_article_in_review=article.status == ArticleStatus.FOR_REVIEW,
            has_approve_access=request.user.role == UserRole.EDITOR,
            help_text=help_text
        )

        return render(request, template_name='articles/article.html', context=ctx)


class ArticleApprovalView(View):

    def post(self, request, article_id):

        if not (request.user.role == UserRole.EDITOR or request.user.is_superuser):
            return HttpResponseForbidden()

        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404

        article.approved_by = request.user
        article.status = ArticleStatus.APPROVED
        article.save()

        ctx = dict(
            article=article,
            is_article_open=article.status == ArticleStatus.OPEN,
            is_article_in_review=article.status == ArticleStatus.FOR_REVIEW,
            has_approve_access=request.user.role == UserRole.EDITOR
        )

        return render(request, template_name='articles/article.html', context=ctx)
