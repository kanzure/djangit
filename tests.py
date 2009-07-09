#!/usr/bin/python
#note: move this into the parent directory and run it.
#is there a better way to do django unit tests?
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "pydjangitwiki/settings"
#done setting up environment
import pydjangitwiki
#for view testing
import pydjangitwiki.wiki.views
#for url testing
import pydjangitwiki.urls
import unittest
import git
import copy

class TestURLs(unittest.TestCase):
    def test_index(self):
        #pydjangitwiki.urls.urlpatterns that should return index
        pass
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
        pass
    def test_render(self):
        pass

class TestViews(unittest.TestCase):
    def test_pop_path(self):
       path = "super/star/destroyer"
       self.assertTrue(pydjangitwiki.wiki.views.pop_path(path)=="star/destroyer")
       path ="/super/star/destroyer"
       #print pydjangitwiki.wiki.views.pop_path(path)
       self.assertTrue(pydjangitwiki.wiki.views.pop_path(path)=="star/destroyer")
       path = "one/two/three/four/"
       self.assertTrue(pydjangitwiki.wiki.views.pop_path(copy.copy(path))=="two/three/four/")
       popped = pydjangitwiki.wiki.views.pop_path(copy.copy(path))
       popped2 = pydjangitwiki.wiki.views.pop_path(copy.copy(popped))
       self.assertTrue(popped2=="three/four/")
    def test_children(self):
        #find all tree items and combine them into a dict
        #depth=-1 means infinite depth
        
        #make a repo, add files, commit, etc.
        #then check to see if those files are there

        #now make a repo, add files, commit, add folders, etc.
        #then check to see if those files & folders are there

        pass
    def test_find(self):
        pass
    def test_pathExists(self):
        pass
    def test_pathIsFile(self):
        pass
    def test_index(self):
        pass
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
        pass
    def test_render(self):
        #not sure if this needs to be tested
        #it's kind of a hack in the first place
        pass

if __name__ == '__main__':
    unittest.main()
