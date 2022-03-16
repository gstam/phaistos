"""phaistos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_registration.backends.one_step.views import RegistrationView
from main.views import MainPageView
from users.forms import CustomUserForm

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),  # set as default view
    path('admin/', admin.site.urls),
    path('accounts/register', RegistrationView.as_view(form_class=CustomUserForm, success_url="/"), name="django_registration_register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('employees/', include('employees.urls')),
    path('leaves/', include('leaves.urls')),
    path('api/', include('api.urls'))
]

# make gunicorn serve static files as well (in staging, production, etc)
urlpatterns += staticfiles_urlpatterns()