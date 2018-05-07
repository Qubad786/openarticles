from django.db import models


class ArticleStatus(object):
    FOR_REVIEW = 'for-review'
    APPROVED = 'approved'
    OPEN = 'open'

    CHOICES = (
        (FOR_REVIEW, 'For-review'),
        (APPROVED, 'Approved'),
        (OPEN, 'Open'),
    )


class Article(models.Model):
    assigned_to = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='assigned_articles'
    )
    approved_by = models.ForeignKey(
        'accounts.User',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='approved_articles'
    )
    headline = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=50, choices=ArticleStatus.CHOICES)