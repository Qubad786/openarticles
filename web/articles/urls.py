from django.urls import path
from django.contrib.auth.decorators import login_required


from web.articles.views import ArticleView, ArticleApprovalView

urlpatterns = [
    path('single/<int:article_id>/', login_required(ArticleView.as_view()), name='article_details'),
    path('<int:article_id>/update/', login_required(ArticleView.as_view()), name='update_article'),
    path('<int:article_id>/approve/', login_required(ArticleApprovalView.as_view()), name='approve_article')
]

