from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

                       
    url(r'^regi/$','log.views.regist'),
    url(r'^login/$','log.views.login'),
    url(r'^index/$','log.views.index'),
    url(r'^logout/$','log.views.logout'),
    url(r'^person/$','log.views.center'),
    url(r'^news/newslist/$','news.views.news_list'),
    url(r'^news/(?P<id>\d+)/$','news.views.news_show'),
    url(r'^news/tag/(?P<id>\d+)/$','news.views.news_filter'),
    url(r'^contact/$','contact.views.contact'),
    url(r'^contact/thanks/$','contact.views.thanks'),
    #url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),                     
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
