from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login$', LoginView.as_view(template_name="login/login_form.html"), name='dashboard_login'),
    url(r'^logout$', LogoutView.as_view(), name='dashboard_logout'),
]