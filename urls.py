from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'task_manager.views.home'),
                       url(r'^login/', TemplateView.as_view(template_name='index.html')),
                       url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'task_manager.handlers.handle404'
