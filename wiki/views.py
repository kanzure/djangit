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
    return render_to_response("index.html", locals())

def edit(request, path=""):
    return render_to_response("edit.html", locals())

def indexviewcommit(request,sha=""):
    return render_to_response("indexviewcommit.html", locals())

def archive(request,path=""):
    return render_to_response("archive.html", locals())

def history(request,path=""):
    return render_to_response("history.html", locals())

def diff(request, path=""):
    return render_to_response("diff.html", locals())

def upload(request, path=""):
    return render_to_response("upload.html", locals())

def new(request,path=""):
    return render_to_response("new.html", locals())

def viewcommit_for_file(request,path="",sha=""):
    return render_to_response("viewcommit_for_file.html", locals())

def changelog(request,path=""):
    returnstring = "changelog (path=%s)" % (path)
    return HttpResponse(returnstring)

def view(request,path=""):
    returnstring = "view (path=%s)" % (path)
    return HttpResponse(returnstring)
