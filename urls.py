from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
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

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    #login/signup stuff not included here
    #also user profile stuff not included here
    (r'^edit/', 'pydjangitwiki.wiki.edit'),
    (r'^root$', 'pydjangitwiki.wiki.index'),
    (r'^/$', 'pydjangitwiki.wiki.index'),
    #(r'^/([^/?&#.]+)\.css$', # /:style.css
    (r'^commit/([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.indexviewcommit'), # commit/:sha
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/archive$', 'pydjangitwiki.wiki.archive'), # /?:path?/archive #make zip file
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/history$', 'pydjangitwiki.wiki.history'), # /?:path?/history
    (r'^/?([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)?/diff$', 'pydjangitwiki.wiki.diff'), # /?:path?/diff
    (r'^/([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/edit$', 'pydjangitwiki.wiki.edit'), # /:path/edit
    (r'^/([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'pydjangitwiki.wiki.upload'), # /:path/upload
    (r'^new$', 'pydjangitwiki.wiki.new'), # /new
    (r'^upload$', 'pydjangitwiki.wiki.upload'), # /upload
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/new$', 'pydjangitwiki.wiki.new'), # /:path/new
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/upload$', 'pydjangitwiki.wiki.upload'), # /:path/upload
    (r'^([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.indexviewcommit'), # /:sha
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/([A-Fa-f0-9]{5,40})$', 'pydjangitwiki.wiki.viewcommit_for_file'), # /:path/:sha
    (r'^changelog\.rss$', 'pydjangitwiki.wiki.changelog'), # /changelog.rss
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)/changelog\.rss$', 'pydjangitwiki.wiki.changelog_for_file'), # /:path/changelog.rss
    #the catch-all
    (r'^([\w:.+\-_\/](?:[\w:.+\-_\/ ]*[\w.+\-_\/])?)$', 'pydjangitwiki.wiki.view'), # /:path
)
