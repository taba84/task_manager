from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'task_manager.views.home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^testing/$', 'task_manager.views.testing'),
                       url(r'^logout/$', 'task_manager.views.logout_view')
)

handler404 = 'task_manager.handlers.handle404'
