# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import maya.cmds as cmds

import cgInTools as cit
from ...ui import autoNodeRenameUI as UI
from ...library import dataLB as dLB
from ...library import jsonLB as jLB
from ..library import windowLB as wLB
from ..library import nameLB as nnLB
from ..library import nodeLB as nLB
cit.reloads([UI,dLB,jLB,wLB,nnLB,nLB])

DATAFOLDER_STR="autoNodeRename"
RESET_DIR,DATA_DIR=cit.checkScriptsData(DATAFOLDER_STR,cit.maya_dir,cit.mayaData_dir)

class AutoNodeRenameOP(UI.AutoNodeRenameBase):
    def __init__(self,*args,**kwargs):
        self._setting_strs=[
            "ModeSwitch",
            "ComboBoxOrders",
            "CustomText",
            "TitleText",
            "NodeText",
            "SideText"
        ]
        super().__init__(*args,**kwargs)
        self._dataFolder_str=DATAFOLDER_STR
        self._reset_dir=RESET_DIR
        self._data_dir=DATA_DIR

    #Single Function
    def importJson_query_dict(self,dataPath):
        setting=jLB.AppJson()
        setting.setDataPath(dataPath)
        settings_dict=setting.read()
        return settings_dict
    
    def exportJson_create_func(self,dataPath,switch,custom,title,node,side,orders):
        write_dict={
            "ModeSwitch":switch,
            "CustomText":custom,
            "TitleText":title,
            "NodeText":node,
            "SideText":side,
            "ComboBoxOrders":orders
        }
        setting=jLB.AppJson()
        setting.setDataPath(dataPath)
        setting.setJsonDict(write_dict)
        setting.write()

    #Setting Function
    def setModeSwitch(self,variable):
        modeSwitch_QAbstractButton=self.radioGrp_QButtonGroup.button(variable)
        modeSwitch_QAbstractButton.setChecked(True)
    def getModeSwitch(self):
        modeSwitch_int=self.radioGrp_QButtonGroup.checkedId()
        return modeSwitch_int
    
    def setComboBoxOrders(self,variables):
        self.name01_QComboBox.setCurrentText(variables[0])
        self.name02_QComboBox.setCurrentText(variables[1])
        self.name03_QComboBox.setCurrentText(variables[2])
        self.name04_QComboBox.setCurrentText(variables[3])
        self.name05_QComboBox.setCurrentText(variables[4])
    def getComboBoxOrders(self):
        name01_str=self.name01_QComboBox.currentText()
        name02_str=self.name02_QComboBox.currentText()
        name03_str=self.name03_QComboBox.currentText()
        name04_str=self.name04_QComboBox.currentText()
        name05_str=self.name05_QComboBox.currentText()
        order_strs=[name01_str,name02_str,name03_str,name04_str,name05_str]
        order_strs=[order_str for order_str in order_strs if order_str not in "None"]
        return order_strs
    
    def setCustomText(self,variable):
        self.custom_QLineEdit.setText(variable)
    def getCustomText(self):
        custom_str=self.custom_QLineEdit.text()
        if custom_str is "":
            return None
        return custom_str
    
    def setTitleText(self,variable):
        self.title_QLineEdit.setText(variable)
    def getTitleText(self):
        title_str=self.title_QLineEdit.text()
        if title_str is "":
            return None
        return title_str
    
    def setNodeText(self,variable):
        self.node_QLineEdit.setText(variable)
    def getNodeText(self):
        node_str=self.node_QLineEdit.text()
        if node_str is "":
            return None
        return node_str
    
    def setSideText(self,variable):
        self.side_QLineEdit.setText(variable)
    def getSideText(self):
        side_str=self.side_QLineEdit.text()
        if side_str is "":
            return None
        return side_str

    #Public Function
    def refreshClicked(self):
        refresh_DataPath=dLB.DataPath()
        refresh_DataPath.setAbsoluteDirectory(self._reset_dir)
        refresh_DataPath.setFile("autoNodeRenameOP")
        refresh_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(refresh_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def restoreClicked(self):
        restore_DataPath=dLB.DataPath()
        restore_DataPath.setAbsoluteDirectory(self._data_dir)
        restore_DataPath.setFile("autoNodeRenameOP")
        restore_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(restore_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def saveClicked(self):
        save_DataPath=dLB.DataPath()
        save_DataPath.setAbsoluteDirectory(self._data_dir)
        save_DataPath.setFile("autoNodeRenameOP")
        save_DataPath.setExtension("json")

        getValue_values=[]
        for _setting_str in self._setting_strs:
            getValue_value=eval('self.get'+_setting_str+'()')
            getValue_values.append(getValue_value)
            
        self.exportJson_create_func(
            dataPath=save_DataPath,
            switch=getValue_values[0],
            orders=getValue_values[1],
            custom=getValue_values[2],
            title=getValue_values[3],
            node=getValue_values[4],
            side=getValue_values[5]
        )

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
        
        getValue_values=[]
        for _setting_str in self._setting_strs:
            getValue_value=eval('self.get'+_setting_str+'()')
            getValue_values.append(getValue_value)
            
        self.exportJson_create_func(
            dataPath=export_DataPath,
            switch=getValue_values[0],
            orders=getValue_values[1],
            custom=getValue_values[2],
            title=getValue_values[3],
            node=getValue_values[4],
            side=getValue_values[5]
        )

    def buttonLeftClicked(self):
        node_DataPath=dLB.DataPath()
        node_DataPath.setAbsoluteDirectory(cit.mayaData_dir)
        node_DataPath.setRelativeDirectory("autoNodeRename")
        node_DataPath.setFile("autoNodeRenameEX")
        node_DataPath.setExtension("json")

        node_DataNodeName=nnLB.DataNodeName()
        node_DataNodeName.setOriginDataPath(node_DataPath)
        node_DataNodeName.setTitle(self.getTitleText())
        node_DataNodeName.setNodeType(self.getNodeText())
        node_DataNodeName.setSide(self.getSideText())
        node_DataNodeName.setNumbers([0])
        node_DataNodeName.setHierarchys(["A"])
        node_DataNodeName.setCustoms([self.getCustomText()])
        node_DataNodeName.setOrders(self.getComboBoxOrders())
        node_DataNodeName.setIncrease(None)
        node_DataNodeName.writeJson()

        objs=cmds.ls(sl=True)
        for obj in objs:
            node_DataNode=nLB.DataNode()
            node_DataNode.setName(obj)

            node_AppNodeName=nLB.SelfDGNode()
            node_AppNodeName.setDataNode(node_DataNode)
            node_AppNodeName.setDataNodeName(node_DataNodeName)
            if self.getModeSwitch() is 0:
                node_AppNodeName.autoRename()
            elif self.getModeSwitch() is 1:
                node_AppNodeName.editRename()
        self.close()

    def buttonCenterClicked(self):
        node_DataPath=dLB.DataPath()
        node_DataPath.setAbsoluteDirectory(cit.mayaData_dir)
        node_DataPath.setRelativeDirectory("autoNodeRename")
        node_DataPath.setFile("autoNodeRenameEX")
        node_DataPath.setExtension("json")

        node_DataNodeName=nnLB.DataNodeName()
        node_DataNodeName.setOriginDataPath(node_DataPath)
        node_DataNodeName.setTitle(self.getTitleText())
        node_DataNodeName.setNodeType(self.getNodeText())
        node_DataNodeName.setSide(self.getSideText())
        node_DataNodeName.setNumbers([0])
        node_DataNodeName.setHierarchys(["A"])
        node_DataNodeName.setCustoms([self.getCustomText()])
        node_DataNodeName.setOrders(self.getComboBoxOrders())
        node_DataNodeName.setIncrease(None)
        node_DataNodeName.writeJson()

        objs=cmds.ls(sl=True)
        for obj in objs:
            node_DataNode=nLB.DataNode()
            node_DataNode.setName(obj)

            node_AppNodeName=nLB.SelfDGNode()
            node_AppNodeName.setDataNode(node_DataNode)
            node_AppNodeName.setDataNodeName(node_DataNodeName)
            if self.getModeSwitch() is 0:
                node_AppNodeName.autoRename()
            elif self.getModeSwitch() is 1:
                node_AppNodeName.editRename()

    def buttonRightClicked(self):
        self.close()

def main():
    viewWindow=AutoNodeRenameOP(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.show()
