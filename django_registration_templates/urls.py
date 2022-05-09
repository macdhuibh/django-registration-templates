from django.urls import path
from django_registration_templates import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('accounts/profile/', views.AccountProfile.as_view(), name='account_profile'),
]
