# -*- coding: iso-8859-15 -*-
try:
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
except ImportError:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *

import cgInTools as cit
from ..library import dataLB as dLB
from ..library import jsonLB as jLB
cit.reloads([dLB,jLB])

class ColorChengeWindouBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(ColorChengeWindouBase, self).__init__(*args, **kwargs)
        colorIndex_DataPath=dLB.DataPath()
        colorIndex_DataPath.setAbsoluteDirectory(cit.ui_dir)
        colorIndex_DataPath.setFile("ui")
        colorIndex_DataPath.setExtension("json")
        
        colorIndex_AppJson=jLB.AppJson()
        colorIndex_AppJson.setDataPath(colorIndex_DataPath)
        self.__colorIndex_dicts=colorIndex_AppJson.read().get("colorIndex_dicts")

        self.setWindowFlags(Qt.Window)

        main_QVBoxLayout=QVBoxLayout(self)

        artAttr_QHBoxLayout=self.artAttrLayout_create_QHBoxLayout()
        neutralButton_QHBoxLayout=self.neutralButtonLayout_create_QHBoxLayout()
        templateColor_QWidget=self.templateColor_create_QWidget()
        indexColor_QWidget=self.indexColor_create_QWidget()
        mgearColor_QWidget=self.mgearColor_create_QWidget()
        grisColor_QWidget=self.grisColor_create_QWidget()

        ctrlColor_QTabWidget=QTabWidget(self)
        ctrlColor_QTabWidget.addTab(templateColor_QWidget,"Default")
        ctrlColor_QTabWidget.addTab(indexColor_QWidget,"Index")
        ctrlColor_QTabWidget.addTab(mgearColor_QWidget,"Mgear")
        ctrlColor_QTabWidget.addTab(grisColor_QWidget,"Gris")

        main_QVBoxLayout.addLayout(artAttr_QHBoxLayout)
        main_QVBoxLayout.addLayout(neutralButton_QHBoxLayout)
        main_QVBoxLayout.addWidget(ctrlColor_QTabWidget)

    #Single Function
    def artAttrLayout_create_QHBoxLayout(self):
        artAttr_QHBoxLayout=QHBoxLayout(self)
        self.radioGrp_QButtonGroup=QButtonGroup()

        override_QRadioButton=QRadioButton("Override",self)
        override_QRadioButton.setChecked(True)
        self.radioGrp_QButtonGroup.addButton(override_QRadioButton,0)
        artAttr_QHBoxLayout.addWidget(override_QRadioButton)

        wireframe_QRadioButton=QRadioButton("WireFrame",self)
        self.radioGrp_QButtonGroup.addButton(wireframe_QRadioButton,1)
        artAttr_QHBoxLayout.addWidget(wireframe_QRadioButton)
        
        return artAttr_QHBoxLayout
    
    def neutralButtonLayout_create_QHBoxLayout(self):
        neutralButton_QHBoxLayout=QHBoxLayout(self)

        overrideNeutral_QPushButton=QPushButton("OverrideNeutral",self)
        overrideNeutral_QPushButton.setStyleSheet("color: gray;")
        overrideNeutral_QPushButton.clicked.connect(self.buttonOverrideNeutralClicked)
        neutralButton_QHBoxLayout.addWidget(overrideNeutral_QPushButton)

        wireNeutral_QPushButton=QPushButton("WireNeutral",self)
        wireNeutral_QPushButton.setStyleSheet("color: gray;")
        wireNeutral_QPushButton.clicked.connect(self.buttonWireNeutralClicked)
        neutralButton_QHBoxLayout.addWidget(wireNeutral_QPushButton)
        
        return neutralButton_QHBoxLayout
    
    def templateColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)

        index13_QPushButton=QPushButton("main",self)
        index13_str=self.__colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#888888; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.buttonIndex13Clicked)
        right_QVBoxLayout.addWidget(index13_QPushButton,True)

        index20_QPushButton=QPushButton("sub",self)
        index20_str=self.__colorIndex_dicts[20]["RGBFF"]
        index20_QPushButton.setStyleSheet("color:#888888; background:"+index20_str+";")
        index20_QPushButton.clicked.connect(self.buttonIndex20Clicked)
        right_QVBoxLayout.addWidget(index20_QPushButton,True)
        
        index31_QPushButton=QPushButton("support",self)
        index31_str=self.__colorIndex_dicts[31]["RGBFF"]
        index31_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index31_str+";")
        index31_QPushButton.clicked.connect(self.buttonIndex31Clicked)
        right_QVBoxLayout.addWidget(index31_QPushButton,True)
        
        index04_QPushButton=QPushButton("inside",self)
        index04_str=self.__colorIndex_dicts[4]["RGBFF"]
        index04_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index04_str+";")
        index04_QPushButton.clicked.connect(self.buttonIndex04Clicked)
        right_QVBoxLayout.addWidget(index04_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        index17_QPushButton=QPushButton("main",self)
        index17_str=self.__colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#888888; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.buttonIndex17Clicked)
        center_QVBoxLayout.addWidget(index17_QPushButton,True)

        index14_QPushButton=QPushButton("sub",self)
        index14_str=self.__colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#888888; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.buttonIndex14Clicked)
        center_QVBoxLayout.addWidget(index14_QPushButton,True)

        index27_QPushButton=QPushButton("support",self)
        index27_str=self.__colorIndex_dicts[27]["RGBFF"]
        index27_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index27_str+";")
        index27_QPushButton.clicked.connect(self.buttonIndex27Clicked)
        center_QVBoxLayout.addWidget(index27_QPushButton,True)

        index07_QPushButton=QPushButton("inside",self)
        index07_str=self.__colorIndex_dicts[7]["RGBFF"]
        index07_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index07_str+";")
        index07_QPushButton.clicked.connect(self.buttonIndex07Clicked)
        center_QVBoxLayout.addWidget(index07_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        index06_QPushButton=QPushButton("main",self)
        index06_str=self.__colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#888888; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.buttonIndex06Clicked)
        left_QVBoxLayout.addWidget(index06_QPushButton,True)

        index18_QPushButton=QPushButton("sub",self)
        index18_str=self.__colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#888888; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.buttonIndex18Clicked)
        left_QVBoxLayout.addWidget(index18_QPushButton,True)
        
        index28_QPushButton=QPushButton("support",self)
        index28_str=self.__colorIndex_dicts[28]["RGBFF"]
        index28_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index28_str+";")
        index28_QPushButton.clicked.connect(self.buttonIndex28Clicked)
        left_QVBoxLayout.addWidget(index28_QPushButton,True)
        
        index15_QPushButton=QPushButton("inside",self)
        index15_str=self.__colorIndex_dicts[15]["RGBFF"]
        index15_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index15_str+";")
        index15_QPushButton.clicked.connect(self.buttonIndex15Clicked)
        left_QVBoxLayout.addWidget(index15_QPushButton,True)

        other_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(other_QVBoxLayout,1,3)

        other_QLabel=QLabel("Other Color",self)
        other_QVBoxLayout.addWidget(other_QLabel,True)
        
        index16_QPushButton=QPushButton("main",self)
        index16_str=self.__colorIndex_dicts[16]["RGBFF"]
        index16_QPushButton.setStyleSheet("color:#888888; background:"+index16_str+";")
        index16_QPushButton.clicked.connect(self.buttonIndex16Clicked)
        other_QVBoxLayout.addWidget(index16_QPushButton,True)

        index09_QPushButton=QPushButton("sub",self)
        index09_str=self.__colorIndex_dicts[9]["RGBFF"]
        index09_QPushButton.setStyleSheet("color:#888888; background:"+index09_str+";")
        index09_QPushButton.clicked.connect(self.buttonIndex09Clicked)
        other_QVBoxLayout.addWidget(index09_QPushButton,True)

        index30_QPushButton=QPushButton("support",self)
        index30_str=self.__colorIndex_dicts[30]["RGBFF"]
        index30_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index30_str+";")
        index30_QPushButton.clicked.connect(self.buttonIndex30Clicked)
        other_QVBoxLayout.addWidget(index30_QPushButton,True)
        
        index01_QPushButton=QPushButton("inside",self)
        index01_str=self.__colorIndex_dicts[1]["RGBFF"]
        index01_QPushButton.setStyleSheet("color:#BBBBBB; background:"+index01_str+";")
        index01_QPushButton.clicked.connect(self.buttonIndex01Clicked)
        other_QVBoxLayout.addWidget(index01_QPushButton,True)
        return color_QWidget

    def indexColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        index01_QPushButton=QPushButton("1",self)
        index01_str=self.__colorIndex_dicts[1]["RGBFF"]
        index01_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index01_str+";")
        index01_QPushButton.clicked.connect(self.buttonIndex01Clicked)
        custom_QGridLayout.addWidget(index01_QPushButton,0,0)
        
        index02_QPushButton=QPushButton("2",self)
        index02_str=self.__colorIndex_dicts[2]["RGBFF"]
        index02_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index02_str+";")
        index02_QPushButton.clicked.connect(self.buttonIndex02Clicked)
        custom_QGridLayout.addWidget(index02_QPushButton,0,1)
        
        index03_QPushButton=QPushButton("3",self)
        index03_str=self.__colorIndex_dicts[3]["RGBFF"]
        index03_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index03_str+";")
        index03_QPushButton.clicked.connect(self.buttonIndex03Clicked)
        custom_QGridLayout.addWidget(index03_QPushButton,0,2)
        
        index04_QPushButton=QPushButton("4",self)
        index04_str=self.__colorIndex_dicts[4]["RGBFF"]
        index04_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index04_str+";")
        index04_QPushButton.clicked.connect(self.buttonIndex04Clicked)
        custom_QGridLayout.addWidget(index04_QPushButton,0,3)
        
        index05_QPushButton=QPushButton("5",self)
        index05_str=self.__colorIndex_dicts[5]["RGBFF"]
        index05_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index05_str+";")
        index05_QPushButton.clicked.connect(self.buttonIndex05Clicked)
        custom_QGridLayout.addWidget(index05_QPushButton,0,4)
        
        index06_QPushButton=QPushButton("6",self)
        index06_str=self.__colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.buttonIndex06Clicked)
        custom_QGridLayout.addWidget(index06_QPushButton,0,5)
        
        index07_QPushButton=QPushButton("7",self)
        index07_str=self.__colorIndex_dicts[7]["RGBFF"]
        index07_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index07_str+";")
        index07_QPushButton.clicked.connect(self.buttonIndex07Clicked)
        custom_QGridLayout.addWidget(index07_QPushButton,0,6)
        
        index08_QPushButton=QPushButton("8",self)
        index08_str=self.__colorIndex_dicts[8]["RGBFF"]
        index08_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index08_str+";")
        index08_QPushButton.clicked.connect(self.buttonIndex08Clicked)
        custom_QGridLayout.addWidget(index08_QPushButton,0,7)
        
        index09_QPushButton=QPushButton("9",self)
        index09_str=self.__colorIndex_dicts[9]["RGBFF"]
        index09_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index09_str+";")
        index09_QPushButton.clicked.connect(self.buttonIndex09Clicked)
        custom_QGridLayout.addWidget(index09_QPushButton,0,8)
        
        index10_QPushButton=QPushButton("10",self)
        index10_str=self.__colorIndex_dicts[10]["RGBFF"]
        index10_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index10_str+";")
        index10_QPushButton.clicked.connect(self.buttonIndex10Clicked)
        custom_QGridLayout.addWidget(index10_QPushButton,0,9)
        
        index11_QPushButton=QPushButton("11",self)
        index11_str=self.__colorIndex_dicts[11]["RGBFF"]
        index11_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index11_str+";")
        index11_QPushButton.clicked.connect(self.buttonIndex11Clicked)
        custom_QGridLayout.addWidget(index11_QPushButton,1,0)
        
        index12_QPushButton=QPushButton("12",self)
        index12_str=self.__colorIndex_dicts[12]["RGBFF"]
        index12_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index12_str+";")
        index12_QPushButton.clicked.connect(self.buttonIndex12Clicked)
        custom_QGridLayout.addWidget(index12_QPushButton,1,1)
        
        index13_QPushButton=QPushButton("13",self)
        index13_str=self.__colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.buttonIndex13Clicked)
        custom_QGridLayout.addWidget(index13_QPushButton,1,2)
        
        index14_QPushButton=QPushButton("14",self)
        index14_str=self.__colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.buttonIndex14Clicked)
        custom_QGridLayout.addWidget(index14_QPushButton,1,3)
        
        index15_QPushButton=QPushButton("15",self)
        index15_str=self.__colorIndex_dicts[15]["RGBFF"]
        index15_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index15_str+";")
        index15_QPushButton.clicked.connect(self.buttonIndex15Clicked)
        custom_QGridLayout.addWidget(index15_QPushButton,1,4)
        
        index16_QPushButton=QPushButton("16",self)
        index16_str=self.__colorIndex_dicts[16]["RGBFF"]
        index16_QPushButton.setStyleSheet("color:#202020; background:"+index16_str+";")
        index16_QPushButton.clicked.connect(self.buttonIndex16Clicked)
        custom_QGridLayout.addWidget(index16_QPushButton,1,5)
        
        index17_QPushButton=QPushButton("17",self)
        index17_str=self.__colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.buttonIndex17Clicked)
        custom_QGridLayout.addWidget(index17_QPushButton,1,6)
        
        index18_QPushButton=QPushButton("18",self)
        index18_str=self.__colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.buttonIndex18Clicked)
        custom_QGridLayout.addWidget(index18_QPushButton,1,7)
        
        index19_QPushButton=QPushButton("19",self)
        index19_str=self.__colorIndex_dicts[19]["RGBFF"]
        index19_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index19_str+";")
        index19_QPushButton.clicked.connect(self.buttonIndex19Clicked)
        custom_QGridLayout.addWidget(index19_QPushButton,1,8)
        
        index20_QPushButton=QPushButton("20",self)
        index20_str=self.__colorIndex_dicts[20]["RGBFF"]
        index20_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index20_str+";")
        index20_QPushButton.clicked.connect(self.buttonIndex20Clicked)
        custom_QGridLayout.addWidget(index20_QPushButton,1,9)
        
        index21_QPushButton=QPushButton("21",self)
        index21_str=self.__colorIndex_dicts[21]["RGBFF"]
        index21_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index21_str+";")
        index21_QPushButton.clicked.connect(self.buttonIndex21Clicked)
        custom_QGridLayout.addWidget(index21_QPushButton,2,0)
        
        index22_QPushButton=QPushButton("22",self)
        index22_str=self.__colorIndex_dicts[22]["RGBFF"]
        index22_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index22_str+";")
        index22_QPushButton.clicked.connect(self.buttonIndex22Clicked)
        custom_QGridLayout.addWidget(index22_QPushButton,2,1)
        
        index23_QPushButton=QPushButton("23",self)
        index23_str=self.__colorIndex_dicts[23]["RGBFF"]
        index23_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index23_str+";")
        index23_QPushButton.clicked.connect(self.buttonIndex23Clicked)
        custom_QGridLayout.addWidget(index23_QPushButton,2,2)
        
        index24_QPushButton=QPushButton("24",self)
        index24_str=self.__colorIndex_dicts[24]["RGBFF"]
        index24_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index24_str+";")
        index24_QPushButton.clicked.connect(self.buttonIndex24Clicked)
        custom_QGridLayout.addWidget(index24_QPushButton,2,3)
        
        index25_QPushButton=QPushButton("25",self)
        index25_str=self.__colorIndex_dicts[25]["RGBFF"]
        index25_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index25_str+";")
        index25_QPushButton.clicked.connect(self.buttonIndex25Clicked)
        custom_QGridLayout.addWidget(index25_QPushButton,2,4)
        
        index26_QPushButton=QPushButton("26",self)
        index26_str=self.__colorIndex_dicts[26]["RGBFF"]
        index26_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index26_str+";")
        index26_QPushButton.clicked.connect(self.buttonIndex26Clicked)
        custom_QGridLayout.addWidget(index26_QPushButton,2,5)
        
        index27_QPushButton=QPushButton("27",self)
        index27_str=self.__colorIndex_dicts[27]["RGBFF"]
        index27_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index27_str+";")
        index27_QPushButton.clicked.connect(self.buttonIndex27Clicked)
        custom_QGridLayout.addWidget(index27_QPushButton,2,6)
        
        index28_QPushButton=QPushButton("28",self)
        index28_str=self.__colorIndex_dicts[28]["RGBFF"]
        index28_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index28_str+";")
        index28_QPushButton.clicked.connect(self.buttonIndex28Clicked)
        custom_QGridLayout.addWidget(index28_QPushButton,2,7)
        
        index29_QPushButton=QPushButton("29",self)
        index29_str=self.__colorIndex_dicts[29]["RGBFF"]
        index29_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index29_str+";")
        index29_QPushButton.clicked.connect(self.buttonIndex29Clicked)
        custom_QGridLayout.addWidget(index29_QPushButton,2,8)
        
        index30_QPushButton=QPushButton("30",self)
        index30_str=self.__colorIndex_dicts[30]["RGBFF"]
        index30_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index30_str+";")
        index30_QPushButton.clicked.connect(self.buttonIndex30Clicked)
        custom_QGridLayout.addWidget(index30_QPushButton,2,9)
        
        index31_QPushButton=QPushButton("31",self)
        index31_str=self.__colorIndex_dicts[31]["RGBFF"]
        index31_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index31_str+";")
        index31_QPushButton.clicked.connect(self.buttonIndex31Clicked)
        custom_QGridLayout.addWidget(index31_QPushButton,3,0)
        return color_QWidget
    
    def mgearColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        right_QVBoxLayout.addStretch(1)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)

        index23_QPushButton=QPushButton("FK",self)
        index23_str=self.__colorIndex_dicts[23]["RGBFF"]
        index23_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index23_str+";")
        index23_QPushButton.clicked.connect(self.buttonIndex23Clicked)
        right_QVBoxLayout.addWidget(index23_QPushButton,True)

        index14_QPushButton=QPushButton("IK",self)
        index14_str=self.__colorIndex_dicts[14]["RGBFF"]
        index14_QPushButton.setStyleSheet("color:#202020; background:"+index14_str+";")
        index14_QPushButton.clicked.connect(self.buttonIndex14Clicked)
        right_QVBoxLayout.addWidget(index14_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        center_QVBoxLayout.addStretch(1)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        index13_QPushButton=QPushButton("FK",self)
        index13_str=self.__colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.buttonIndex13Clicked)
        center_QVBoxLayout.addWidget(index13_QPushButton,True)

        index17_QPushButton=QPushButton("IK",self)
        index17_str=self.__colorIndex_dicts[17]["RGBFF"]
        index17_QPushButton.setStyleSheet("color:#202020; background:"+index17_str+";")
        index17_QPushButton.clicked.connect(self.buttonIndex17Clicked)
        center_QVBoxLayout.addWidget(index17_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        left_QVBoxLayout.addStretch(1)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        index06_QPushButton=QPushButton("FK",self)
        index06_str=self.__colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.buttonIndex06Clicked)
        left_QVBoxLayout.addWidget(index06_QPushButton,True)

        index18_QPushButton=QPushButton("IK",self)
        index18_str=self.__colorIndex_dicts[18]["RGBFF"]
        index18_QPushButton.setStyleSheet("color:#202020; background:"+index18_str+";")
        index18_QPushButton.clicked.connect(self.buttonIndex18Clicked)
        left_QVBoxLayout.addWidget(index18_QPushButton,True)
        return color_QWidget
    
    def grisColor_create_QWidget(self):
        color_QWidget=QWidget()
        custom_QGridLayout=QGridLayout(self)
        color_QWidget.setLayout(custom_QGridLayout)

        right_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(right_QVBoxLayout,1,0)

        right_QLabel=QLabel("Right Color",self)
        right_QVBoxLayout.addWidget(right_QLabel,True)

        index04_QPushButton=QPushButton("main",self)
        index04_str=self.__colorIndex_dicts[4]["RGBFF"]
        index04_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index04_str+";")
        index04_QPushButton.clicked.connect(self.buttonIndex04Clicked)
        right_QVBoxLayout.addWidget(index04_QPushButton,True)

        index09_QPushButton=QPushButton("sub",self)
        index09_str=self.__colorIndex_dicts[9]["RGBFF"]
        index09_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index09_str+";")
        index09_QPushButton.clicked.connect(self.buttonIndex09Clicked)
        right_QVBoxLayout.addWidget(index09_QPushButton,True)
        
        index30_QPushButton=QPushButton("support",self)
        index30_str=self.__colorIndex_dicts[30]["RGBFF"]
        index30_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index30_str+";")
        index30_QPushButton.clicked.connect(self.buttonIndex30Clicked)
        right_QVBoxLayout.addWidget(index30_QPushButton,True)

        center_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(center_QVBoxLayout,1,1)

        center_QLabel=QLabel("Center Color",self)
        center_QVBoxLayout.addWidget(center_QLabel,True)

        index33_QPushButton=QPushButton("main",self)
        index33_str=self.__colorIndex_dicts[33]["RGBFF"]
        index33_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index33_str+";")
        index33_QPushButton.clicked.connect(self.buttonIndex33Clicked)
        center_QVBoxLayout.addWidget(index33_QPushButton,True)

        index23_QPushButton=QPushButton("sub",self)
        index23_str=self.__colorIndex_dicts[23]["RGBFF"]
        index23_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index23_str+";")
        index23_QPushButton.clicked.connect(self.buttonIndex23Clicked)
        center_QVBoxLayout.addWidget(index23_QPushButton,True)

        index13_QPushButton=QPushButton("support",self)
        index13_str=self.__colorIndex_dicts[13]["RGBFF"]
        index13_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index13_str+";")
        index13_QPushButton.clicked.connect(self.buttonIndex13Clicked)
        center_QVBoxLayout.addWidget(index13_QPushButton,True)
        
        left_QVBoxLayout=QVBoxLayout(self)
        custom_QGridLayout.addLayout(left_QVBoxLayout,1,2)
        
        left_QLabel=QLabel("Left Color",self)
        left_QVBoxLayout.addWidget(left_QLabel,True)

        index06_QPushButton=QPushButton("main",self)
        index06_str=self.__colorIndex_dicts[6]["RGBFF"]
        index06_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index06_str+";")
        index06_QPushButton.clicked.connect(self.buttonIndex06Clicked)
        left_QVBoxLayout.addWidget(index06_QPushButton,True)

        index28_QPushButton=QPushButton("sub",self)
        index28_str=self.__colorIndex_dicts[28]["RGBFF"]
        index28_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index28_str+";")
        index28_QPushButton.clicked.connect(self.buttonIndex28Clicked)
        left_QVBoxLayout.addWidget(index28_QPushButton,True)
        
        index29_QPushButton=QPushButton("support",self)
        index29_str=self.__colorIndex_dicts[29]["RGBFF"]
        index29_QPushButton.setStyleSheet("color:#f5f5f5; background:"+index29_str+";")
        index29_QPushButton.clicked.connect(self.buttonIndex29Clicked)
        left_QVBoxLayout.addWidget(index29_QPushButton,True)
        return color_QWidget

    #Public Function
    def buttonIndex01Clicked(self):
        print(1)
    def buttonIndex02Clicked(self):
        print(2)
    def buttonIndex03Clicked(self):
        print(3)
    def buttonIndex04Clicked(self):
        print(4)
    def buttonIndex05Clicked(self):
        print(5)
    def buttonIndex06Clicked(self):
        print(6)
    def buttonIndex07Clicked(self):
        print(7)
    def buttonIndex08Clicked(self):
        print(8)
    def buttonIndex09Clicked(self):
        print(9)
    def buttonIndex10Clicked(self):
        print(10)
    def buttonIndex11Clicked(self):
        print(11)
    def buttonIndex12Clicked(self):
        print(12)
    def buttonIndex13Clicked(self):
        print(13)
    def buttonIndex14Clicked(self):
        print(14)
    def buttonIndex15Clicked(self):
        print(15)
    def buttonIndex16Clicked(self):
        print(16)
    def buttonIndex17Clicked(self):
        print(17)
    def buttonIndex18Clicked(self):
        print(18)
    def buttonIndex19Clicked(self):
        print(19)
    def buttonIndex20Clicked(self):
        print(20)
    def buttonIndex21Clicked(self):
        print(21)
    def buttonIndex22Clicked(self):
        print(22)
    def buttonIndex23Clicked(self):
        print(23)
    def buttonIndex24Clicked(self):
        print(24)
    def buttonIndex25Clicked(self):
        print(25)
    def buttonIndex26Clicked(self):
        print(26)
    def buttonIndex27Clicked(self):
        print(27)
    def buttonIndex28Clicked(self):
        print(28)
    def buttonIndex29Clicked(self):
        print(29)
    def buttonIndex30Clicked(self):
        print(30)
    def buttonIndex31Clicked(self):
        print(31)
    def buttonIndex32Clicked(self):
        print(32)
    def buttonIndex33Clicked(self):
        print(33)
    def buttonIndex34Clicked(self):
        print(34)
    def buttonIndex35Clicked(self):
        print(35)
    def buttonIndex36Clicked(self):
        print(36)
    def buttonIndex37Clicked(self):
        print(37)
    def buttonIndex38Clicked(self):
        print(38)
    def buttonIndex39Clicked(self):
        print(39)
    def buttonOverrideNeutralClicked(self):
        print("OverrideNeutral")
    def buttonWireNeutralClicked(self):
        print("WireNeutral")

#viewWindow=ColorChengeWindouBase()
#viewWindow.show()
