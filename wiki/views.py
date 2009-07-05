# Create your views here.
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from wiki.models import *
from git import *

#def about_pages(request, page):
#    try:
#        return direct_to_template(request, template="about/%s.html" % page)
#    except TemplateDoesNotExist:
#        raise Http404()

def index(request):
    returnstring = "this is the index"
    return HttpResponse(returnstring)
def edit(request, path=""):
    returnstring = "edit (path=%s)" % (path)
    return HttpResponse(returnstring)
def indexviewcommit(request,sha=""):
    returnstring = "indexviewcommit (sha=%s)" % (sha)
    return HttpResponse(returnstring)
def archive(request,path=""):
    returnstring = "archive (path=%s)" % (path)
    return HttpResponse(returnstring)
def history(request,path=""):
    returnstring = "history (path=%s)" % (path)
    return HttpResponse(returnstring)
def diff(request, path=""):
    returnstring = "diff (path=%s)" % (path)
    return HttpResponse(returnstring)
def upload(request, path=""):
    returnstring = "upload (path=%s)" % (path)
    return HttpResponse(returnstring)
def new(request,path=""):
    returnstring = "new (path=%s)" % (path)
    return HttpResponse(returnstring)

def viewcommit_for_file(request,path="",sha=""):
    return render_to_response("viewcommit_for_file.html", locals())

def changelog(request,path=""):
    returnstring = "changelog (path=%s)" % (path)
    return HttpResponse(returnstring)
def view(request,path=""):
    returnstring = "view (path=%s)" % (path)
    return HttpResponse(returnstring)
