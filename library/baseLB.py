# -*- coding: iso-8859-15 -*-
from abc import ABC,abstractmethod
import inspect

import cgInTools as cit
from . import serializeLB as sLB
from . import jsonLB as jLB
from . import xmlLB as xLB
cit.reloads([sLB,jLB,xLB])

class DataOrigin(ABC):
    def __init__(self,*dataTuple):
        self._setting_strs=self.__isSetGetFunction_query_strs()
        self._setting_dict=None
        from . import dataLB as dLB
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._origin_DataPath=None
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],dLB.DataPath):
                self._origin_DataPath=dataTuple[0]
            elif isinstance(dataTuple[0],DataOrigin):
                self._origin_DataPath=dataTuple[0].getOriginDataPath()
    
    #Private Function
    def __isSetGetFunction_query_strs(self):
        setting_strs=[
            m[0].replace("get","")
            for m in inspect.getmembers(self,predicate=inspect.ismethod)
            if m[0].startswith("get") and m[0] is not "getSettingDict" and m[0] is not "getOriginDataPath"
        ]
        return setting_strs

    #Setting Function
    def setOriginDataPath(self,variable):
        self._origin_DataPath=variable
        return self._origin_DataPath
    def getOriginDataPath(self):
        return self._origin_DataPath

    def setSettingDict(self,variable):
        self._setting_dict=variable
        return self._setting_dict
    def getSettingDict(self):
        return self._setting_dict

    #Public Function
    @abstractmethod
    def readDict(self,setting_dict=None):
        pass
    
    def writeDict(self):
        write_dict={}
        for __setting_str in self._setting_strs:
            setting_str=__setting_str[0].upper()+__setting_str[1:]
            variable=eval('self.get'+setting_str+'()')
            if type(variable) in (bool,int,float,str) or variable is None:
                write_dict[setting_str]=variable
            elif type(variable) in (list,tuple):
                variables=[]
                for v in variable:
                    if type(v) in (bool,int,float,str) or v is None:
                        variables.append(v)
                    else:
                        variables.append(v.writeDict())
                write_dict[setting_str]=variables
            else:
                write_dict[setting_str]=variable.writeDict()
        return write_dict

    @abstractmethod
    def readXML(self,dataPath=None):
        pass

    def writeXML(self,dataPath=None):
        pass

    def readJson(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        read_AppJson=jLB.AppJson()
        read_AppJson.setDataPath(_origin_DataPath)
        read_dict=read_AppJson.read()
        self.readDict(read_dict)

    def writeJson(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath
        
        write_AppJson=jLB.AppJson()
        write_AppJson.setDataPath(_origin_DataPath)
        write_AppJson.setJsonDict(self.writeDict())
        write_AppJson.write()

    def readData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        selfpy_SelfSerialize=sLB.AppSerialize()
        selfpy_SelfSerialize.setDataPath(_origin_DataPath)
        selfpy_SelfObject=selfpy_SelfSerialize.read()
        self.__init__(selfpy_SelfObject)

    def writeData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        selfpy_SelfSerialize=sLB.AppSerialize()
        selfpy_SelfSerialize.setDataPath(_origin_DataPath)
        selfpy_SelfSerialize.setWriteSelfObject(self)
        selfpy_SelfSerialize.write()

class SelfOrigin(ABC):
    def __init__(self,selfObject=None):
        if selfObject is None:
            self._origin_DataPath=None
            self._doIt_strs=[]
        elif isinstance(selfObject,SelfOrigin):
            self._origin_DataPath=selfObject.getOriginDataPath()
            self._doIt_strs=selfObject.getDoItStrs()
    
    #Setting Function
    def setOriginDataPath(self,variable):
        self._origin_DataPath=variable
        return self._origin_DataPath
    def getOriginDataPath(self):
        return self._origin_DataPath

    def setDoItStrs(self,variables):
        self._doIt_strs=variables
        return self._doIt_strs
    def addDoItStrs(self,variables):
        self._doIt_strs+=variables
        return self._doIt_strs
    def getDoItStrs(self):
        return self._doIt_strs
    
    #Public Function
    def readData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        selfpy_SelfSerialize=sLB.AppSerialize()
        selfpy_SelfSerialize.setDataPath(_origin_DataPath)
        selfpy_SelfObject=selfpy_SelfSerialize.read()
        self.__init__(selfpy_SelfObject)

    def writeData(self,dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

        selfpy_SelfSerialize=sLB.AppSerialize()
        selfpy_SelfSerialize.setDataPath(_origin_DataPath)
        selfpy_SelfSerialize.setWriteSelfObject(self)
        selfpy_SelfSerialize.write()

    def doIt(self,doIts=None):
        _doIt_strs=doIts or self._doIt_strs

        if _doIt_strs is None or _doIt_strs == []:
            return
        else:
            for _doIt_str in _doIt_strs:
                exec('self.'+_doIt_str+'()')