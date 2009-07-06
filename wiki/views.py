# Create your views here.
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from wiki.models import *
import git
import os.path
from django.conf import settings

#def about_pages(request, page):
#    try:
#        return direct_to_template(request, template="about/%s.html" % page)
#    except TemplateDoesNotExist:
#        raise Http404()

# TODO: download a single page (not in a compressed archive)
# TODO: figure out how to do multiple pages (i.e., with POST or SUBMIT
# django request objects: http://docs.djangoproject.com/en/dev/ref/request-response/)

def index(request,sha=""):
    repo = git.Repo(settings.REPO_DIR)
    commits = repo.commits(start=sha or 'master', max_count=1)
    head = commits[0]
    files = head.tree.items()
    data_for_index = [] #start with nothing
    for each in files:
        toinsert = {}
        myblob = each[1]
        thecommit = myblob.blame(repo,head,myblob.basename)[0][0]
        toinsert['author'] = thecommit.committer.name
        toinsert['author_email'] = thecommit.committer.email
        toinsert['id'] = thecommit.id
        toinsert['date'] = thecommit.authored_date
        toinsert['message'] = thecommit.message
        toinsert['filename'] = myblob.basename
        data_for_index.append(toinsert)
    return render_to_response("index.html", locals())

def edit(request, path="", sha=""):
    '''
    edit a page. if there are POST variables, these will be taken as the contents of the edit.

    the "sha" named parameter is for which version of the file to edit
    TODO: proper branching support
    '''
    if request.method == 'GET':
        #display form
        pass
    elif request.method == 'POST':
        #submit modifications
        pass
    return render_to_response("edit.html", locals())

def archive(request,path="",sha=""):
    '''
    download a zip archive of the current path
    
    (the archive must have the full path (inside of it) so that it is not a tarbomb)
    '''
    repo = git.Repo(settings.REPO_DIR)
    mycommit = repo.commit(id=sha or 'master') #er, test this
    mytree = mycommit.tree()
    myitems = mytree.items()
    #now what about the path?
    #cases:
    #1) it's a file
    #2) it's a folder
    return render_to_response("archive.html", locals())

def history(request,path="",sha=""):
    '''
    return the history for a given path (commits)

    "sha" determines the latest version to show (not necessary but useful for paging, etc.)
    '''
    return render_to_response("history.html", locals())

def diff(request, path="", sha1="", sha2=""):
    '''
    display the diff between two commits (SHA strings)
    '''
    if not request.GET['show'] == True:
        #pick files to diff
    elif request.GET['show']:
        #diff view
    return render_to_response("diff.html", locals())

def upload(request, path=""):
    '''
    upload a file
    '''
    if request.method == 'GET':
        #display the form
        pass
    elif request.method == 'POST':
        #upload file
        pass
    return render_to_response("upload.html", locals())

def new(request,path="",sha=""):
    '''
    make a new file/page at the given "path"

    TODO: implement branching given the "sha" named parameter
    '''
    if request.method == 'GET':
        #show the form
        pass
    elif request.method == 'POST':
        #add content to repo
        pass
    return render_to_response("new.html", locals())

def changelog(request,path="",sha=""):
    '''
    display the RSS changelog for this path

    TODO: display the RSS changelog for all changes since sha="sha" (optional)
    '''
    return render_to_response("changelog.rss", locals())

def view(request,path="",sha=""):
    '''
    view the path/file/page at a given commit
    '''
    repo = git.Repo(settings.REPO_DIR)
    commits = repo.commits(start=sha or 'master',max_count=1)
    head = commits[0]
    files = head.tree.items()
    returncontents = ""
    for each in files:
        myblob = each[1]
        filename = myblob.name
        contents = myblob.data
        if filename == path:
            #we have a match
            returncontents = contents
            break
    return render_to_response("view.html", locals())

def render(request, file="", filename=""):
    '''
    render - meant for displaying some of the static images for the template
    
    this is a terrible hack.
    (see urls.py)
    '''
    if not filename and not (file == ""):
        if (file.rfind("css") > 0):
            return render_to_response(file,locals(),mimetype="text/css")
        elif (file.rfind("js") > 0):
            return render_to_response(file,locals(),mimetype="text/js")
    elif not filename == "":
        fp = open(os.path.join(os.path.realpath(os.path.curdir),("templates/pydjangitwiki-static/static/images/%s.png" % (filename))))
        blah = fp.read()
        return HttpResponse(blah,mimetype="image/png")
