# Create your views here.
from django.http import HttpResponse
from wiki.models import *
from git import *

def index(request):
    returnstring = "this is the index"
    return HttpResponse(returnstring)
def edit(request, path=""):
    returnstring = "edit"
    return HttpResponse(returnstring)
def indexviewcommit(request,sha=""):
    returnstring = "indexviewcommit"
    return HttpResponse(returnstring)
def archive(request,path=""):
    returnstring = "archive"
    return HttpResponse(returnstring)
def history(request,path=""):
    returnstring = "history"
    return HttpResponse(returnstring)
def diff(request, path=""):
    returnstring = "diff"
    return HttpResponse(returnstring)
def upload(request, path=""):
    returnstring = "upload"
    return HttpResponse(returnstring)
def new(request,path=""):
    returnstring = "new"
    return HttpResponse(returnstring)
def viewcommit_for_file(request,path="",sha=""):
    returnstring = "viewcommit_for_file"
    return HttpResponse(returnstring)
def changelog(request):
    returnstring = "changelog"
    return HttpResponse(returnstring)
def changelog_for_file(request,path=""):
    returnstring = "changelog_for_file"
    return HttpResponse(returnstring)
def view(request,path=""):
    returnstring = "view"
    return HttpResponse(returnstring)
