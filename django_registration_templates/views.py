from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'


class AccountProfile(TemplateView):
    template_name = 'account_profile.html'
