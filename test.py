import appuifw
import sys

def foo():
    form = appuifw.Form([(u"Foobar", 'text'), (u"Barfoo", 'date')])
    form.execute()

def large():
    appuifw.app.screen = 'large'

def full():
    appuifw.app.screen = 'full'

def normal():
    appuifw.app.screen = 'normal'

def tab_changed(i):
    print "Tab changed to %d" % (i)

#appuifw.app.screen = 'full'
appuifw.app.title = 'Foobar'
appuifw.app.menu = [(u'test', foo), (u'Screen', ((u'large', large), (u'full', full), (u'normal', normal)))]
print type(appuifw.app)
appuifw.app.set_tabs([u"foo", u"Bar"], tab_changed)


sys.exit(appuifw.app.exec_())


