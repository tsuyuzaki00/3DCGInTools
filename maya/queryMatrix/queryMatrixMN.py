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
class LookMatrixWindow(UI.TableWindowBase):
    def __init__(self,parent):
        super(LookMatrixWindow,self).__init__(parent)
        windowTitle="queryMatrix_lists"
        self.setObjectName(windowTitle)
        self.setWindowTitle(windowTitle)
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.table_SelfTableWidget.setHeaderReverseBool(True)
        self.table_SelfTableWidget.setHeaderLabelStrs([
            "ObjectName",
            "NormalMatrixX","NormalMatrixY","NormalMatrixZ","NormalMatrixT",
            "worldMatrixX","worldMatrixY","worldMatrixZ","worldMatrixT",
            "ParentMatrixX","ParentMatrixY","ParentMatrixZ","ParentMatrixT",
            "XformMatrixX","XformMatrixY","XformMatrixZ","XformMatrixT",
            "InverseMatrixX","InverseMatrixY","InverseMatrixZ","InverseMatrixT",
            "InverseWorldMatrixX","InverseWorldMatrixY","InverseWorldMatrixZ","InverseWorldMatrixT",
            "InverseParentMatrixX","InverseParentMatrixY","InverseParentMatrixZ","InverseParentMatrixT",
            "OffsetParentMatrixX","OffsetParentMatrixY","OffsetParentMatrixZ","OffsetParentMatrixT"
        ])
        self.table_SelfTableWidget.createBase()
        geometry=self.table_SelfTableWidget.geometry()
        self.setGeometry(geometry)

    #Single Function
    @staticmethod
    def nodeMatrix_query_strs(node_str):
        getAttr_strs=[
            "matrix",
            "worldMatrix",
            "parentMatrix",
            "xformMatrix",
            "inverseMatrix",
            "worldInverseMatrix",
            "parentInverseMatrix",
            "offsetParentMatrix"
        ]
        matrix_strs=[]
        matrix_strs.append(node_str)
        for getAttr_str in getAttr_strs:
            getMatrix_floats=cmds.getAttr(node_str+"."+getAttr_str)
            for i in range(0,13):
                matrix_strs.append(str(getMatrix_floats[i]))
        return matrix_strs
    
    #Public Function
    def createSelectionTable(self,variables):
        table_lists=[]
        for node_str in variables:
            matrix_strs=self.nodeMatrix_query_strs(node_str)
            table_lists.append(matrix_strs)
            self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
            self.table_SelfTableWidget.createTable()
    
    def editSelectionTable(self,variables):
        table_lists=self.table_SelfTableWidget.queryTableLists()
        for node_str in variables:
            matrix_strs=self.nodeMatrix_query_strs(node_str)
            table_lists.append(matrix_strs)
            self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
            self.table_SelfTableWidget.createTable()

    def buttonLeftClicked(self):
        main()

    def buttonCenterClicked(self):
        node_strs=cmds.ls(sl=True)
        self.createSelectionTable(node_strs)

    def buttonRightClicked(self):
        node_strs=cmds.ls(sl=True)
        self.editSelectionTable(node_strs)

def main():
    viewWindow=LookMatrixWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.buttonCenterClicked()
    viewWindow.show()