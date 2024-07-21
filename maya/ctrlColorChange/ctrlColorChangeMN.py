# -*- coding: iso-8859-15 -*-
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

import maya.cmds as cmds

import cgInTools as cit
from ...ui import ctrlColorChengeUI as UI
from ..library import windowLB as wLB
from ..library import colorLB as cLB
cit.reloads([UI,wLB,cLB])

class ColorChangeWindow(UI.ColorChengeWindouBase):
    def __init__(self,parent):
        super(ColorChangeWindow,self).__init__(parent)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("ctrlColorChenge")

    #Single Function
    @staticmethod
    def changeColor_edit_func(color_value,swicth_int=0):
        change_AppColor=cLB.AppColor()
        change_AppColor.setColor(color_value)
        sel_strs=cmds.ls(sl=True)
        for sel_str in sel_strs:
            change_AppColor.setNode(sel_str)
            if swicth_int is 0:
                change_AppColor.overrideColor()
            elif swicth_int is 1:
                change_AppColor.wireframeColor()

    #Public Function
    def buttonIndex01Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(1,colorSwicth_int)
    def buttonIndex02Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(2,colorSwicth_int)
    def buttonIndex03Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(3,colorSwicth_int)
    def buttonIndex04Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(4,colorSwicth_int)
    def buttonIndex05Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(5,colorSwicth_int)
    def buttonIndex06Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(6,colorSwicth_int)
    def buttonIndex07Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(7,colorSwicth_int)
    def buttonIndex08Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(8,colorSwicth_int)
    def buttonIndex09Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(9,colorSwicth_int)
    def buttonIndex10Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(10,colorSwicth_int)
    def buttonIndex11Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(11,colorSwicth_int)
    def buttonIndex12Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(12,colorSwicth_int)
    def buttonIndex13Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(13,colorSwicth_int)
    def buttonIndex14Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(14,colorSwicth_int)
    def buttonIndex15Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(15,colorSwicth_int)
    def buttonIndex16Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(16,colorSwicth_int)
    def buttonIndex17Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(17,colorSwicth_int)
    def buttonIndex18Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(18,colorSwicth_int)
    def buttonIndex19Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(19,colorSwicth_int)
    def buttonIndex20Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(20,colorSwicth_int)
    def buttonIndex21Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(21,colorSwicth_int)
    def buttonIndex22Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(22,colorSwicth_int)
    def buttonIndex23Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(23,colorSwicth_int)
    def buttonIndex24Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(24,colorSwicth_int)
    def buttonIndex25Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(25,colorSwicth_int)
    def buttonIndex26Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(26,colorSwicth_int)
    def buttonIndex27Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(27,colorSwicth_int)
    def buttonIndex28Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(28,colorSwicth_int)
    def buttonIndex29Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(29,colorSwicth_int)
    def buttonIndex30Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(30,colorSwicth_int)
    def buttonIndex31Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(31,colorSwicth_int)
    
    def buttonIndex32Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(32,colorSwicth_int)
    def buttonIndex33Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(33,colorSwicth_int)
    def buttonIndex34Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(34,colorSwicth_int)
    def buttonIndex35Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(35,colorSwicth_int)
    def buttonIndex36Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(36,colorSwicth_int)
    def buttonIndex37Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(37,colorSwicth_int)
    def buttonIndex38Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(38,colorSwicth_int)
    def buttonIndex39Clicked(self):
        colorSwicth_int=self.radioGrp_QButtonGroup.checkedId()
        self.changeColor_edit_func(39,colorSwicth_int)

    def buttonOverrideNeutralClicked(self):
        self.changeColor_edit_func(None,0)#OverrideNeutral
    def buttonWireNeutralClicked(self):
        self.changeColor_edit_func(None,1)#WireFrameNeutral

def main():
    mayaWindow=ColorChangeWindow(parent=wLB.mayaMainWindow_query_QWidget())
    mayaWindow.show()