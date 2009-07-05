# Create your views here.
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from wiki.models import *
from git import *
import os.path
from django.conf import settings

#def about_pages(request, page):
#    try:
#        return direct_to_template(request, template="about/%s.html" % page)
#    except TemplateDoesNotExist:
#        raise Http404()

def index(request):
    repo = Repo(settings.REPO_DIR)
    commits = repo.commits('master', max_count=100)
    head = commits[0]
    files = head.tree.items()
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
    return render_to_response("changelog.rss", locals())

def view(request,path=""):
    return render_to_response("view.html", locals())

def render(request, file="", filename=""):
    if not filename and not (file == ""):
        if (file.rfind("css") > 0):
            return render_to_response(file,locals(),mimetype="text/css")
        elif (file.rfind("js") > 0):
            return render_to_response(file,locals(),mimetype="text/js")
    elif not filename == "":
        fp = open(os.path.join(os.path.realpath(os.path.curdir),("templates/pydjangitwiki-static/static/images/%s.png" % (filename))))
        blah = fp.read()
        return HttpResponse(blah,mimetype="image/png")
