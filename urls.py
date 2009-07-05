from django.conf.urls.defaults import *

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
    (r'^edit/$', 'pydjangitwiki.wiki.views.edit'),
    (r'^root$', 'pydjangitwiki.wiki.views.index'),
    #what was this one for?
    #(r'^/$', 'pydjangitwiki.wiki.views.index'),
    #(r'^/([^/?&#.]+)\.css$', # /:style.css
    (r'^commit/([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.views.indexviewcommit'), # commit/:sha
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/archive$', 'pydjangitwiki.wiki.views.archive'), # /?:path?/archive #make zip file
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/history$', 'pydjangitwiki.wiki.views.history'), # /?:path?/history
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/diff$', 'pydjangitwiki.wiki.views.diff'), # /?:path?/diff
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/edit$', 'pydjangitwiki.wiki.views.edit'), # /:path/edit
    (r'^/([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'pydjangitwiki.wiki.views.upload'), # /:path/upload
    (r'^new$', 'pydjangitwiki.wiki.views.new'), # /new
    (r'^upload$', 'pydjangitwiki.wiki.views.upload'), # /upload
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/new$', 'pydjangitwiki.wiki.views.new'), # /:path/new
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'pydjangitwiki.wiki.views.upload'), # /:path/upload
    (r'^([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.views.indexviewcommit'), # /:sha
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.views.viewcommit_for_file'), # /:path/:sha
    (r'^changelog\.rss$', 'pydjangitwiki.wiki.views.changelog'), # /changelog.rss
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/changelog\.rss$', 'pydjangitwiki.wiki.views.changelog_for_file'), # /:path/changelog.rss
    #the catch-all
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)$', 'pydjangitwiki.wiki.views.view'), # /:path
)
