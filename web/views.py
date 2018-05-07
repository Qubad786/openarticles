from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic.base import View

from web.accounts.forms import SignInForm
from web.articles.models import Article


class IndexView(View):
    """
    Index view for PTW application
    """
    template_name = 'web/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            response = render(request, template_name='web/articles.html', context=dict(articles=Article.objects.all()))
        else:
            response = render(request, self.template_name, context=dict(form=SignInForm()))

        return response

    def post(self, request):
        form = SignInForm(request.POST)
        # for the validations to trigger.
        if not form.is_valid():
            return render(request, self.template_name, context=dict(form=form))

        account = authenticate(
            unique_data={'username': request.POST['username']},
            password=request.POST['password']
        )

        if account is not None:
            # That's the case when an account has been deactivated through admin portal.
            if not account.is_active:
                response = render(
                    request,
                    template_name=self.template_name,
                    context=dict(form=form, errors='Account has been deactivated.')
                )
            else:
                login(request, account)
                response = render(
                    request,
                    template_name='web/articles.html',
                    context=dict(articles=Article.objects.all())
                )
        else:
            response = render(
                request,
                template_name=self.template_name,
                context=dict(form=form, errors='Username or password is invalid.')
            )

        return response
