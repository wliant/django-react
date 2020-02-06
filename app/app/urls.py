from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from url_checker.views import check_url, FrontendAppView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('url_checker', check_url),
    url(r'^', FrontendAppView.as_view())
]