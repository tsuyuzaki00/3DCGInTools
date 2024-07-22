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
import random
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

import cgInTools as cit
from ...ui import plainTextUI as UI
from ...library import dataLB as dLB
from ..library import windowLB as wLB
cit.reloads([UI,dLB,wLB])

DATAFOLDER_STR="querySelections"
RESET_DIR,DATA_DIR=cit.checkScriptsData(DATAFOLDER_STR,cit.maya_dir,cit.mayaData_dir)

class QuerySelectionsWindow(MayaQWidgetDockableMixin,UI.PlainTextWindowBase):
    def __init__(self,parent):
        self._setting_strs=[
            "SelectionText"
        ]
        super(QuerySelectionsWindow, self).__init__(parent)
        self._dataFolder_str=DATAFOLDER_STR
        self._reset_dir=RESET_DIR
        self._data_dir=DATA_DIR

        windowTitle_str="querySelections"
        random_int=random.randint(0,9999)
        self.setObjectName(windowTitle_str+str(random_int))
        self.setWindowTitle(windowTitle_str)
        
        self.buttonLeft_QPushButton.setText("Selection")
        self.buttonCenter_QPushButton.setText("Select Replace")
        self.buttonRight_QPushButton.setText("Select Add")

    #Single Function
    @staticmethod
    def convertListToString_edit_str(text_strs):
        text_str=""
        if not text_strs is []:
            for num,text in enumerate(text_strs):
                if num == 0:
                    text_str="[\n"
                text_str+='    "'+text+'",\n'
                if num == len(text_strs)-1:
                    text_str=text_str.rstrip(",\n")
                    text_str+="\n]"
        return text_str

    @staticmethod
    def convertStringToList_edit_strs(listText_str):
        text_strs=[]
        if not listText_str is "":
            text_strs=eval(listText_str)
        return text_strs
    
    @staticmethod
    def organizeList_edit_strs(text_list2s=[[],[]]):
        text_strs=[]
        for text_list2 in text_list2s:
            text_strs.extend(text_list2)
            text_strs=list(set(text_strs))
        return text_strs

    #Setting Function
    def setSelectionText(self,variables):
        variables.sort()
        text_str=self.convertListToString_edit_str(variables)
        self.textPlain_QPlainTextEdit.setPlainText(text_str)
    def addSelectionText(self,variables):
        organizeText_strs=variables
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        addText_strs=self.convertStringToList_edit_strs(getText_str)
        organizeText_strs=self.organizeList_edit_strs([addText_strs,variables])
        organizeText_strs.sort()
        text_str=self.convertListToString_edit_str(organizeText_strs)
        self.textPlain_QPlainTextEdit.setPlainText(text_str)
    def getSelectionText(self):
        getText_str=self.textPlain_QPlainTextEdit.toPlainText()
        text_strs=self.convertStringToList_edit_strs(getText_str)
        return text_strs
    
    #Public Function
    def refreshClicked(self):
        refresh_DataPath=dLB.DataPath()
        refresh_DataPath.setAbsoluteDirectory(self._reset_dir)
        refresh_DataPath.setFile("querySelectionsMN")
        refresh_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(refresh_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def restoreClicked(self):
        restore_DataPath=dLB.DataPath()
        restore_DataPath.setAbsoluteDirectory(self._data_dir)
        restore_DataPath.setFile("querySelectionsMN")
        restore_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(restore_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def saveClicked(self):
        save_DataPath=dLB.DataPath()
        save_DataPath.setAbsoluteDirectory(self._data_dir)
        save_DataPath.setFile("querySelectionsMN")
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
        text_strs=self.getSelectionText()
        if not text_strs==[]:
            for text_str in text_strs:
                if cmds.objExists(text_str):
                    cmds.select(text_str,add=True)

    def buttonCenterClicked(self):
        node_strs=cmds.ls(sl=True)
        if not node_strs==[]:
            self.setSelectionText(node_strs)

    def buttonRightClicked(self):
        node_strs=cmds.ls(sl=True)
        if not node_strs==[]:
            self.addSelectionText(node_strs)

def main():
    viewWindow=QuerySelectionsWindow(parent=wLB.mayaMainWindow_query_QWidget())
    node_strs=cmds.ls(sl=True)
    if not node_strs==[]:
        viewWindow.setSelectionText(node_strs)
    viewWindow.show(dockable=True,floating=True)
