from django.conf.urls.defaults import *
from django.shortcuts import render_to_response
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import pydjangitwiki.wiki
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pydjangitwiki/', include('pydjangitwiki.foo.urls')),

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
    (r'^pydjangitwiki-static/static/images/(?P<filename>[A-Za-z]*)\.png$', 'pydjangitwiki.wiki.views.render', {'file':""}),
    (r'^pydjangitwiki-static/screen.css$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/screen.css"}),
    (r'^pydjangitwiki-static/print.css$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/print.css"}),
    (r'^pydjangitwiki-static/reset.css$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/reset.css"}),
    (r'^pydjangitwiki-static/static/highlight.css$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/static/highlight.css"}),
    (r'^pydjangitwiki-static/static/script/jquery/jquery-1.3.1.js$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/static/script/jquery/jquery-1.3.1.js"}),
    (r'^pydjangitwiki-static/static/script/jquery/ui.core.js$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/static/script/jquery/ui.core.js"}),
    (r'^pydjangitwiki-static/static/script/jquery/ui.tabs.js$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/static/script/jquery/ui.tabs.js"}),
    (r'^pydjangitwiki-static/static/script/jquery/tablesorter.js$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/static/script/jquery/tablesorter.js"}),
    (r'^pydjangitwiki-static/static/script/app.js$', 'pydjangitwiki.wiki.views.render', {'file':"pydjangitwiki-static/static/script/app.js"}),
    (r'^edit/$', 'pydjangitwiki.wiki.views.edit'),
    (r'^root$', 'pydjangitwiki.wiki.views.index'),
    (r'^$', 'pydjangitwiki.wiki.views.index'),
    #(r'^/([^/?&#.]+)\.css$', # /:style.css
    (r'^commit/([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.views.index'), # commit/:sha
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/archive$', 'pydjangitwiki.wiki.views.archive'), # /?:path?/archive #make zip file
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/history$', 'pydjangitwiki.wiki.views.history'), # /?:path?/history
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/diff$', 'pydjangitwiki.wiki.views.diff'), # /?:path?/diff
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/edit$', 'pydjangitwiki.wiki.views.edit'), # /:path/edit
    (r'^/([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'pydjangitwiki.wiki.views.upload'), # /:path/upload
    (r'^new$', 'pydjangitwiki.wiki.views.new'), # /new
    (r'^upload$', 'pydjangitwiki.wiki.views.upload'), # /upload
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/new$', 'pydjangitwiki.wiki.views.new'), # /:path/new
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'pydjangitwiki.wiki.views.upload'), # /:path/upload
    (r'^([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.views.index'), # /:sha
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.views.viewcommit_for_file'), # /:path/:sha
    (r'^changelog\.rss$', 'pydjangitwiki.wiki.views.changelog'), # /changelog.rss
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/changelog\.rss$', 'pydjangitwiki.wiki.views.changelog'), # /:path/changelog.rss
    #the catch-all
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)$', 'pydjangitwiki.wiki.views.view'), # /:path
)
