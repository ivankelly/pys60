from PyQt4 import QtGui, QtCore

class S60Menu(QtGui.QMenu):
    def __init__(self, menu):
        QtGui.QMenu.__init__(self, "s60menu")
        self._submenus = []
        if len(menu) > 0:
            for mi in menu:
                if type(mi) == tuple and len(mi) > 1:
                    if type(mi[1]) == tuple:
                        # submenu 
                        submenu = QtGui.QMenu(mi[0]);
                        for s in mi[1]:
                            submenu.addAction(s[0], s[1])
                        self.addMenu(submenu)
                        self._submenus.append(submenu)
                    else:
                        self.addAction(mi[0], mi[1])

