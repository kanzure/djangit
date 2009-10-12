from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import djangit.wiki
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djangit/', include('djangit.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #some extra notes
    #browse to /polls/23/ 
    # (r'^polls/(?P<poll_id>\d+)/$', 'mysite.polls.views.detail')
    # detail(request=<HttpRequest object>, poll_id=23)
    #for more information, see:
    #http://docs.djangoproject.com/en/dev/topics/http/urls/

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    #login/signup stuff not included here
    #also user profile stuff not included here
    #do CSS/JS first
    (r'^djangit-static/static/images/(?P<filename>[A-Za-z]*)\.png$', 'djangit.wiki.views.render', {'file':""}),
    (r'^djangit-static/screen.css$', 'djangit.wiki.views.render', {'file':"djangit-static/screen.css"}),
    (r'^djangit-static/print.css$', 'djangit.wiki.views.render', {'file':"djangit-static/print.css"}),
    (r'^djangit-static/reset.css$', 'djangit.wiki.views.render', {'file':"djangit-static/reset.css"}),
    (r'^djangit-static/static/highlight.css$', 'djangit.wiki.views.render', {'file':"djangit-static/static/highlight.css"}),
    (r'^djangit-static/static/script/jquery/jquery-1.3.1.js$', 'djangit.wiki.views.render', {'file':"djangit-static/static/script/jquery/jquery-1.3.1.js"}),
    (r'^djangit-static/static/script/jquery/ui.core.js$', 'djangit.wiki.views.render', {'file':"djangit-static/static/script/jquery/ui.core.js"}),
    (r'^djangit-static/static/script/jquery/ui.tabs.js$', 'djangit.wiki.views.render', {'file':"djangit-static/static/script/jquery/ui.tabs.js"}),
    (r'^djangit-static/static/script/jquery/tablesorter.js$', 'djangit.wiki.views.render', {'file':"djangit-static/static/script/jquery/tablesorter.js"}),
    (r'^djangit-static/static/script/app.js$', 'djangit.wiki.views.render', {'file':"djangit-static/static/script/app.js"}),
    (r'^edit/$', 'djangit.wiki.views.edit'),
    (r'^root$', 'djangit.wiki.views.index'),
    (r'^$', 'djangit.wiki.views.index'),
    #(r'^/([^/?&#.]+)\.css$', # /:style.css
    (r'^commit/([A-Fa-f0-9]{5,40})$', 'djangit.wiki.views.index'), # commit/:sha
    (r'^new$', 'djangit.wiki.views.new'), # /new
    (r'^upload$', 'djangit.wiki.views.upload'), # /upload
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/archive$', 'djangit.wiki.views.archive'), # /?:path?/archive #make zip file
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/history$', 'djangit.wiki.views.history'), # /?:path?/history
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/diff$', 'djangit.wiki.views.diff'), # /?:path?/diff
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/edit$', 'djangit.wiki.views.edit'), # /:path/edit
    (r'^/([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'djangit.wiki.views.upload'), # /:path/upload
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/new$', 'djangit.wiki.views.new'), # /:path/new
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'djangit.wiki.views.upload'), # /:path/upload
    (r'^([A-Fa-f0-9]{5,40})$', 'djangit.wiki.views.index'), # /:sha
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/([A-Fa-f0-9]{5,40})$', 'djangit.wiki.views.view'), # /:path/:sha
    (r'^changelog\.rss$', 'djangit.wiki.views.changelog'), # /changelog.rss
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/changelog\.rss$', 'djangit.wiki.views.changelog'), # /:path/changelog.rss
    #the catch-all
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)$', 'djangit.wiki.views.view'), # /:path
)
