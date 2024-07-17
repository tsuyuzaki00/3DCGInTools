# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import cgInTools as cit
from ...ui import autoNodeRenameUI as UI
from ...library import jsonLB as jLB
from ..library import windowLB as wLB
from ...library import dataLB as dLB
from ..library import nameLB as nnLB
from ..library import nodeLB as nLB
cit.reloads([UI,jLB,wLB])

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

    #Private Function
    def __replaceListWithUI_edit_func(self,settings_dict):
        naming_list=settings_dict["nameOrderList"]
        self.name01_QComboBox.setCurrentText(naming_list[0])
        self.name02_QComboBox.setCurrentText(naming_list[1])
        self.name03_QComboBox.setCurrentText(naming_list[2])
        self.name04_QComboBox.setCurrentText(naming_list[3])
        self.name05_QComboBox.setCurrentText(naming_list[4])

        custom_str=settings_dict["customText"]
        self.custom_QLineEdit.setText(custom_str)

        title_str=settings_dict["titleText"]
        self.title_QLineEdit.setText(title_str)
        
        node_str=settings_dict["nodeText"]
        self.node_QLineEdit.setText(node_str)
        
        side_str=settings_dict["sideText"]
        self.side_QLineEdit.setText(side_str)
        
        switch_str=settings_dict["modeSwitch"]
        if switch_str == "fullAuto":
            self.fullAuto_QRadioButton.setChecked(True)
        elif switch_str == "setAuto":
            self.setAuto_QRadioButton.setChecked(True)
        elif switch_str == "markAuto":
            self.mark_QRadioButton.setChecked(True)
        else:
            self.fullAuto_QRadioButton.setChecked(True)

    def __modeSwitch_query_str(self):
        modeSwitch=self.radioGrp_QButtonGroup.checkedButton().text()
        return modeSwitch
    
    def __lineText_query_dict(self):
        custom=self.custom_QLineEdit.text()
        title=self.title_QLineEdit.text()
        node=self.node_QLineEdit.text()
        side=self.side_QLineEdit.text()
        lineText_dict={"custom":custom,"title":title,"node":node,"side":side}
        return lineText_dict

    def __replaceComboBox_query_list(self):
        name01=self.name01_QComboBox.currentText()
        name02=self.name02_QComboBox.currentText()
        name03=self.name03_QComboBox.currentText()
        name04=self.name04_QComboBox.currentText()
        name05=self.name05_QComboBox.currentText()
        order_list=[name01,name02,name03,name04,name05]
        return order_list

    #Summary Function
    def __importJson(self,path,file):
        settings_dict=self.importJson_query_dict(path,file)
        self.__replaceListWithUI_edit_func(settings_dict)

    def __exportJson(self,path,file):
        switch=self.__modeSwitch_query_str()
        lineText_dict=self.__lineText_query_dict()
        order_list=self.__replaceComboBox_query_list()
        self.exportJson_edit_func(path,file,switch,lineText_dict["custom"],lineText_dict["title"],lineText_dict["node"],lineText_dict["side"],order_list)
    
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
        return order_strs
    
    def setCustomText(self,variable):
        self.custom_QLineEdit.setText(variable)
    def getCustomText(self):
        custom_str=self.custom_QLineEdit.text()
        return custom_str
    
    def setTitleText(self,variable):
        self.title_QLineEdit.setText(variable)
    def getTitleText(self):
        title_str=self.title_QLineEdit.text()
        return title_str
    
    def setNodeText(self,variable):
        self.node_QLineEdit.setText(variable)
    def getNodeText(self):
        node_str=self.node_QLineEdit.text()
        return node_str
    
    def setSideText(self,variable):
        self.side_QLineEdit.setText(variable)
    def getSideText(self):
        side_str=self.side_QLineEdit.text()
        return side_str

    #Public Function
    def refreshClicked(self):
        refresh_DataPath=dLB.DataPath()
        refresh_DataPath.setAbsoluteDirectory(self._reset_dir)
        refresh_DataPath.setRelativeDirectory("autoNodeRename")
        refresh_DataPath.setFile("autoNodeRenameOP")
        refresh_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(refresh_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def restoreClicked(self):
        restore_DataPath=dLB.DataPath()
        restore_DataPath.setAbsoluteDirectory(self._data_dir)
        restore_DataPath.setRelativeDirectory("autoNodeRename")
        restore_DataPath.setFile("autoNodeRenameOP")
        restore_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(restore_DataPath)
        for _setting_str in self._setting_strs:
            exec('self.set'+_setting_str+'(settings_dict.get("'+_setting_str+'"))')

    def saveClicked(self):
        save_DataPath=dLB.DataPath()
        save_DataPath.setAbsoluteDirectory(self._data_dir)
        save_DataPath.setRelativeDirectory("autoNodeRename")
        save_DataPath.setFile("autoNodeRenameOP")
        save_DataPath.setExtension("json")

        getValue_values=[exit('self.get'+_setting_str+'()') for _setting_str in self._setting_strs]
        self.exportJson_create_func(save_DataPath)

    def importClicked(self):
        import_dict=wLB.mayaPathDialog_query_dict(text="import setting",fileMode=1,directory=self._data_dir)
        if import_dict is None:
            return
        import_DataPath=dLB.DataPath()
        import_DataPath.setAbsoluteDirectory(import_dict["directory"])
        import_DataPath.setFile(import_dict["file"])
        import_DataPath.setExtension("json")

        settings_dict=self.importJson_query_dict(import_DataPath)


    def exportClicked(self):
        export_dict=wLB.mayaPathDialog_query_dict(text="export setting",fileMode=0,directory=self._data_dir)
        if export_dict is None:
            return
        export_DataPath=dLB.DataPath()
        export_DataPath.setAbsoluteDirectory(export_dict["directory"])
        export_DataPath.setFile(export_dict["file"])
        export_DataPath.setExtension("json")
        

        self.exportJson_create_func(export_DataPath,)

    def buttonLeftClicked(self):
        self.__exportJson(self._pathSet,self._file)
        EX.main()
        self.close()

    def buttonCenterClicked(self):
        self.__exportJson(self._pathSet,self._file)
        EX.main()

    def buttonRightClicked(self):
        self.close()

def main():
    viewWindow=AutoNodeRenameOP(parent=wLB.mayaMainWindow_query_QWidget())
    viewWindow.show()
