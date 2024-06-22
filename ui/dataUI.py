# -*- coding: iso-8859-15 -*-
try:
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
except ImportError:
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *

class DataTableWidget(QTableWidgetItem):
    def __init__(self,*args,**kwargs):
        super(DataTableWidget,self).__init__(*args,**kwargs)
        