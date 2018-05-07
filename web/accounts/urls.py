from django.urls import path

from web.accounts.views import SignUpView, LogoutView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
