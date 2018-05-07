from django.contrib.auth import logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from web.accounts.forms import SignUpForm


class SignUpView(View):

    def get(self, request):
        return render(request=request, template_name='web/register.html', context=dict(form=SignUpForm()))

    def post(self, request):
        form = SignUpForm(request.POST)
        ctx = dict(form=form)
        if form.is_valid():
            try:
                user = form.save()
                user.set_password(request.POST['password'])
                user.is_active = True
                user.save()
                return HttpResponseRedirect(reverse('index'))
            except IntegrityError:  # violates unique constraint.
                ctx['errors'] = 'This username is not available. Please choose a different username.'

        return render(request=request, template_name='web/register.html', context=ctx)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
