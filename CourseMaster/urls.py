"""CourseMaster URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin

from . import views
from Account import views as Account_views
from AddCourse import views as AddCourse_views

urlpatterns = [
    url(r'^$', views.PandingView, name='landing'),
    url(r'^index/$', views.IndexView, name='index'),

    url(r'^login/$', Account_views.LoginView, name='login'),
    url(r'^logout/$', Account_views.LogoutView, name='logout'),
    url(r'^register/$', Account_views.RegisterView, name='register'),

    url(r'^addcourse/$',AddCourse_views.AddCourseView, name='add_course'),
    url(r'^buycourse/(?P<howmany>[0-9]{1})/$', AddCourse_views.BuyCourseView, name='buy_course'),
    url(r'^delcourse/(?P<number>[0-9]{6})/$', AddCourse_views.DeleteCourseView, name='delete_course'),

    url(r'^setpsu/$', Account_views.AddPsuInfoView, name='setpsu'),

    url(r'^admin/', include(admin.site.urls)),
]
