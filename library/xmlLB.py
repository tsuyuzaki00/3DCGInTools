# -*- coding: iso-8859-15 -*-
import xml.etree.ElementTree as ET 

import cgInTools as cit
from . import pathLB as pLB
cit.reloads([pLB])

class AppXml(object):
    def __init__(self):
        self._path_DataPath=None
        self._xml_ElementTree=None

    #Setting Function
    def setDataPath(self,variable):
        self._path_DataPath=variable
        return self._path_DataPath
    def getDataPath(self):
        return self._path_DataPath
    
    def setElementTree(self,variable):
        self._xml_ElementTree=variable
        return self._xml_ElementTree
    def getElementTree(self):
        return self._xml_ElementTree

    #Public Function
    def read(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        path_AppPath=pLB.AppPath()
        absolute_path=path_AppPath.queryAbsolutePath(_path_DataPath)
        xml_ElementTree=ET.parse(absolute_path)
        return xml_ElementTree
    
    def write(self,dataPath=None,xmlElementTree=None):
        _path_DataPath=dataPath or self._path_DataPath
        _xmlElementTree=xmlElementTree or self._xml_ElementTree

        path_AppPath=pLB.AppPath()
        absolute_path=path_AppPath.queryAbsolutePath(_path_DataPath)
        _xmlElementTree.write(absolute_path)

    def check(self,dataPath=None):
        _path_DataPath=dataPath or self._path_DataPath

        path_AppPath=pLB.AppPath()
        path_AppPath.setDataPath(_path_DataPath)
        absolutePath_bool=path_AppPath.checkAbsolutePath()
        return absolutePath_bool
