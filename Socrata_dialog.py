# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SocrataDialog
                                 A QGIS plugin
 Automatically Download or Upload to Socrata
                             -------------------
        begin                : 2016-03-01
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Socrata, Inc
        email                : peter.moore@socrata.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Socrata_dialog_base.ui'))

MAP_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'Domain_maps.ui'))

MESSAGE_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'MessageBox.ui'))
class SocrataDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SocrataDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

class MapDialog(QtGui.QDialog, MAP_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MapDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

class MessageDialog(QtGui.QDialog, MESSAGE_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MessageDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)