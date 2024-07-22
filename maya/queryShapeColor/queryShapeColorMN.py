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

class LookShapeColorWindow(UI.TableWindowBase):
    def __init__(self, parent):
        self._setting_strs=[
            "ShapeColorTable"
        ]
        super(LookShapeColorWindow, self).__init__(parent)
        windowTitle="queryShapeColors"
        self.setObjectName(windowTitle)
        self.setWindowTitle(windowTitle)
        self.buttonLeft_QPushButton.setText("print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.table_SelfTableWidget.setHeaderLabelStrs(["ObjectName","OverrideColor","OverrideColorR","OverrideColorG","OverrideColorB","WireFrameColor","WireFrameColorR","WireFrameColorG","WireFrameColorB"])
        self.table_SelfTableWidget.createBase()
        geometry=self.table_SelfTableWidget.geometry()
        self.setGeometry(geometry)

    #Single Function
    @staticmethod
    def nurbsCurves_check_bool(node_str):
        shape_strs=cmds.listRelatives(node_str,type='nurbsCurve')
        if None is shape_strs:
            return False
        else:
            return True

    #Setting Function
    def setShapeColorTable(self,variables):
        self.table_SelfTableWidget.setDataTableWidgetLists(variables)
        self.table_SelfTableWidget.createTable()
    def getShapeColorTable(self):
        tableWidgetItem_lists=self.table_SelfTableWidget.queryTableLists()
        return tableWidgetItem_lists

    #Public Function
    def createSelectionTable(self,variables):
        table_lists=[]
        getAttr_strs=[
            "overrideColor",
            "overrideColorR",
            "overrideColorG",
            "overrideColorB",
            "objectColor",
            "wireColorR",
            "wireColorG",
            "wireColorB"
        ]
        shape_lists=[
            cmds.listRelatives(node_str,type='nurbsCurve')
            for node_str in variables
            if self.nurbsCurves_check_bool(node_str)
        ]
        shape_strs=[
            shape_str 
            for shape_strs in shape_lists
            for shape_str in shape_strs
        ]
        for shape_str in shape_strs:
            getColor_strs=[shape_str]
            for getAttr_str in getAttr_strs:
                getColor_str=str(cmds.getAttr(shape_str+"."+getAttr_str))
                getColor_strs.append(getColor_str)
            table_lists.append(getColor_strs)
        self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
        self.table_SelfTableWidget.createTable()

    def editSelectionTable(self,variables):
        table_lists=self.table_SelfTableWidget.queryTableLists()
        getAttr_strs=[
            "overrideColor",
            "overrideColorR",
            "overrideColorG",
            "overrideColorB",
            "objectColor",
            "wireColorR",
            "wireColorG",
            "wireColorB"
        ]
        shape_lists=[
            cmds.listRelatives(node_str,type='nurbsCurve')
            for node_str in variables
            if self.nurbsCurves_check_bool(node_str)
        ]
        shape_strs=[
            shape_str 
            for shape_strs in shape_lists
            for shape_str in shape_strs
        ]
        for shape_str in shape_strs:
            getColor_strs=[shape_str]
            for getAttr_str in getAttr_strs:
                getColor_str=str(cmds.getAttr(shape_str+"."+getAttr_str))
                getColor_strs.append(getColor_str)
            table_lists.append(getColor_strs)
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
    viewWindow=LookShapeColorWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.buttonCenterClicked()
    viewWindow.show()