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
    url(r'^viewcomplaints/','foundation.views.viewcomplaints'),
    url(r'^leaderboard/', 'authentication.views.leaderboard'),
    url(r'^$','authentication.views.index'),
    url(r'^drivenav/index/','drivenav.views.index'),
    url(r'^drivenav/issues/','drivenav.views.issues'),
    url(r'^drivenav/route/(?P<issue_id>\d+)/$','drivenav.views.route',name = 'route'),
    url(r'^drivenav/testjson/','drivenav.views.test'),
    url(r'^chat/bot/','foundation.views.chatbot'),
    url(r'^livechatbot','foundation.views.livechatbot'),
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