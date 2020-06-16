# encoding: utf8
import os
import sys
import unittest
try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk


pygubu_basedir = os.path.abspath(os.path.dirname(
                    os.path.dirname(os.path.realpath(sys.argv[0]))))
if pygubu_basedir not in sys.path:
    sys.path.insert(0, pygubu_basedir)

import pygubu
import support

has_scrolledtext = False
if sys.version_info.major >= 3:
    from tkinter.scrolledtext import ScrolledText
    has_scrolledtext = True

class TestScrolledtest(unittest.TestCase):

    def setUp(self):
        support.root_deiconify()
        if has_scrolledtext:
            xmldata = 'test_tkinter_scrolledtext.ui'
            self.builder = builder = pygubu.Builder()
            builder.add_from_file(xmldata)
            self.widget = builder.get_object('mainframe')
            self.scrolledtext = builder.get_object('scrolledtext1')

    def tearDown(self):
        support.root_withdraw()

    @unittest.skipIf(has_scrolledtext == False, 'Needs Python 3 for this')
    def test_class(self):
        self.assertIsInstance(self.scrolledtext, ScrolledText)
        self.widget.destroy()
