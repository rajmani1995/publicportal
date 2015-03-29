from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'publicportal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^login/','authentication.views._loginpage'),
    url(r'^logout/','authentication.views._logout'),
    url(r'^loginuser/','authentication.views._login'),
    url(r'^signup/','authentication.views.signup'),
    url(r'^dashboard/','authentication.views.dashboard'),
    url(r'^complain/','foundation.views.complain'),
    url(r'^sendposition/','foundation.views.sendposition'),
    url(r'^viewcomplaints/','foundation.views.viewcomplaints'),
    url(r'^$','authentication.views.index'),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)