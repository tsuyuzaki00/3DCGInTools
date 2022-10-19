# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import os
from maya import cmds
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from ...ui import scriptsRunUI as UI
from ..library import cJson as SJ

class MainMenu(UI.MainWindowBase):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)
        self.setWindowTitle("windowTitle")
        
        layouts = QFormLayout(self)
        self.centerWidget.setLayout(layouts)
        #widget = NewClassName(self)
        #layouts.addWidget(widget)

# mayaのメインウインドウを取得する
def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    widget = wrapInstance(int(ptr), QWidget)
    return widget

def main():
    # 依存関係のないウインドウを継承して作ったMaya用のボタンUI
    maya_window_instance = MainMenu(parent=get_maya_main_window())
    maya_window_instance.show()