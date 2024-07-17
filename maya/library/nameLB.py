# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import functionLB as fLB
from . import openMayaLB as oLB
cit.reloads([bLB,fLB,oLB])

RULES_DICT=fLB.readJson(cit.maya_dir,"library","nameLB")

class DataNodoName(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super().__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._titleName_str=None
            self._tagTypeName_str=None
            self._sideName_str=None
            self._numberName_ints=[0]
            self._hierarchyName_strs=["A"]
            self._customName_strs=[]
            self._orderName_strs=["Title","TagType","Numbers_0"]
            #["Title","TagType","Side","Numbers_0","Hierarchys_1","Customs_10","Title_Numbers_0","Title_Hierarchys_2","Side_Numbers_0","Side_Hierarchys_2"]
            self._increaseName_str=None
            #None,"Numbers_0","Hierarchys_10"
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataNodoName):
                self._titleName_str=dataTuple[0].getTitle()
                self._tagTypeName_str=dataTuple[0].getTagType()
                self._sideName_str=dataTuple[0].getSide()
                self._numberName_ints=dataTuple[0].getNumbers()
                self._hierarchyName_strs=dataTuple[0].getHierarchys()
                self._customName_strs=dataTuple[0].getCustoms()
                self._orderName_strs=dataTuple[0].getOrders()
                self._increaseName_str=dataTuple[0].getIncrease()

    #Setting Function
    def setTitle(self,variable):
        self._titleName_str=variable
        return self._titleName_str
    def getTitle(self):
        return self._titleName_str
    
    def setTagType(self,variable):
        self._tagTypeName_str=variable
        return self._tagTypeName_str
    def getTagType(self):
        return self._tagTypeName_str
    
    def setSide(self,variable):
        self._sideName_str=variable
        return self._sideName_str
    def getSide(self):
        return self._sideName_str
    
    def setNumbers(self,variables):
        self._numberName_ints=variables
        return self._numberName_ints
    def addNumbers(self,variables):
        self._numberName_ints+=variables
        return self._numberName_ints
    def getNumbers(self):
        return self._numberName_ints
    
    def setHierarchys(self,variables):
        self._hierarchyName_strs=variables
        return self._hierarchyName_strs
    def addHierarchys(self,variables):
        self._hierarchyName_strs+=variables
        return self._hierarchyName_strs
    def getHierarchys(self):
        return self._hierarchyName_strs
    
    def setCustoms(self,variables):
        self._customName_strs=variables
        return self._customName_strs
    def addCustoms(self,variables):
        self._customName_strs+=variables
        return self._customName_strs
    def getCustoms(self):
        return self._customName_strs
    
    def setOrders(self,variables):
        self._orderName_strs=variables
        return self._orderName_strs
    def addOrders(self,variables):
        self._orderName_strs+=variables
        return self._orderName_strs
    def getOrders(self):
        return self._orderName_strs

    def setIncrease(self,variable):
        self._increaseName_str=variable
        return self._increaseName_str
    def getIncrease(self):
        return self._increaseName_str

    #Public Function
    def readDict(self, setting_dict=None):
        _setting_dict=setting_dict or self._setting_dict

        for __setting_str in self._setting_strs:
            exec('self.set'+__setting_str+'(_setting_dict.get("'+__setting_str+'"))')
    
    def readXML(self, dataPath=None):
        _origin_DataPath=dataPath or self._origin_DataPath

class AppNodeName(oLB.AppOpenMayaBase):
    def __init__(self):
        super().__init__()
        self._name_DataNodoName=None
        self._node_DataNode=None
        self._nodeNameRule_dict=RULES_DICT["nodeName_dict"]

    #Single Function
    @staticmethod
    def orderNames_create_str(name_DataNodoName):
        order_strs=name_DataNodoName.getOrders()
        partsName_strs=[]
        for order_str in order_strs:
            if order_str is None:
                continue
            orderSplit_strs=order_str.split("_")
            if len(orderSplit_strs) is 1:
                partsName_value=eval('name_DataNodoName.get'+orderSplit_strs[0]+'()')
            elif len(orderSplit_strs) is 2:
                partsName_value=eval('name_DataNodoName.get'+orderSplit_strs[0]+'()['+orderSplit_strs[-1]+']')
            elif len(orderSplit_strs) is 3:
                partsName_value=eval('name_DataNodoName.get'+orderSplit_strs[0]+'()')
                sequence_value=eval('name_DataNodoName.get'+orderSplit_strs[1]+'()['+orderSplit_strs[-1]+']')
                if partsName_value is None:
                    partsName_value=sequence_value
                else:
                    partsName_value=partsName_value+str(sequence_value)
            partsName_strs.append(partsName_value)
        cleanName_strs=[str(partsName_str) for partsName_str in partsName_strs if partsName_str is not None]
        name_str="_".join(cleanName_strs)
        return name_str
    
    @staticmethod
    def nextAlphabet_edit_str(alphabet_str):
        if alphabet_str == "Z":
            return "A"
        elif alphabet_str == "z":
            return "a"
        else:
            return chr(ord(alphabet_str)+1)
    
    @staticmethod
    def smashNumber_edit_str(name_str):
        while name_str[-1].isdigit():
            name_str=name_str[:-1]
            if name_str == "":
                return None
        return name_str
    
    @staticmethod
    def smashAlphabet_edit_str(name_str):
        while name_str[-1].isupper():
            name_str=name_str[:-1]
            if name_str == "":
                return None
        return name_str

    #Multi Function
    def _sameName_check_str(self,name_str):
        while cmds.objExists(name_str):
            next_DataNodoName=self.nextIncrease()
            if next_DataNodoName is None:
                break
            else:
                name_str=self.orderNames_create_str(next_DataNodoName)
        return name_str

    #Inheritance Function
    def _sideName_query_str(self,nodeName_str,dist=1):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MFnTransform=om2.MFnTransform(node_MDagPath)
        node_MVector=node_MFnTransform.translation(om2.MSpace.kWorld)
        if node_MVector.x > dist and node_MVector.x > dist:
            return "L"
        elif node_MVector.x < -dist and node_MVector.x < -dist:
            return "R"
        else:
            return "C"

    def _tagType_query_str(self,nodeName_str):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        if node_MFnDependencyNode.typeName == "transform":
            try:
                node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
                shape_MDagPath=node_MDagPath.extendToShape()
                shape_MFnDagNode=om2.MFnDagNode(shape_MDagPath)
                tagType_str=shape_MFnDagNode.typeName
            except RuntimeError:
                return "none"
        else:
            tagType_str=node_MFnDependencyNode.typeName
        return tagType_str
        
    def _nodeRename_edit_str(self,nodeName_str,rename_str):
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        node_MFnDependencyNode.setName(rename_str)
        return node_MFnDependencyNode.name()

    #Setting Function
    def setDataNodoName(self,variable):
        self._name_DataNodoName=variable
        return self._name_DataNodoName
    def getDataNodoName(self):
        return self._name_DataNodoName

    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setNodeNameRule(self,variable):
        self._nodeNameRule_dict=variable
        return self._nodeNameRule_dict
    def getNodeNameRule(self):
        return self._nodeNameRule_dict
    
    #Public Function
    def create(self,dataName=None):
        _name_DataNodoName=dataName or self._name_DataNodoName

        name_str=self.orderNames_create_str(_name_DataNodoName)
        checkName_str=self._sameName_check_str(name_str)
        return checkName_str
    
    def nextIncrease(self,dataName=None):
        _name_DataNodoName=dataName or self._name_DataNodoName

        if _name_DataNodoName.getIncrease() is None:
            _name_DataNodoName.addOrders(["Numbers_0"])
            return _name_DataNodoName
        increase_strs=_name_DataNodoName.getIncrease().split("_")
        if "Numbers" in increase_strs:
            number_ints=_name_DataNodoName.getNumbers()
            number_int=number_ints[int(increase_strs[-1])]
            number_ints[int(increase_strs[-1])]=number_int+1
            _name_DataNodoName.setNumbers(number_ints)
            return _name_DataNodoName
        elif "Hierarchys" in increase_strs:
            increase_strs=_name_DataNodoName.getIncrease().split("_")
            hierarchy_strs=_name_DataNodoName.getHierarchys()
            hierarchy_str=hierarchy_strs[int(increase_strs[-1])]
            hierarchy_strs[int(increase_strs[-1])]=self.nextAlphabet_edit_str(hierarchy_str)
            _name_DataNodoName.setHierarchys(hierarchy_strs)
            return _name_DataNodoName
        else:
            _name_DataNodoName.addOrders(["Numbers_0"])
            return _name_DataNodoName
        
    def rename(self,dataName=None,dataNode=None):
        _name_DataNodoName=dataName or self._name_DataNodoName
        _node_DataNode=dataNode or self._node_DataNode

        name_str=self.orderNames_create_str(_name_DataNodoName)
        checkName_str=self._sameName_check_str(name_str)
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),checkName_str)
        return rename_str

    def editRename(self,dataName=None,dataNode=None):
        _name_DataNodoName=dataName or self._name_DataNodoName
        _node_DataNode=dataNode or self._node_DataNode

        if _name_DataNodoName.getTitle() is None:
            nameSplits=_node_DataNode.getName().split("_")
            smashNumber_str=self.smashNumber_edit_str(nameSplits[0])
            smashAlphabet_str=self.smashAlphabet_edit_str(smashNumber_str)
            _name_DataNodoName.setTitle(smashAlphabet_str)

        if _name_DataNodoName.getTagType() is None:
            tagType_str=self._tagType_query_str(_node_DataNode.getName())
            typeName_str=self._nodeNameRule_dict.get(tagType_str)
            _name_DataNodoName.setTagType(typeName_str)

        if _name_DataNodoName.getSide() is None:
            side_str=self._sideName_query_str(_node_DataNode.getName())
            _name_DataNodoName.setSide(side_str)

        name_str=self.orderNames_create_str(_name_DataNodoName)
        checkName_str=self._sameName_check_str(name_str)
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),checkName_str)
        return rename_str

    def autoRename(self,dataNode=None,order_strs=["Title","TagType"]):
        _node_DataNode=dataNode or self._node_DataNode

        _name_DataNodoName=DataNodoName()
        _name_DataNodoName.setOrders(order_strs)

        nameSplits=_node_DataNode.getName().split("_")
        smashNumber_str=self.smashNumber_edit_str(nameSplits[0])
        smashAlphabet_str=self.smashAlphabet_edit_str(smashNumber_str)
        _name_DataNodoName.setTitle(smashAlphabet_str)
        
        tagType_str=self._tagType_query_str(_node_DataNode.getName())
        typeName_str=self._nodeNameRule_dict.get(tagType_str)
        _name_DataNodoName.setTagType(typeName_str)
        
        side_str=self._sideName_query_str(_node_DataNode.getName())
        _name_DataNodoName.setSide(side_str)

        name_str=self.orderNames_create_str(_name_DataNodoName)
        checkName_str=self._sameName_check_str(name_str)
        rename_str=self._nodeRename_edit_str(_node_DataNode.getName(),checkName_str)
        return rename_str
    