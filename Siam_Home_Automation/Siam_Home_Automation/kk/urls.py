from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'kk.web.views.home', name='home'),
    url(r'^rooms/$', 'kk.web.views.rooms', name='users'),
    url(r'^rooms/create/$', 'kk.web.views.create_room', name='create_room'),
    url(r'^users/$', 'kk.web.views.users', name='users'),
    url(r'^users/create/$', 'kk.web.views.create_user', name='create_user'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
