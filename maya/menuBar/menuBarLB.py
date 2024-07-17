# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
from ...library import xmlLB as xLB
cit.reloads([bLB,jLB,xLB])

class DataMenuParam(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super().__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._label_str=None
            self._fromFolder_str=None
            self._importFile_str=None
            self._function_str=None
            self._iconFileExt_str=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMenuParam):
                self._label_str=dataTuple[0].getLabel()
                self._fromFolder_str=dataTuple[0].getFromFolder()
                self._importFile_str=dataTuple[0].getImportFile()
                self._function_str=dataTuple[0].getFunction()
                self._iconFileExt_str=dataTuple[0].getIcon()

    #Setting Function    
    def setLabel(self,variable):
        self._label_str=variable
        return self._label_str
    def getLabel(self):
        return self._label_str
    
    def setFromFolder(self,variable):
        self._fromFolder_str=variable
        return self._fromFolder_str
    def getFromFolder(self):
        return self._fromFolder_str
    
    def setImportFile(self,variable):
        self._importFile_str=variable
        return self._importFile_str
    def getImportFile(self):
        return self._importFile_str
    
    def setFunction(self,variable):
        self._function_str=variable
        return self._function_str
    def getFunction(self):
        return self._function_str
    
    def setIcon(self,variable):
        self._iconFileExt_str=variable
        return self._iconFileExt_str
    def getIcon(self):
        return self._iconFileExt_str

    #Public Function
    def readDict(self,setting_dict=None):
        _setting_dict=setting_dict or self._setting_dict
        
        for __setting_str in self._setting_strs:
            exec('self.set'+__setting_str+'(_setting_dict.get("'+__setting_str+'"))')

    def readXML(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath
    
class DataMenuParamArray(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super().__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._menuName_str=None
            self._menuType_str=None #"single" or "multi"
            self._menu_DataMenuParams=[]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMenuParamArray):
                self._menuName_str=dataTuple[0].getName()
                self._menuType_str=dataTuple[0].getType()
                self._menu_DataMenuParams=dataTuple[0].getDataMenuParams()

    def __len__(self):
        return len(self._menu_DataMenuParams)

    def __getitem__(self,index):
        return self._menu_DataMenuParams[index]

    def __setitem__(self,index,value):
        self._menu_DataMenuParams[index]=value

    def __delitem__(self,index):
        del self._menu_DataMenuParams[index]

    def __iter__(self):
        return iter(self._menu_DataMenuParams)

    #Setting Function
    def setName(self,variable):
        self._menuName_str=variable
        return self._menuName_str
    def getName(self):
        return self._menuName_str
    
    def setType(self,variable):
        self._menuType_str=variable
        return self._menuType_str
    def getType(self):
        return self._menuType_str
    
    def setDataMenuParams(self,variable):
        self._menu_DataMenuParams=variable
        return self._menu_DataMenuParams
    def addDataMenuParams(self,variable):
        self._menu_DataMenuParams+=variable
        return self._menu_DataMenuParams
    def getDataMenuParams(self):
        return self._menu_DataMenuParams
    
    #Public Function
    def readDict(self,setting_dict=None):
        _setting_dict=setting_dict or self._setting_dict

        self.setName(_setting_dict.get("Name"))
        self.setType(_setting_dict.get("Type"))
        for DataMenuParam_dict in _setting_dict.get("DataMenuParamArray"):
            menu_DataMenuParam=DataMenuParam()
            menu_DataMenuParam.setSettingDict(DataMenuParam_dict)
            menu_DataMenuParam.readDict()
            self.addDataMenuParams([menu_DataMenuParam])
    
    def readXML(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

class DataMenu(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super().__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._menuName_str=None
            self._menu_DataMenuParamArrays=[]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataMenu):
                self._menuName_str=dataTuple[0].getName()
                self._menu_DataMenuParamArrays=dataTuple[0].getDataMenuParamArrays()

    #Setting Function
    def setName(self,variable):
        self._menuName_str=variable
        return self._menuName_str
    def getName(self):
        return self._menuName_str
    
    def setDataMenuParamArrays(self,variables):
        self._menu_DataMenuParamArrays=variables
        return self._menu_DataMenuParamArrays
    def addDataMenuParamArrays(self,variables):
        self._menu_DataMenuParamArrays+=variables
        return self._menu_DataMenuParamArrays
    def getDataMenuParamArrays(self):
        return self._menu_DataMenuParamArrays
    
    #Public Function
    def readDict(self,setting_dict=None):
        _setting_dict=setting_dict or self._setting_dict

        self.setName(_setting_dict.get("Name"))
        for DataMenuParamArray_dict in _setting_dict.get("DataMenuParamArrays"):
            menu_DataMenuParamArray=DataMenuParamArray()
            menu_DataMenuParamArray.setSettingDict(DataMenuParamArray_dict)
            menu_DataMenuParamArray.readDict()
            self.addDataMenuParamArrays([menu_DataMenuParamArray])
    
    def readXML(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

class AppMenu():
    def __init__(self):
        self._menu_DataMenu=None

    #Single Function
    def setItem_create_func(self,title,fromFolder,importFile,function,icon):
        command="import cgInTools as cit; from "+fromFolder+" import "+importFile+" as ps; cit.reloads([ps]); ps."+function
        if title == True or title == 1:
            cmds.menuItem(optionBox=title,c=command)
        else:
            cmds.menuItem(label=title,c=command,i=icon)

    #Multi Function
    def _singleItem_create_func(self,itemName_str,menu_DataMenuParams):
        cmds.menuItem(divider=True,dividerLabel=itemName_str)
        for menu_DataMenuParam in menu_DataMenuParams:
            label_str=menu_DataMenuParam.getLabel()
            from_str=menu_DataMenuParam.getFromFolder()
            import_str=menu_DataMenuParam.getImportFile()
            function_str=menu_DataMenuParam.getFunction()
            icon_str=menu_DataMenuParam.getIcon()
            self.setItem_create_func(label_str,from_str,import_str,function_str,icon_str)

    def _multiItem_create_func(self,itemName_str,menu_DataMenuParams):
        cmds.menuItem(subMenu=True,to=True,label=itemName_str)
        for menu_DataMenuParam in menu_DataMenuParams:
            label_str=menu_DataMenuParam.getLabel()
            from_str=menu_DataMenuParam.getFromFolder()
            import_str=menu_DataMenuParam.getImportFile()
            function_str=menu_DataMenuParam.getFunction()
            icon_str=menu_DataMenuParam.getIcon()
            self.setItem_create_func(label_str,from_str,import_str,function_str,icon_str)
        cmds.setParent("..",menu=True)

    def _settingsMenu_create_func(self,menuName_str,menu_DataMenuParamArrays):
        cmds.menu(l=menuName_str,p="MayaWindow",to=True)
        for menu_DataMenuParamArray in menu_DataMenuParamArrays:
            if menu_DataMenuParamArray.getType() == "single":
                self._singleItem_create_func(menu_DataMenuParamArray.getName(),menu_DataMenuParamArray.getDataMenuParams())
            elif menu_DataMenuParamArray.getType() == "multi":
                self._multiItem_create_func(menu_DataMenuParamArray.getName(),menu_DataMenuParamArray.getDataMenuParams())
            else:
                pass
    
    #Setting Function
    def setDataMenu(self,variable):
        self._menu_DataMenu=variable
        return self._menu_DataMenu
    def getDataMenu(self):
        return self._menu_DataMenu
        
    #Public Function
    def create(self):
        menuName_str=self._menu_DataMenu.getName()
        menu_DataMenuParamArrays=self._menu_DataMenu.getDataMenuParamArrays()
        self._settingsMenu_create_func(menuName_str,menu_DataMenuParamArrays)

class SelfMenu(bLB.SelfOrigin):
    def __init__(self,selfObject=None):
        super().__init__(selfObject)
        if selfObject is None:
            self._menu_DataMenu=None
        elif isinstance(selfObject,SelfMenu):
            self._menu_DataMenu=selfObject.getDataMenu()

    #Setting Function
    def setDataMenu(self,variable):
        self._menu_DataMenu=variable
        return self._menu_DataMenu
    def getDataMenu(self):
        return self._menu_DataMenu
    
    #Public Function
    def create(self,dataMenu=None):
        _menu_DataMenu=dataMenu or self._menu_DataMenu

        menu_AppMenu=AppMenu()
        menu_AppMenu.setDataMenu(_menu_DataMenu)
        menu_AppMenu.create()

    def updata(self,dataMenu=None):
        pass
