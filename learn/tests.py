#coding=utf-8
from django.test import TestCase
from django.core.urlresolvers import resolve
from learn.views import index
from docs.views import doc

#单元测试试验田
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)

    def test_root_url_resovles_to_index_view(self):
        found = resolve('/')
        print "=========="
        print found
        self.assertEqual(found.func, index)

    def test_root_url_resovles_to_doc_name(self):
        found = resolve('/doc/')
        print "=========="
        print found
        self.assertEqual(found.url_name, "doc")
