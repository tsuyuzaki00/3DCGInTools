# -*- coding: iso-8859-15 -*-

try:
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
except ImportError:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *

from . import baseUI as UI

class AutoNodeRenameBase(UI.MainWindowBase):
    def __init__(self,*args,**kwargs):
        super(AutoNodeRenameBase,self).__init__(*args, **kwargs)
        self.setObjectName("autoRename")
        self.setWindowTitle("autoRenameOption")
        self.buttonLeft_QPushButton.setText("run")
        self.buttonCenter_QPushButton.setText("apply")
        self.buttonRight_QPushButton.setText("close")

        main_QVBoxLayout=QVBoxLayout(self)
        
        central_QWidget=QWidget()
        central_QWidget.setLayout(main_QVBoxLayout)
        self.custom_QScrollArea.setWidget(central_QWidget)

        modeSwitch_QHBoxLayout=QHBoxLayout(self)
        main_QVBoxLayout.addLayout(modeSwitch_QHBoxLayout)

        self.radioGrp_QButtonGroup=QButtonGroup()

        self.fullAuto_QRadioButton=QRadioButton("fullAuto",self)
        #self.fullAuto_QRadioButton.setChecked(True)
        self.radioGrp_QButtonGroup.addButton(self.fullAuto_QRadioButton,0)
        modeSwitch_QHBoxLayout.addWidget(self.fullAuto_QRadioButton)

        self.setAuto_QRadioButton=QRadioButton("setAuto",self)
        self.setAuto_QRadioButton.setChecked(True)
        self.radioGrp_QButtonGroup.addButton(self.setAuto_QRadioButton,1)
        modeSwitch_QHBoxLayout.addWidget(self.setAuto_QRadioButton)

        self.mark_QRadioButton=QRadioButton("mark",self)
        self.radioGrp_QButtonGroup.addButton(self.mark_QRadioButton,2)
        modeSwitch_QHBoxLayout.addWidget(self.mark_QRadioButton)

        nameOrder_QHBoxLayout=QHBoxLayout(self)
        main_QVBoxLayout.addLayout(nameOrder_QHBoxLayout)

        self.name01_QComboBox=QComboBox()
        self.name01_QComboBox.addItems(["Title","NodeType","Side","Custom_0","Title_Numbers_0","Title_Hierarchys_0","NodeType_Numbers_0","NodeType_Hierarchys_0","Side_Numbers_0","Side_Hierarchys_0"])
        nameOrder_QHBoxLayout.addWidget(self.name01_QComboBox)

        self.name02_QComboBox=QComboBox()
        self.name02_QComboBox.addItems(["None","Title","NodeType","Side","Numbers_0","Hierarchys_0","Custom_0","Title_Numbers_0","Title_Hierarchys_0","NodeType_Numbers_0","NodeType_Hierarchys_0","Side_Numbers_0","Side_Hierarchys_0"])
        nameOrder_QHBoxLayout.addWidget(self.name02_QComboBox)

        self.name03_QComboBox=QComboBox()
        self.name03_QComboBox.addItems(["None","Title","NodeType","Side","Numbers_0","Hierarchys_0","Custom_0","Title_Numbers_0","Title_Hierarchys_0","NodeType_Numbers_0","NodeType_Hierarchys_0","Side_Numbers_0","Side_Hierarchys_0"])
        nameOrder_QHBoxLayout.addWidget(self.name03_QComboBox)

        self.name04_QComboBox=QComboBox()
        self.name04_QComboBox.addItems(["None","Title","NodeType","Side","Numbers_0","Hierarchys_0","Custom_0","Title_Numbers_0","Title_Hierarchys_0","NodeType_Numbers_0","NodeType_Hierarchys_0","Side_Numbers_0","Side_Hierarchys_0"])
        nameOrder_QHBoxLayout.addWidget(self.name04_QComboBox)

        self.name05_QComboBox=QComboBox()
        self.name05_QComboBox.addItems(["None","Title","NodeType","Side","Numbers_0","Hierarchys_0","Custom_0","Title_Numbers_0","Title_Hierarchys_0","NodeType_Numbers_0","NodeType_Hierarchys_0","Side_Numbers_0","Side_Hierarchys_0"])
        nameOrder_QHBoxLayout.addWidget(self.name05_QComboBox)

        customPlain_QFormLayout=QFormLayout(self)
        main_QVBoxLayout.addLayout(customPlain_QFormLayout)

        custom_QLabel=QLabel("custom:",self)
        self.custom_QLineEdit=QLineEdit(self)
        customPlain_QFormLayout.addRow(custom_QLabel,self.custom_QLineEdit)
        
        title_QLabel=QLabel("title:",self)
        self.title_QLineEdit=QLineEdit(self)
        customPlain_QFormLayout.addRow(title_QLabel,self.title_QLineEdit)

        node_QLabel=QLabel("node:",self)
        self.node_QLineEdit=QLineEdit(self)
        customPlain_QFormLayout.addRow(node_QLabel,self.node_QLineEdit)
        
        side_QLabel=QLabel("side:",self)
        self.side_QLineEdit=QLineEdit(self)
        customPlain_QFormLayout.addRow(side_QLabel,self.side_QLineEdit)

#viewWindow=AutoNodeRenameBase()
#viewWindow.show()