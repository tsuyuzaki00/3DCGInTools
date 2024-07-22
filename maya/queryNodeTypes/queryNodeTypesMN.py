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
import maya.api.OpenMaya as om2
import random
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import cgInTools as cit
from ...ui import tableUI as UI
from ...library import dataLB as dLB
from ...library import jsonLB as jLB
from ..library import windowLB as wLB
from ..library import checkLB as chLB
cit.reloads([UI,dLB,jLB,wLB,chLB])

DATAFOLDER_STR="queryNodeTypes"
RESET_DIR,DATA_DIR=cit.checkScriptsData(DATAFOLDER_STR,cit.maya_dir,cit.mayaData_dir)

class QueryNodeTypeWindow(MayaQWidgetDockableMixin,UI.TableWindowBase):
    def __init__(self, parent):
        self._setting_strs=[
            "NodeTypeTable"
        ]
        super(QueryNodeTypeWindow,self).__init__(parent)
        self._dataFolder_str=DATAFOLDER_STR
        self._reset_dir=RESET_DIR
        self._data_dir=DATA_DIR
        
        windowTitle_str="queryNodeTypes"
        random_int=random.randint(0,9999)
        self.setObjectName(windowTitle_str+str(random_int))
        self.setWindowTitle(windowTitle_str)

        self.buttonLeft_QPushButton.setText("Print")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

        self.table_SelfTableWidget.setHeaderLabelStrs(["ObjectName","NodeType","MFnType","MFnTypeID"])
        self.table_SelfTableWidget.createBase()
        geometry=self.table_SelfTableWidget.geometry()
        self.setGeometry(geometry)

    #Single Function
    @staticmethod
    def sameObjName_check_func(node_strs):
        check=chLB.CheckBoolean()
        for node_str in node_strs:
            check.setNode(node_str)
            judge_dict=check.sameObjName()
            if judge_dict["bool"]:
                #print("OK:"+" node:"+str(judge_dict["node"]))
                pass
            else:
                cmds.error("NG:"+"sameObjName node:"+str(judge_dict["node"]))

    @staticmethod
    def addShapes_query_strs(node_strs):
        nodeAndShape_strs=[]
        for node_str in node_strs:
            nodeAndShape_strs.append(node_str)
            shape_strs=cmds.listRelatives(node_str,s=True)
            if not shape_strs == None:
                for shape_str in shape_strs:
                    nodeAndShape_strs.append(shape_str)
        return nodeAndShape_strs

    @staticmethod
    def MFuType_query_str_int(node):
        if node == None:
            return None
        node_MSelectionList=om2.MSelectionList()
        node_MSelectionList.add(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject.apiTypeStr,node_MObject.apiType()

    #Setting Function
    def setNodeTypeTable(self,variables):
        self.table_SelfTableWidget.setDataTableWidgetLists(variables)
        self.table_SelfTableWidget.createTable()
    def getNodeTypeTable(self):
        tableWidgetItem_lists=self.table_SelfTableWidget.queryTableLists()
        return tableWidgetItem_lists

    #Public Function
    def createSelectionTable(self,variables):
        table_lists=[]
        node_strs=self.addShapes_query_strs(variables)
        for node_str in node_strs:
            nodeType_str=cmds.nodeType(node_str)
            MFnType_str,MFnTypeID_int=self.MFuType_query_str_int(node_str)
            table_lists.append([node_str,nodeType_str,MFnType_str,str(MFnTypeID_int)])
        self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
        self.table_SelfTableWidget.createTable()
    
    def editSelectionTable(self,variables):
        table_lists=self.table_SelfTableWidget.queryTableLists()
        node_strs=self.addShapes_query_strs(variables)
        for node_str in node_strs:
            nodeType_str=cmds.nodeType(node_str)
            MFnType_str,MFnTypeID_int=self.MFuType_query_str_int(node_str)
            table_lists.append([node_str,nodeType_str,MFnType_str,str(MFnTypeID_int)])
        self.table_SelfTableWidget.setDataTableWidgetLists(table_lists)
        self.table_SelfTableWidget.createTable()

    def refreshClicked(self):
        refresh_DataPath=dLB.DataPath()
        refresh_DataPath.setAbsoluteDirectory(self._reset_dir)
        refresh_DataPath.setFile("queryNodeTypesMN")
        refresh_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(refresh_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def restoreClicked(self):
        restore_DataPath=dLB.DataPath()
        restore_DataPath.setAbsoluteDirectory(self._data_dir)
        restore_DataPath.setFile("queryNodeTypesMN")
        restore_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(restore_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def saveClicked(self):
        save_DataPath=dLB.DataPath()
        save_DataPath.setAbsoluteDirectory(self._data_dir)
        save_DataPath.setFile("queryNodeTypesMN")
        save_DataPath.setExtension("json")

        getValue_dict={}
        for _setting_str in self._setting_strs:
            getValue_value=eval('self.get'+_setting_str+'()')
            getValue_dict[_setting_str]=getValue_value
            
        self.exportJson_create_func(save_DataPath,getValue_dict)

    def importClicked(self):
        import_dir,import_file=wLB.mayaPathDialog_query_dir_file(text="import setting",fileMode=1,directory=self._data_dir)
        if import_dir is None or import_file is None:
            return
        import_DataPath=dLB.DataPath()
        import_DataPath.setAbsoluteDirectory(import_dir)
        import_DataPath.setFile(import_file)
        import_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(import_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def exportClicked(self):
        export_dir,export_file=wLB.mayaPathDialog_query_dir_file(text="export setting",fileMode=0,directory=self._data_dir)
        if export_dir is None or export_file is None:
            return
        export_DataPath=dLB.DataPath()
        export_DataPath.setAbsoluteDirectory(export_dir)
        export_DataPath.setFile(export_file)
        export_DataPath.setExtension("json")
        
        getValue_dict={}
        for _setting_str in self._setting_strs:
            getValue_value=eval('self.get'+_setting_str+'()')
            getValue_dict[_setting_str]=getValue_value

        self.exportJson_create_func(export_DataPath,getValue_dict)

    def buttonLeftClicked(self):
        main()

    def buttonCenterClicked(self):
        node_strs=cmds.ls(sl=True)
        self.createSelectionTable(node_strs)

    def buttonRightClicked(self):
        node_strs=cmds.ls(sl=True)
        self.editSelectionTable(node_strs)
    
def main():
    viewWindow=QueryNodeTypeWindow(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.buttonCenterClicked()
    viewWindow.show(dockable=True,floating=True)