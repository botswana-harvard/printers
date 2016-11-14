from django.conf.urls import url, include
from django.contrib import admin

from edc_base.views import LoginView, LogoutView

from edc_printers.views import HomeView


urlpatterns = [
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    url(r'^admin/', admin.site.urls),
    url(r'^edc/', include('edc_base.urls', namespace='edc-base')),
    url(r'^', HomeView.as_view(), name='home_url'),
]
