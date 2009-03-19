import appuifw
import sys
from PyQt4 import QtCore

def foo():
    pass

def large():
    appuifw.app.screen = 'large'

def full():
    appuifw.app.screen = 'full'

def normal():
    appuifw.app.screen = 'normal'

def tab_changed(i):
    print "Tab changed to %d" % (i)

appuifw.app.screen = 'full'
appuifw.app.title = u'Foobar'
#appuifw.app.menu = [(u'test', foo), (u'Screen', ((u'large', large), (u'full', full), (u'normal', normal)))]
#print type(appuifw.app)
#appuifw.app.set_tabs([u"foo", u"Bar"], tab_changed)

#form = appuifw.Form([(u"Foobar", 'text'), 
#                     (u"Barfoo", 'date', 102221222.1),
#                     (u"Default Date", 'date'),
#                     (u"Barfoo", 'time', 102221222.1),
#                     (u"Default time", 'time'),
#                     (u"C-c-c-combo", 'combo', ([u"foobar", u"barfoo", u"buffalo"], 2))])
#form.execute()
#print form[0]
#print form[1]
#print form[2]
#print form[3]
#print form[4]

while 1:
    pass
#sys.exit(appuifw.app.exec_())




