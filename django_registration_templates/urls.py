from django.urls import path
from django_registration_templates import views


urlpatterns = [
    path('index_template/', views.Index.as_view(), name='index_template'),
]
