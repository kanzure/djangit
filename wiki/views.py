# Create your views here.
from django.http import HttpResponse
from wiki.models import *
from git import *

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
    returnstring = "viewcommit_for_file (path=%s,sha=%s)" % (path,sha)
    return HttpResponse(returnstring)
def changelog(request,path=""):
    returnstring = "changelog (path=%s)" % (path)
    return HttpResponse(returnstring)
def view(request,path=""):
    returnstring = "view (path=%s)" % (path)
    return HttpResponse(returnstring)
