# -*- coding: iso-8859-15 -*-
try:
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
except ImportError:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *

import maya.cmds as cmds

import cgInTools as cit
from ...ui import tableUI as UI
from ..library import windowLB as wLB
cit.reloads([UI,wLB])

class LookKeyWindow(UI.TableWindowBase):
    def __init__(self,parent):
        super(LookKeyWindow, self).__init__(parent)
        windowTitle="queryKeyAttr_lists"
        self.setObjectName(windowTitle)
        self.setWindowTitle(windowTitle)
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.table_SelfTableWidget.setHeaderReverseBool(True)
        geometry=self.table_SelfTableWidget.geometry()
        self.setGeometry(geometry)

    #Single Function
    @staticmethod
    def getKeyAttrs_query_strs_strs(node_str):
        attrValue_strs=[]
        attrValue_strs.append(node_str)
        keyAttr_values=cmds.listAttr(node_str,k=True)
        headerLabel_strs=["ObjectName"]
        for keyAttr_value in keyAttr_values:
            headerLabel_strs.append(str(keyAttr_value))
            attrValue_value=cmds.getAttr(node_str+"."+keyAttr_value)
            attrValue_strs.append(str(attrValue_value))
        return headerLabel_strs,attrValue_strs

    #Public Function
    def createSelectionTable(self,variables):
        table_lists=[]
        for node_str in variables:
            self._headerLabel_strs,attrValue_strs=self.getKeyAttrs_query_strs_strs(node_str)
            table_lists.append(attrValue_strs)
            self.table_SelfTableWidget.setHeaderLabelStrs(self._headerLabel_strs)
            self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
            self.table_SelfTableWidget.createTable()

    def editSelectionTabel(self,variables):
        table_lists=self.table_SelfTableWidget.queryTableLists()
        for node_str in variables:
            self._headerLabel_strs,attrValue_strs=self.getKeyAttrs_query_strs_strs(node_str)
            table_lists.append(attrValue_strs)
            self.table_SelfTableWidget.setHeaderLabelStrs(self._headerLabel_strs)
            self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
            self.table_SelfTableWidget.createTable()
    
    def buttonLeftClicked(self):
        main()

    def buttonCenterClicked(self):
        node_strs=cmds.ls(sl=True)
        self.createSelectionTable(node_strs)

    def buttonRightClicked(self):
        node_strs=cmds.ls(sl=True)
        self.editSelectionTabel(node_strs)

def main():
    viewWindow=LookKeyWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.buttonCenterClicked()
    viewWindow.show()