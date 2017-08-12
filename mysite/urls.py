"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# from mysite.views import hello, current_datetime, hours_ahead, \
#                             current_datetime2, current_datetime3, \
#                             current_datetime4, hours_ahead2
from mysite import views
import books.views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    # url(r'^time/$', current_datetime),
    # url(r'^time/$', current_datetime2),
    # url(r'^time/$', current_datetime3),
    url(r'^time/$', views.current_datetime4),
    # url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead2),
    url(r'^books/$', books.views.book_list),

    # url(r'^search_form/$', books.views.search_form),
    # url(r'^search/$', books.views.search),
    url(r'^search/$', books.views.search2),
]
