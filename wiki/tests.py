#!/usr/bin/python
import unittest
import git
import copy
import djangit.wiki.views
import djangit.urls
import djangit.settings
import django.test.client
import django.test
import os #for rmall

def addfile(repo="",filename="myfilename",contents="contents",message="commit message"):
    if not repo: return False
    thefile = open(repo.git.get_dir + "/" + filename,"w")
    thefile.write(contents)
    thefile.close()
    repo.git.execute(["git","add",filename])
    repo.git.execute(["git","commit","-m",message])
    return True

def addfolder(repo="",foldername="myfoldername",message="commit message"):
    if not repo: return False
    git.os.mkdir(repo.git.get_dir + "/" + foldername)
    repo.git.execute(["git","add",foldername])
    #you can't commit just a folder
    #repo.git.execute(["git","commit","-m",message])
    return True

def rmall(path="/tmp/some/dir/here/"):
    top = path
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
                os.remove(os.path.join(root, name))
        for name in dirs:
                os.rmdir(os.path.join(root, name))
    return

def begin(path="/tmp/tmprepo",barepath="/tmp/bare-repo/"):
    #mkdir tmpdir; cd tmpdir; git init; cd ..; git clone --bare tmpdir/ bare/;
    rmall(path)
    if git.os.path.exists(path): git.os.rmdir(path)
    git.os.mkdir(path)
    rmall(barepath)
    if git.os.path.exists(barepath): git.os.rmdir(barepath)
    #git.os.mkdir(barepath)
    #barerepo = git.Repo.create(barepath)#mkdr=True)
    git.Git.execute(git.Git(path),["git","init"])
    git.Git.execute(git.Git(path),["git","clone","--bare",path,barepath])
    djangit.settings.REPO_DIR = path

    return git.Repo(path)

def end(path="/tmp/tmprepo",barepath="/tmp/bare-repo/"):
    rmall(path)
    git.os.rmdir(path)
    rmall(barepath)
    git.os.rmdir(barepath)
    return

def find_urls(methodname="index"):
    '''
    return all RegexURLPattern objects that call a certain method
    '''
    patterns = djangit.urls.urlpatterns
    returnlist = []
    for pat in patterns:
        if pat.callback.__name__ == methodname:
            #see also: pat.callback.__module__
            returnlist.append(pat)
    return returnlist

def resolve(regexes=[],validpatterns=[]):
    returndict = {}
    for each in regexes:
        for pattern in validpatterns:
            if not each.resolve(pattern) == None:
                if not returndict.has_key(pattern):
                    returndict[pattern] = [each]
                else:
                    returndict[pattern].append(each)
    return returndict

#class TestURLs(unittest.TestCase):
class TestURLs:
    def test_index(self):
        #djangit.urls.urlpatterns that should return 'pydjangitwiki.wiki.views.index'
        #note: some of these patterns are handled by 'view' which then calls index()
        #validpatterns = ["/", "", "/folder-name/", "folder-name"]
        validpatterns = [""]
        regexes = find_urls(methodname="index")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_edit(self):
        validpatterns = [
                            "edit/",
                            "edit",
                            "home/something/something/edit",
                            "home/something/something/edit/",
                        ]
        regexes = find_urls(methodname="edit")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_archive(self):
        validpatterns = [
                            "archive/", #or is this a dir?
                            "archive",
                            "home/something/something/archive", #or is this a file?
                            "home/something/something/archive/", #or is this a dir?
                            "/archive", #or is this a file?
                            "/archive/", #or is this a dir?
                        ]
        regexes = find_urls(methodname="archive")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_history(self):
        validpatterns = [
                            "history",
                            "/history", #or is this a file?
                            "/history/", #or is this a dir?
                            "history/", #or is this a dir?
                            "some/path/here/history",
                            "some/path/here/history/", #or is this a dir?
                        ]
        regexes = find_urls(methodname="history")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_upload(self):
        validpatterns = [
                            "upload",
                            "some/path/to/a/file/upload",
                            #"some/path/to/a/dir/upload", #should this be invalid?
                        ]
        regexes = find_urls(methodname="upload")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_new(self):
        validpatterns = [
                            "new",
                            "some/path/to/a/dir/file/new",
                        ]
        regexes = find_urls(methodname="new")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_changelog(self):
        validpatterns = [
                            "changelog.rss",
                            "some/path/to/a/dir/file/changelog.rss",
                        ]
        regexes = find_urls(methodname="changelog")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_view(self):
        validpatterns = [
                            "some/path/to/a/file",
                            "some/path/to/a/dir/", #should redirect to index() however
                            "some/path/to/a/file/SHA_HERE",
                        ]
        regexes = find_urls(methodname="view")
        testresults = resolve(regexes=regexes,validpatterns=validpatterns)
        self.assertTrue(len(testresults) == len(validpatterns))
        return
    def test_render(self):
        #not sure if we care about this hack of a function
        #it should be rewritten anyway
        pass

class TestViews(django.test.TestCase):
    #TODO: test_addfile
    #TODO: test_addfolder
    #TODO: test_rmall
    #TODO: test_begin
    #TODO: test_end
    def test_pop_path(self):
       path = "super/star/destroyer"
       self.assertTrue(djangit.wiki.views.pop_path(path)=="star/destroyer")
       path ="/super/star/destroyer"
       #print djangit.wiki.views.pop_path(path)
       self.assertTrue(djangit.wiki.views.pop_path(path)=="star/destroyer")
       path = "one/two/three/four/"
       self.assertTrue(djangit.wiki.views.pop_path(copy.copy(path))=="two/three/four/")
       popped = djangit.wiki.views.pop_path(copy.copy(path))
       popped2 = djangit.wiki.views.pop_path(copy.copy(popped))
       self.assertTrue(popped2=="three/four/")
    def test_children(self):
        #find all tree items and combine them into a dict
        #depth=-1 means infinite depth
        
        #make a repo, add files, commit, etc.
        #then check to see if those files are there
        #see git.Repo.init_bare(path,mkdir=True)
        #tmprepo = git.Repo.init_bare("/tmp/tmprepo/",mkdir=True)
        rmall("/tmp/tmprepo")
        if git.os.path.exists("/tmp/tmprepo"): git.os.rmdir("/tmp/tmprepo")
        git.os.mkdir("/tmp/tmprepo")
        tmprepo = git.Git("/tmp/tmprepo/")
        tmprepo.execute(["git","init"])
        somefile = open("/tmp/tmprepo/somefile","w")
        somefile.write("this is some file in the repository")
        somefile.close()
        fancyhat = open("/tmp/tmprepo/fancyhat","w")
        fancyhat.write("there is a fancy hat here")
        fancyhat.close()
        tmprepo.execute(["git","add","somefile"])
        tmprepo.execute(["git","add","fancyhat"])
        tmprepo.execute(["git","commit","-m","commited somefile and fancyhat"])

        children = djangit.wiki.views.children(gitpath=tmprepo.get_dir)
        self.assertTrue(children.has_key("somefile"))
        self.assertTrue(children.has_key("fancyhat"))

        rmall(tmprepo.get_dir)
        git.os.rmdir(tmprepo.get_dir)

        #now make a repo, add files, commit, add folders, etc.
        #then check to see if those files & folders are there

        pass
    def test_find(self):
        pass
    def test_pathExists(self):
        tmprepo = begin(path="/tmp/tmprepo")
        addfile(repo=tmprepo,filename="superfile",contents="file contents, you see",message="added superfile")
        self.assertTrue(djangit.wiki.views.pathExists(path="superfile",gitrepo=tmprepo))
        self.assertFalse(djangit.wiki.views.pathExists(path="some_file_that_does_not_exist",gitrepo=tmprepo))
        #check a non-existant folder
        self.assertFalse(djangit.wiki.views.pathExists(path="folder/to/the/place/",gitrepo=tmprepo))
        self.assertFalse(djangit.wiki.views.pathExists(path="folder/to/the/place",gitrepo=tmprepo))
        #make a folder
        blah = addfolder(repo=tmprepo,foldername="folder")
        #make a file in the folder
        addfile(repo=tmprepo,filename="folder/somefile",contents="contents of the file go here",message="added a file")
        children = djangit.wiki.views.children(gitpath=tmprepo.git.get_dir)
        #test the folder
        self.assertTrue(djangit.wiki.views.pathExists(path="folder",gitrepo=tmprepo))
        #self.assertTrue(djangit.wiki.views.pathExists(path="folder/",gitrepo=tmprepo)) #should this work?
        #self.assertTrue(djangit.wiki.views.pathExists(path="/folder",gitrepo=tmprepo))
        #self.assertTrue(djangit.wiki.views.pathExists(path="/folder/",gitrepo=tmprepo))
        #make a file in the folder
        #test the file
        self.assertTrue(djangit.wiki.views.pathExists(path="folder/somefile",gitrepo=tmprepo))
        end(tmprepo.git.get_dir)
        return
    def test_pathIsFile(self):
        tmprepo = begin(path="/tmp/tmprepo")
        addfile(repo=tmprepo,filename="myfilename",contents="these are the contents of the file",message="added myfilename")
        self.assertTrue(djangit.wiki.views.pathIsFile(path="myfilename",gitrepo=tmprepo))
        self.assertFalse(djangit.wiki.views.pathIsFile(path="/",gitrepo=tmprepo))
        self.assertFalse(djangit.wiki.views.pathIsFile(path="some_file_that_does_not_exist",gitrepo=tmprepo))
        #make a folder, add a file.
        addfolder(repo=tmprepo,foldername="foldername",message="added a folder, behold!")
        #test the folder
        self.assertFalse(djangit.wiki.views.pathIsFile(path="foldername/",gitrepo=tmprepo))
        self.assertFalse(djangit.wiki.views.pathIsFile(path="foldername",gitrepo=tmprepo))
        #add a file
        addfile(repo=tmprepo,filename="foldername/some-super-file",contents="well, here goes nothing",message="trying subdir adding file")
        #test the file
        self.assertTrue(djangit.wiki.views.pathIsFile(path="foldername/some-super-file",gitrepo=tmprepo))
        #what about another file in the dir?
        self.assertFalse(djangit.wiki.views.pathIsFile(path="foldername/other_file_here",gitrepo=tmprepo))
        end(tmprepo.git.get_dir)
        return
    def test_index(self):
        #make a repository
        tmprepo = begin(path="/tmp/tmprepo/")
        
        #add a file
        filenamevar = "the_filename"
        addfile(repo=tmprepo,filename=filenamevar,contents="this is the content of the file",message="added the_filename")
        #test that the dict worked
        c = self.client
        #FIXME: c.get() calls djangit.wiki.index() but it ignores pydjangitwiki.settings.REPO_DIR modifications made in begin()
        response = c.get("/")
        self.assertTrue(response.context[0].dicts[0].keys().__contains__("data_for_index"))
        #test that the file shows up in the index's output
        has_right_filename = False
        for each in response.context[0].dicts[0]["data_for_index"]:
            if each.has_key("filename"):
                if each["filename"] == filenamevar:
                    has_right_filename = True
        self.assertTrue(has_right_filename)

        #add a folder
        #add a file within that folder
        foldernamevar = "the-folder-name"
        filenamevaragain = foldernamevar + "/" + "somethingfilesomething.so"
        addfolder(repo=tmprepo,foldername=foldernamevar,message="added a folder")
        addfile(repo=tmprepo,filename=filenamevaragain,contents="contents of a file go here.\nnewline.\ttab\n\t\ttabtab.",message="added a file")
        c = self.client
        response = c.get("/")
        #it should have a folder.
        self.assertTrue(response.context[0].dicts[0].keys().__contains__("folders_for_index"))
        #it should have data for the index
        self.assertTrue(response.context[0].dicts[0].keys().__contains__("data_for_index"))
        #it should have the folder
        self.assertTrue(response.context[0].dicts[0]["folders_for_index"][0].has_key("name"))
        self.assertTrue(response.context[0].dicts[0]["folders_for_index"][0]["name"] == foldernamevar)
        #it should have the file
        #note that the only reason we can do this is because there's one file in the output.
        self.assertTrue(response.context[0].dicts[0]["data_for_index"][0]["filename"] == filenamevar)

        #cleanup
        end(tmprepo.git.get_dir)
        return
    def test_edit(self):
        pass
    def test_archive(self):
        pass
    def test_history(self):
        pass
    def test_upload(self):
        pass
    def test_new(self):
        pass
    def test_changelog(self):
        pass
    def test_view(self):
        tmprepo = begin(path="/tmp/tmprepo")
        filenamevar = "the_filename"
        filecontent = "filecontent goes here"
        addfile(repo=tmprepo,filename=filenamevar,contents=filecontent,message="added the_filename")
        c = self.client
        response = c.get("/" + filenamevar)
        self.assertTrue(response.context[0].dicts[0]["returncontents"]==filecontent)
        #test view of file in a folder
        foldernamevar = "the-folder-name"
        filenamevaragain = foldernamevar + "/" + "somethingfilesomething.so"
        filenamevaragain_contents = "contents of a file go here.\nnewline\n\t\ttabtab."
        addfolder(repo=tmprepo,foldername=foldernamevar,message="added a folder")
        addfile(repo=tmprepo,filename=filenamevaragain,contents=filenamevaragain_contents,message="added the-folder-name/somethingfilesomething.so")
        c = self.client
        response = c.get("/" + filenamevaragain)
        self.assertTrue(response.context[0].dicts[0]["returncontents"]==filenamevaragain_contents)
        end(tmprepo.git.get_dir)
        pass
    def test_render(self):
        #not sure if this needs to be tested
        #it's kind of a hack in the first place
        pass

if __name__ == '__main__':
    django.test.utils.setup_test_environment()
    #django.conf.settings.configure(default_settings=djangit.settings,REPO_DIR="/tmp/tmprepo")
    unittest.main()
