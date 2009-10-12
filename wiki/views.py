# Create your views here.
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template
import django.shortcuts #render_to_response
#import wiki.models
import git
import os.path
from django.conf import settings
import string #for path_is_file()
import copy

#def about_pages(request, page):
#    try:
#        return direct_to_template(request, template="about/%s.html" % page)
#    except TemplateDoesNotExist:
#        raise Http404()

# TODO: download a single page (not in a compressed archive)
# django request objects: http://docs.djangoproject.com/en/dev/ref/request-response/

def strip_trailing_slashes(path):
    try:
        if path[-1] == "/":
            return path[:-1]
        else: return path
    except IndexError, err:
        return path

def pop_path(path):
    '''
    if path is super/star/destroyer, then pop_path will return star/destroyer
    '''
    path2 = copy.copy(path)
    if (path2.count("/") == 0): return ""
    pieces = string.split(path2, "/")
    pieces.reverse()
    leftover = pieces.pop()
    pieces.reverse()
    if leftover == "":
        pieces.reverse()
        pieces.pop()
        pieces.reverse()
    return string.join(pieces, "/")

def pop_path_rev(path2):
    '''if path is hello/world then this would return hello'''
    path = copy.copy(path2)
    if path.count("/") == 0: return ""
    pieces = string.split(path, "/")
    pieces.reverse()
    return pieces.pop()

def path_depth(path,depth):
    '''if path is hello/world/hi and depth=1 then this would return hello, if depth=3, then this would return hi'''
    pieces = string.split(path, "/")
    if len(pieces) >= depth: return pieces[depth]
    else: return "" #error :(

def tree_handler(path_to_tree="",sha="",depth=-1,gitpath=""):
    '''return everything in this tree.'''
    if depth == 0: return {}
    if depth < -1: depth = -1
    if not gitpath: gitpath = settings.REPO_DIR
    repo = git.Repo(gitpath)
    return {} #not implemented yet

#stop = False
#while not stop:
#    path_part = pop_path_rev(path)
#    path = pop_path(path)
#    if path_part == "": stop = True
#    else:
#        #go through the list of items in this level, find the tree with the same name as the path_part

def children(path="",sha="",depth=-1,gitpath=""):
    '''
    find all trees and pages and combine them into a dict
 
    depth=-1 means infinite depth.
    '''
    if path == "" and gitpath == "": return {}
    if not gitpath: gitpath = settings.REPO_DIR
    repo = git.Repo(gitpath)
    files = repo.tree().items()
    returndict = {}
    for each in files:
        if type(each[1]) == git.tree.Tree:
            #it's a folder
            returndict = dict(returndict, **{str(each[1].name):each[1]})
            if depth<0 or depth>0:
                returndict = dict(returndict, **children(path=pop_path(copy.copy(path)),sha=sha,depth=depth-1))
        elif type(each[1]) == git.blob.Blob:
            #it's a file
            returndict = dict(returndict, **{str(each[1].name):each[1]})
    return returndict

def find(path="",sha="",depth=-1):
    #find resource in repo by path and commit SHA, return it.
    #FIXME: SHA
    if not path: path = "/"
    if path == "/":
        repo = git.Repo(settings.REPO_DIR)
        mytree = repo.tree().items()
        #mydict = mytree.__dict__["_contents"]
        #mydict.keys()
        return mytree
    objects = children(path=path,sha=sha,depth=depth)
    if objects.has_key(path):
        return objects[path]
    else:
        return False #path not found
    pass

def path_exists(path="",sha="",gitrepo=""):
    '''
    return True if the path exists
    return False if the path does not exist
    '''
    #FIXME: handle SHAs
    #TODO: refactor into recursive method
    if type(gitrepo) == git.repo.Repo:
        repo = gitrepo
    else:
	try:
            repo = git.Repo(settings.REPO_DIR)
	except git.InvalidGitRepositoryError:
	    repo = git.Repo.create(settings.REPO_DIR)
    tree = repo.tree()
    try:
	    mykeys = tree.keys()
    except git.GitCommandError, gce:
    	print gce, " line 126"
    try:
        if path[-1]=="/": is_last_char = True
        else: is_last_char = False
    except IndexError, err:
        is_last_char = False
    if string.count(path, "/") > 0 and not is_last_char:
       pieces = string.split(path, "/")
       for each in pieces:
             mykeys = tree.keys()
             somedict = tree.__dict__["_contents"]
             if not somedict.has_key(each):
                return False
             if type(somedict[each]) == git.tree.Tree:
                tree = somedict[each]
       return True #it exists
    else:
       #strip the slashes from the path
       #(if a dir name is "blah", then "blah/" will not match "blah" on well behaving filesystems)
       if is_last_char: path = path[:-1]

       #check if it exists in /
       somedict = tree.__dict__["_contents"]
       if somedict.has_key(path):
             return True #has it
       else:
             return False #not there

def path_is_file(path="",sha="",gitrepo=""):
    '''
    return True if the path is a file
    return False if the path is a path (folder or directory)
    return False if the path does not exist (is not a file nor a dir)
    '''
    #FIXME: handle SHAs
    #TODO: refactor into recursive method
    if not gitrepo or type(gitrepo)==type("hi"): gitrepo = settings.REPO_DIR
    if type(gitrepo) == git.repo.Repo:
        repo = gitrepo
    else:
        repo = git.Repo(gitrepo)
    tree = repo.tree()
    try:
    	mykeys = tree.keys() #or else it doesn't work wtf
    except git.GitCommandError, gce:
    	print gce, " line 162"
    if (string.count(path, "/") > 0):
        pieces = string.split(path, "/")
        for each in pieces:
            #set tree to the tree with name 'each'
            #if there is no tree with name 'each',
            #then check if there's a file (git.blob.Blob)
            #with that name.
            mykeys = tree.keys() #or else it doesn't work wtf
            somedict = tree.__dict__["_contents"]
            if somedict.has_key(each):
                #if it's a file, return.
                if type(somedict[each]) == git.blob.Blob:
                    return True #it's a file
                if type(somedict[each]) == git.tree.Tree:
                    #this gets tricky.
                    tree = somedict[each]
        #it's not a file.
        return False #it's a dir, folder or tree
    else:
        #either a file or a directory in /
        somedict = tree.__dict__["_contents"]
        if somedict.has_key(path):
            if type(somedict[path]) == git.blob.Blob:
                return True #it's a file.
            elif type(somedict[path]) == git.tree.Tree:
                return False #it's a dir, folder or tree.
        else:
            return False #file or path not found

def index(request,path="",sha="",repodir=""):
    #show the index for a given path at a given sha id
    #check if the path is a path and not a file
    #if it is a file, show the view method
    pathcheck = path_exists(path=path,sha=sha)
    pathfilecheck = path_is_file(path=path,sha=sha)
    if pathcheck and pathfilecheck:
        return view(request,path=path,sha=sha)
    if not pathcheck and path:
        return new(request,path=path)
    if repodir == "":
        repo = git.Repo(settings.REPO_DIR)
    if type(repodir) == git.repo.Repo:
        repo = repodir
    if type(repodir) == type("") and not (repodir == ""):
        repo = git.Repo(repodir)
    try:
    	commits = repo.commits(start=sha or 'master', max_count=1, path=path)
    except git.GitCommandError:
    	commits = []
    if len(commits) > 0: head = commits[0]
    else: raise Http404 #oh boy
    #if sha == "" or not sha: head = commits[0]
    #else: #index view into the past
    #    print "for great justice!\n\n\n"
    #    for commit in commits:
    #        if commit.id == sha:
    #            head = commit
    #            print "the commit object is ", commit
    #print "sha is ", head.id, " and sha was: ", sha
    
    #FIXME: use find() and path_exists() and children() and path_is_file() here
    #files = head.tree.items()
    files = find(path=strip_trailing_slashes(path),sha=sha,depth=1)
    if len(files) == 1 and not (type(files) == type([])): files = files.items() #oopsies

    data_for_index = [] #start with nothing
    folders_for_index = []
    for each in files:
        toinsert = {}
        thethingy = None
        myblob = each[1]
        if type(myblob) == git.tree.Tree:
            mytree = myblob
            toinsert['name'] = mytree.name
            files2 = mytree.items()
            #toinsert['id'] = mytree.id
            toinsert['id'] = sha
            folders_for_index.append(toinsert)
            #add this folder (not expanded) (FIXME)
        else: #just add it
            thethingy = myblob.basename
            #if string.count("/",path) == 1:
            #    thethingy = myblob.basename
            #else:
            thethingy = repo.git.git_dir + "/" + myblob.basename
            thethingy = repo.git.git_dir + "/" + path + "/" +  myblob.basename
            thecommit = myblob.blame(repo,commit=sha or 'master',file=thethingy)[0][0]
	    if (thecommit):
            	toinsert['author'] = thecommit.committer.name
            	toinsert['author_email'] = thecommit.committer.email
            	toinsert['id'] = head.id #thecommit.id
            	toinsert['date'] = thecommit.authored_date
            	toinsert['message'] = thecommit.message
                toinsert['filename'] = myblob.basename
                toinsert['filepath'] = path + myblob.basename
            	data_for_index.append(toinsert)
    return django.shortcuts.render_to_response("index.html", locals())

def edit(request, path="", sha=""):
    '''
    edit a page. if there are POST variables, these will be taken as the contents of the edit.

    the "sha" named parameter is for which version of the file to edit
    TODO: proper branching support
    '''
    if request.method == 'GET':
        #display edit form
        pass
    elif request.method == 'POST':
        #commit modifications
        pass
    return django.shortcuts.render_to_response("edit.html", locals())

def archive(request,path="",sha=""):
    '''
    download a zip archive of the current path
    
    (the archive must have the full path (inside of it) so that it is not a tarbomb)

    #git archive --format=zip --prefix=SITE_NAME/ HEAD:THE_DIRECTORY_HERE/ > archive.zip
    '''
    repo = git.Repo(settings.REPO_DIR)
    mycommit = repo.commit(id=sha or 'master',path=path) #er, test this
    mytree = mycommit.tree()
    myitems = mytree.items()
    #now what about the path?
    #cases:
    #1) it's a file
    #2) it's a folder
    return django.shortcuts.render_to_response("archive.html", locals())

def history(request,path="",sha=""):
    '''
    return the history for a given path (commits)

    "sha" determines the latest version to show (not necessary but useful for paging, etc.)

    should work for /history, some-dir/history, and some-file/history
    '''
    #display: id, committer.author, committer.author_email, date, message
    if not path_exists(path=path,sha=sha):
        raise Http404
    #see: http://adl.serveftp.org:4567/history
    #see: adl /var/www/git-wiki/lib/wiki/resource.rb
    repo = git.Repo(settings.REPO_DIR)
    log = repo.log(commit=sha or 'master',path=path)
    history_data = []
    for commit in log:
        toadd = {}
        toadd["commit_id"] = commit.id
        toadd["author"] = commit.author.name
        toadd["author_email"] = commit.author.email
        toadd["date"] = commit.committed_date
        toadd["message"] = commit.summary
        history_data.append(toadd)
    return django.shortcuts.render_to_response("history.html", locals())

def diff(request, path="", sha1="", sha2=""):
    '''
    display the diff between two commits (SHA strings)

    to select them, use the history view.
    '''
    if not path_exists(path=path,sha=sha1) or not path_exists(path=path,sha=sha2):
        #that commit doesn't exist!
        raise Http404
    repo = git.Repo(settings.REPO_DIR)
    diff = repo.diff(a=sha1,b=sha2,paths=[path])
    return django.shortcuts.render_to_response("diff.html", locals())

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
    return django.shortcuts.render_to_response("upload.html", locals())

def new(request,path="",sha=""):
    '''
    make a new file/page at the given "path"

    TODO: implement branching given the "sha" named parameter
    '''
    message = "no message"
    if request.method == 'GET':
        #show the form
        message = "this is the GET message"
        pass
    elif request.method == 'POST':
        #add content to repo
        pass
    return django.shortcuts.render_to_response("new.html", locals())

def changelog(request,path="",sha=""):
    '''
    display the RSS changelog for this path

    TODO: display the RSS changelog for all changes since sha="sha" (optional)
    '''
    return django.shortcuts.render_to_response("changelog.rss", locals())

def view(request,path="",sha="master"):
    '''
    view the path/file/page at a given commit

    note: if it's a folder, return the index view.
    '''
    #check if the path is a path or if the path is a file
    if path:
        if not path_is_file(path=path,sha=sha):
            return index(request,path=path,sha=sha)
    repo = git.Repo(settings.REPO_DIR)
    commits = repo.commits(start=sha,max_count=1)
    head = commits[0]
    files = head.tree.items()
    returncontents = ""
    stop = False
    cur_tree = head.tree
    while not stop:
        check = False
        name = cur_tree.name
        if not name: name = "" #or "/"
        if path.count("/") == 0:
            #check = cur_tree.__dict__["_contents"].has_key(path)
            check2 = (cur_tree.keys()).count(path) #is "path" a file in this tree?
            if check2 == 0: check = False #path is not a file in this tree
            else: check = True #ok, it is
            checkthing = path #in the case of a file, checkthing needs to be the path
        else:
            if not hasattr(cur_tree.__dict__["_contents"], "has_key"):
                raise Http404()
            check = cur_tree.__dict__["_contents"].has_key(pop_path_rev(copy.copy(path))) #
            checkthing = pop_path_rev(path) #in the case of a folder, checkthing needs to be the remaining path as we travel down the rabbit hole
        if check and not name == checkthing: #we don't have what we want, and it's a valid key, so let's setup the next step in the while loop
            cur_tree = cur_tree[checkthing]
            path = pop_path(path) 
            if type(cur_tree) == git.blob.Blob: stop = True #stop if we have our file (by definition we can't go deeper anyway)
        elif name == checkthing: stop = True #we have what we want, let's roll.
    if type(cur_tree) == git.blob.Blob:
        returncontents = cur_tree.data
    return django.shortcuts.render_to_response("view.html", locals())

def render(request, file="", filename=""):
    '''
    render - meant for displaying some of the static images for the template
    
    this is a terrible hack.
    (see urls.py)
    '''
    if not filename and not (file == ""):
        if (file.rfind("css") > 0):
            return django.shortcuts.render_to_response(file,locals(),mimetype="text/css")
        elif (file.rfind("js") > 0):
            return django.shortcuts.render_to_response(file,locals(),mimetype="text/js")
    elif not filename == "":
        fp = open(os.path.join(os.path.realpath(os.path.curdir),("templates/djangit-static/static/images/%s.png" % (filename))))
        blah = fp.read()
        return HttpResponse(blah,mimetype="image/png")
