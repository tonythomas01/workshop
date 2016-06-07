from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from register import views
from register.views import *
from register.models import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),
        name='user_registration_success'),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='profile_edit'),
    url(r'^user/profile/view/$', UserProfileView.as_view(), name='profile_view'),
    url( r'^chocolate/add/', AddChocolateView.as_view(), name="add_chocolate"),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info")
]
