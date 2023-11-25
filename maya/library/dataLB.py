# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2

import cgInTools as cit
from ...library import baseLB as bLB
cit.reloads([bLB])

#Definition Data
class DataMenuParam(bLB.SelfOrigin):
    def __init__(self):
        super(DataMenuParam,self).__init__()
        self._label_str=None
        self._fromFolder_str=None
        self._importFile_str=None
        self._function_str=None
        self._iconFileExt_str=None

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

class DataAttribute(bLB.SelfOrigin):
    def __init__(self,dataAttribute=None):
        super(DataAttribute,self).__init__()
        if dataAttribute is None:
            self._longName_str=None
            self._shortName_str=None
        elif type(dataAttribute) is DataAttribute:
            self._longName_str=dataAttribute.getName()
            self._shortName_str=dataAttribute.getShortName()
        elif type(dataAttribute) is om2.MObject:
            attr_MFnAttribute=om2.MFnAttribute(dataAttribute)

            self._longName_str=attr_MFnAttribute.name
            self._shortName_str=attr_MFnAttribute.shortName
            
    #Setting Function
    def setName(self,variable):
        self._longName_str=variable
        return self._longName_str
    def getName(self):
        return self._longName_str
    
    def setShortName(self,variable):
        self._shortName_str=variable
        return self._shortName_str
    def getShortName(self):
        return self._shortName_str

class DataAttributeBoolean(DataAttribute):
    def __init__(self,dataAttributeBoolean=None):
        super(DataAttributeBoolean,self).__init__(dataAttributeBoolean)
        self.__valueType_int=om2.MFnNumericData().kBoolean #1
        if dataAttributeBoolean is None:
            self._valueBoolean_bool=None
        elif type(dataAttributeBoolean) is DataAttributeBoolean:
            self._valueBoolean_bool=dataAttributeBoolean.getValue()

    def setValue(self,variable):
        self._valueBoolean_bool=variable
        return self._valueBoolean_bool
    def getValue(self):
        return self._valueBoolean_bool

    def getValueType(self):
        return self.__valueType_int

class DataAttributeInt(DataAttribute):
    def __init__(self,dataAttributeInt=None):
        super(DataAttributeInt,self).__init__(dataAttributeInt)
        self.__valueType_int=om2.MFnNumericData().kInt #7
        if dataAttributeInt is None:
            self._valueInt_int=None
            self._limitMax_int=None
            self._limitMin_int=None
        elif type(dataAttributeInt) is DataAttributeInt:
            self._valueInt_int=dataAttributeInt.getValue()
            self._limitMax_int=dataAttributeInt.getMax()
            self._limitMin_int=dataAttributeInt.getMin()

    def setValue(self,variable):
        self._valueInt_int=variable
        return self._valueInt_int
    def getValue(self):
        return self._valueInt_int
    
    def setMax(self,variable):
        self._limitMax_int=variable
        return self._limitMax_int
    def getMax(self):
        return self._limitMax_int
    
    def setMin(self,variable):
        self._limitMin_int=variable
        return self._limitMin_int
    def getMin(self):
        return self._limitMin_int
    

    def getValueType(self):
        return self.__valueType_int

class DataAttributeFloat(DataAttribute):
    def __init__(self,dataAttributeFloat=None):
        super(DataAttributeFloat,self).__init__(dataAttributeFloat)
        self.__valueType_int=om2.MFnNumericData().kFloat #11
        if dataAttributeFloat is None:
            self._valueFloat_float=None
            self._limitMax_float=None
            self._limitMin_float=None
        elif type(dataAttributeFloat) is DataAttributeFloat:
            self._valueFloat_float=dataAttributeFloat.getValue()
            self._limitMax_float=dataAttributeFloat.getMax()
            self._limitMin_float=dataAttributeFloat.getMin()

    def setValue(self,variable):
        self._valueFloat_float=variable
        return self._valueFloat_float
    def getValue(self):
        return self._valueFloat_float

    def setMax(self,variable):
        self._limitMax_float=variable
        return self._limitMax_float
    def getMax(self):
        return self._limitMax_float
    
    def setMin(self,variable):
        self._limitMin_float=variable
        return self._limitMin_float
    def getMin(self):
        return self._limitMin_float
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeVector(DataAttribute):
    def __init__(self,dataAttributeVector=None):
        super(DataAttributeVector,self).__init__()
        self.__valueType_int=om2.MFnNumericData().k3Float  #13
        if dataAttributeVector is None:
            self._valueVector_tuple3=[0.0,0.0,0.0]
            self._limitMax_floats=[]
            self._limitMin_floats=[]
        elif type(dataAttributeVector) is DataAttributeVector:
            self._valueVector_tuple3=dataAttributeVector.getValue()
            self._limitMax_float=dataAttributeVector.getMax()
            self._limitMin_float=dataAttributeVector.getMin()

    #Setting Function
    def setValue(self,variables):
        self._valueVector_tuple3=variables
        return self._valueVector_tuple3
    def getValue(self):
        return self._valueVector_tuple3
    
    def setMax(self,variables):
        self._limitMax_floats=variables
        return self._limitMax_floats
    def getMax(self):
        return self._limitMax_floats
    
    def setMin(self,variables):
        self._limitMin_floats=variables
        return self._limitMin_floats
    def getMin(self):
        return self._limitMin_floats
    

    def setVectorX(self,variable):
        self._valueVector_tuple3[0]=variable
        return self._valueVector_tuple3[0]
    def getVectorX(self):
        return self._valueVector_tuple3[0]
    
    def setVectorY(self,variable):
        self._valueVector_tuple3[1]=variable
        return self._valueVector_tuple3[1]
    def getVectorY(self):
        return self._valueVector_tuple3[1]
    
    def setVectorZ(self,variable):
        self._valueVector_tuple3[2]=variable
        return self._valueVector_tuple3[2]
    def getVectorZ(self):
        return self._valueVector_tuple3[2]
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeString(DataAttribute):
    def __init__(self,dataAttributeString=None):
        super(DataAttributeString,self).__init__(dataAttributeString)
        self.__valueType_int=om2.MFnData().kString #4
        if dataAttributeString is None:
            self._valueString_str=None
        elif type(dataAttributeString) is DataAttributeString:
            self._valueString_str=dataAttributeString.getValue()
    
    def setValue(self,variable):
        self._valueString_str=variable
        return self._valueString_str
    def getValue(self):
        return self._valueString_str
    
    def getValueType(self):
        return self.__valueType_int

class DataAttributeEnum(DataAttribute):
    def __init__(self,dataAttributeEnum=None):
        super(DataAttributeEnum,self).__init__()
        if dataAttributeEnum is None:
            self._fieldEnum_strs=[]
            self._valueEnum_str=None
        elif type(dataAttributeEnum) is DataAttributeEnum:
            self._fieldEnum_strs=dataAttributeEnum.getField()
            self._valueEnum_str=dataAttributeEnum.getEnum()

    #Setting Function
    def setField(self,variables):
        self._fieldEnum_strs=variables
        return self._fieldEnum_strs
    def addField(self,variables):
        self._fieldEnum_strs+=variables
        return self._fieldEnum_strs
    def getField(self):
        return self._fieldEnum_strs

    def setEnum(self,variable):
        self._valueEnum_str=variable
        return self._valueEnum_str
    def getEnum(self):
        return self._valueEnum_str

class DataAttributeWeight(DataAttribute):
    def __init__(self):
        super(DataAttributeWeight,self).__init__()
        self._valueWeight_float=None
        self._indexWeight_int=None

    #Setting Function
    def setValueWeight(self,variable):
        self._valueWeight_float=variable
        return self._valueWeight_float
    def getValueWeight(self):
        return self._valueWeight_float
    
    def setIndexWeight(self,variable):
        self._indexWeight_int=variable
        return self._indexWeight_int
    def getIndexWeight(self):
        return self._indexWeight_int

class DataName(bLB.SelfOrigin):
    def __init__(self):
        self._titleName_str=None
        self._nodeTypeName_str=None
        self._sideName_str=None
        self._numberName_ints=[0]
        self._hierarchyName_strs=["A"]
        self._customName_strs=[]
        #["Title","NodeType","Side","Number_0","Hierarchy_1","Custom_10","Title_Number_0","Title_Hierarchy_2","Side_Number_0","Side_Hierarchy_2"]
        self._orderName_enums=["Title","NodeType"]
        #"Number_0","Hierarchy_10"
        self._increaseName_enum="Number_0"

    #Setting Function
    def setTitle(self,variable):
        self._titleName_str=variable
        return self._titleName_str
    def getTitle(self):
        return self._titleName_str
    
    def setNodeType(self,variable):
        self._nodeTypeName_str=variable
        return self._nodeTypeName_str
    def getNodeType(self):
        return self._nodeTypeName_str
    
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
        self._orderName_enums=variables
        return self._orderName_enums
    def addOrders(self,variables):
        self._orderName_enums+=variables
        return self._orderName_enums
    def getOrders(self):
        return self._orderName_enums

    def setIncrease(self,variable):
        self._increaseName_enum=variable
        return self._increaseName_enum
    def getIncrease(self):
        return self._increaseName_enum

class DataMatrix(om2.MMatrix):
    def __init__(self,*args):
        super(DataMatrix,self).__init__(*args)
        #self.kIdentity=om2.MMatrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self._MSpace=om2.MSpace.kTransform #1
        self._rotateOrder=om2.MEulerRotation.kXYZ #0

    def setMatrix(self,variable):
        self.kIdentity=om2.MMatrix(variable)
        return self.kIdentity
    def getMatrix(self):
        matrix=list(self.kIdentity)
        return matrix
    def getMMatrix(self):
        return self.self.kIdentity
    
    def setMSpace(self,variable):
        self._MSpace=variable
    def getMSpace(self):
        return self._MSpace

    def setRotateOrder(self,variable):
        self._rotateOrder=variable
    def getRotateOrder(self):
        return self._rotateOrder

class DataMatrixMix(bLB.SelfOrigin):
    def __init__(self):
        super(DataMatrixMix,self).__init__()
        self._world_DataMatrix=None
        self._local_DataMatrix=None
        self._parent_DataMatrix=None

    #Setting Function
    def setWorldDataMatrix(self,variable):
        self._world_DataMatrix=variable
        return self._world_DataMatrix
    def getWorldDataMatrix(self):
        return self._world_DataMatrix
    
    def setLocalDataMatrix(self,variable):
        self._local_DataMatrix=variable
        return self._local_DataMatrix
    def getLocalDataMatrix(self):
        return self._local_DataMatrix
    
    def setParentDataMatrix(self,variable):
        self._parent_DataMatrix=variable
        return self._parent_DataMatrix
    def getParentDataMatrix(self):
        return self._parent_DataMatrix

class DataTime(om2.MTime):
    def __init__(self,*args):
        super(DataTime,self).__init__(*args)
        # self.unit=int(Unit Type constant)
        # self.value=float
        
    def setUnitType(self,variable):
        self.unit=variable
        return self.unit
    def currentUnitType(self):
        self.unit=self.uiUnit
        return self.unit
    def getUnitType(self):
        return self.unit
    
    def setTime(self,variable):
        self.value=variable
        return self.value
    def currentTime(self):
        current_MTime=oma2.MAnimControl.currentTime()
        self.value=current_MTime.value
        return self.value
    def getTime(self):
        return self.value

class DataVector(om2.MVector):
    def __init__(self,*args):
        super(DataVector,self).__init__(*args)
        #self.kOneVector=(1,1,1)
        #self.x=None
        #self.y=None
        #self.z=None

    def setVector(self,variables):
        self.kOneVector=om2.MVector(variables)
        return self.kOneVector
    def getVector(self):
        return self.kOneVector
    
    def setVectorX(self,variable):
        self.x=variable
        return self.x
    def getVectorX(self):
        return self.x
    
    def setVectorY(self,variable):
        self.y=variable
        return self.y
    def getVectorY(self):
        return self.y
    
    def setVectorZ(self,variable):
        self.z=variable
        return self.z
    def getVectorZ(self):
        return self.z

class DataTranslate(om2.MVector):
    def __init__(self,*args):
        super(DataTranslate,self).__init__(*args)
        #self.kOneVector=(1,1,1)
        #self.x=None
        #self.y=None
        #self.z=None

    def setTranslate(self,variables):
        self.kOneVector=om2.MVector(variables)
        return self.kOneVector
    def getTranslate(self):
        return self.kOneVector
    
    def setTranslateX(self,variable):
        self.x=variable
        return self.x
    def getTranslateX(self):
        return self.x
    
    def setTranslateY(self,variable):
        self.y=variable
        return self.y
    def getTranslateY(self):
        return self.y
    
    def setTranslateZ(self,variable):
        self.z=variable
        return self.z
    def getTranslateZ(self):
        return self.z

class DataRotation(om2.MEulerRotation):
    def __init__(self,*args):
        super(DataRotation,self).__init__(*args)

class DataQuaternion(om2.MQuaternion):
    def __init__(self,*args):
        super(DataQuaternion,self).__init__(*args)

class DataScale(object):
    def __init__(self):
        super(DataScale,self).__init__()

class DataKey(bLB.SelfOrigin):
    def __init__(self):
        super(DataKey,self).__init__()
        self._inputValue_value=None
        self._outputValue_value=None
        self._inTanType_str=None
        self._outTanType_str=None

    #Setting Function
    def setInputValue(self,variable):
        self._inputValue_value=variable
        return self._inputValue_value
    def getInputValue(self):
        return self._inputValue_value
    
    def setOutputValue(self,variable):
        self._outputValue_value=variable
        return self._outputValue_value
    def getOutputValue(self):
        return self._outputValue_value
    
    def setInputTanType(self,variable):
        self._inputTanType_str=variable
        return self._inputTanType_str
    def getInputTanType(self):
        return self._inputTanType_str
    
    def setOutputTanType(self,variable):
        self._outputTanType_str=variable
        return self._outputTanType_str
    def getOutputTanType(self):
        return self._outputTanType_str

class DataPoint(om2.MPoint):
    def __init__(self,*args):
        super(DataPoint,self).__init__(*args)
        #self.kOrigin=maya.api.OpenMaya.MPoint(0, 0, 0, 1)
        #self.kTolerance=1
        #self.w=None
        #self.x=None
        #self.y=None
        #self.z=None
        self._index_int=None

    def setPoint(self,variables):
        self.kOrigin=om2.MPoint(variables)
        return self.kOrigin
    def getPoint(self):
        return self.kOrigin
    
    def setPointX(self,variable):
        self.x=variable
        return self.x
    def getPointX(self):
        return self.x
    
    def setPointY(self,variable):
        self.y=variable
        return self.y
    def getPointY(self):
        return self.y
    
    def setPointZ(self,variable):
        self.z=variable
        return self.z
    def getPointZ(self):
        return self.z
    
    def setPointW(self,variable):
        self.w=variable
        return self.w
    def getPointW(self):
        return self.w

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

class DataVertex(bLB.SelfOrigin):
    def __init__(self):
        super(DataVertex,self).__init__()
        self._vertex_DataPoint=None
        self._vector_DataVector=None
        self._index_int=None

    def setDataPoint(self,variable):
        self._vertex_DataPoint=variable
        return self._vertex_DataPoint
    def getDataPoint(self):
        return self._vertex_DataPoint

    def setDataVector(self,variable):
        self._vector_DataVector=variable
        return self._vector_DataVector
    def getDataVector(self):
        return self._vector_DataVector

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

class DataEdge(bLB.SelfOrigin):
    def __init__(self):
        super(DataEdge,self).__init__()
        self._edge_DataVertex2=[]
        self._index_int=None

    def setDataVertex2(self,variable2):
        self._edge_DataVertex2=variable2
        return self._edge_DataVertex2
    def getDataVertex2(self):
        return self._edge_DataVertex2

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

class DataFace(bLB.SelfOrigin):
    def __init__(self):
        super(DataFace,self).__init__()
        self._vertexFace_DataVertexs=[]
        self._edgeFace_DataEdges=[]
        self._index_int=None

    def setDataVertexs(self,variables):
        self._vertexFace_DataVertexs=variables
        return self._vertexFace_DataVertexs
    def getDataVertexs(self):
        return self._vertexFace_DataVertexs
    
    def setDataEdges(self,variables):
        self._edgeFace_DataEdges=variables
        return self._edgeFace_DataEdges
    def getDataEdges(self):
        return self._edgeFace_DataEdges

    def setID(self,variable):
        self._index_int=variable
        return self._index_int
    def getID(self):
        return self._index_int

#DefinitionArray Data
class DataMenuParamArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataMenuParamArray,self).__init__()
        self._menuName_str=None
        self._menuType_str=None #"single" or "multi"
        self._menu_DataMenuParams=[]

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
    
class DataAttributeWeightArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataAttributeWeightArray,self).__init__()
        self._indexWeightArray_int=None
        self._attrWeight_DataAttributeWeights=[]

    def __len__(self):
        return len(self._attrWeight_DataAttributeWeights)

    def __getitem__(self,index):
        return self._attrWeight_DataAttributeWeights[index]

    def __setitem__(self,index,value):
        self._attrWeight_DataAttributeWeights[index]=value

    def __delitem__(self,index):
        del self._attrWeight_DataAttributeWeights[index]

    def __iter__(self):
        return iter(self._attrWeight_DataAttributeWeights)

    #Setting Function
    def setIndexWeightArray(self,variable):
        self._indexWeightArray_int=variable
        return self._indexWeightArray_int
    def getIndexWeightArray(self):
        return self._indexWeightArray_int

    def setDataAttributeWeights(self,variables):
        self._attrWeight_DataAttributeWeights=variables
        return self._attrWeight_DataAttributeWeights
    def addDataAttributeWeights(self,variables):
        self._attrWeight_DataAttributeWeights+=variables
        return self._attrWeight_DataAttributeWeights
    def getDataAttributeWeights(self):
        return self._attrWeight_DataAttributeWeights

class DataKeyArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataKeyArray,self).__init__()
        self._key_DataKeys=[]
    
    def __len__(self):
        return len(self._key_DataKeys)

    def __getitem__(self,index):
        return self._key_DataKeys[index]

    def __setitem__(self,index,value):
        self._key_DataKeys[index]=value

    def __delitem__(self,index):
        del self._key_DataKeys[index]

    def __iter__(self):
        return iter(self._key_DataKeys)

    def setDataKeys(self,variables):
        self._key_DataKeys=variables
        return self._key_DataKeys
    def addDataKeys(self,variables):
        self._key_DataKeys+=variables
        return self._key_DataKeys
    def getDataKeys(self):
        return self._key_DataKeys

class DataPointArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataPointArray,self).__init__()
        self._point_DataPoints=[]
    
    def __len__(self):
        return len(self._point_DataPoints)

    def __getitem__(self,index):
        return self._point_DataPoints[index]

    def __setitem__(self,index,value):
        self._point_DataPoints[index]=value

    def __delitem__(self,index):
        del self._point_DataPoints[index]

    def __iter__(self):
        return iter(self._point_DataPoints)

    def setDataPoints(self,variables):
        self._point_DataPoints=variables
        return self._point_DataPoints
    def addDataPoints(self,variables):
        self._point_DataPoints+=variables
        return self._point_DataPoints
    def getDataPoints(self):
        return self._point_DataPoints

#Object Data
class DataMenu(bLB.SelfOrigin):
    def __init__(self,dataMenu=None):
        super(DataMenu,self).__init__()
        if dataMenu is None:
            self._menuName_str=None
            self._menu_DataMenuParamArrays=[]
        elif type(dataMenu) is DataMenu:
            self._menuName_str=dataMenu.getName()
            self._menu_DataMenuParamArrays=dataMenu.getDataMeunParamArrays()

    def setName(self,variable):
        self._menuName_str=variable
        return self._menuName_str
    def getName(self):
        return self._menuName_str
    
    def setDataMeunParamArrays(self,variables):
        self._menu_DataMenuParamArrays=variables
        return self._menu_DataMenuParamArrays
    def addDataMeunParamArrays(self,variables):
        self._menu_DataMenuParamArrays+=variables
        return self._menu_DataMenuParamArrays
    def getDataMeunParamArrays(self):
        return self._menu_DataMenuParamArrays

class DataNode(bLB.SelfOrigin):
    def __init__(self,dataNode=None):
        super(DataNode,self).__init__()
        if dataNode is None:
            self._nodeName_str=None
            self._nodeType_str=None
            self._nodeUUID_str=None
        elif type(dataNode) is DataNode:
            self._nodeName_str=dataNode.getName()
            self._nodeType_str=dataNode.getType()
            self._nodeUUID_str=dataNode.getUUID()
        elif type(dataNode) is om2.MObject:
            node_MFnDependencyNode=om2.MFnDependencyNode(dataNode)
            self._nodeName_str=node_MFnDependencyNode.name()
            self._nodeType_str=node_MFnDependencyNode.typeName
            self._nodeUUID_str=node_MFnDependencyNode.uuid()
    
    def __str__(self):
        return str(self._nodeName_str)
    
    #Setting Function
    def findNode(self,variable):
        node_MSelectionList=om2.MGlobal.getSelectionListByName(variable)
        node_MObject=node_MSelectionList.getDependNode(0)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)

        self._nodeName_str=node_MFnDependencyNode.name()
        self._nodeType_str=node_MFnDependencyNode.typeName
        self._nodeUUID_str=node_MFnDependencyNode.uuid()

    def setName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getName(self):
        return self._nodeName_str
    
    def setType(self,variable):
        self._nodeType_str=variable
        return self._nodeType_str
    def getType(self):
        return self._nodeType_str
    
    def setUUID(self,variable):
        self._nodeUUID_str=variable
        return self._nodeUUID_str
    def getUUID(self):
        return self._nodeUUID_str

class DataPlug(bLB.SelfOrigin):
    def __init__(self,dataPlug=None):
        super(DataPlug,self).__init__()
        if dataPlug is None:
            self._node_DataNode=None
            self._attr_DataAttribute=None
            self._keyLock_bool=False
            self._valueLock_bool=False
            self._channelHide_bool=False
        elif type(dataPlug) is DataPlug:
            self._node_DataNode=dataPlug.getDataNode()
            self._attr_DataAttribute=dataPlug.getDataAttribute()
            self._keyLock_bool=dataPlug.getKeyLockState()
            self._valueLock_bool=dataPlug.getValueLockState()
            self._channelHide_bool=dataPlug.getHideState()
        elif type(dataPlug) is om2.MPlug:
            self._node_DataNode=DataNode(dataPlug.node())# MObject
            self._attr_DataAttribute=DataAttribute(dataPlug.attribute())# MObject
            self._keyLock_bool=not dataPlug.isKeyable
            self._valueLock_bool=dataPlug.isLocked
            self._channelHide_bool=not dataPlug.isChannelBox

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setDataAttribute(self,variable):
        self._attr_DataAttribute=variable
        return self._attr_DataAttribute
    def getDataAttribute(self):
        return self._attr_DataAttribute

    def setKeyLockState(self,variable):
        self._keyLock_bool=variable
        return self._keyLock_bool
    def getKeyLockState(self):
        return self._keyLock_bool
    
    def setValueLockState(self,variable):
        self._valueLock_bool=variable
        return self._valueLock_bool
    def getValueLockState(self):
        return self._valueLock_bool
    
    def setHideState(self,variable):
        self._channelHide_bool=variable
        return self._channelHide_bool
    def getHideState(self):
        return self._channelHide_bool

class DataPlugPair(bLB.SelfOrigin):
    def __init__(self):
        super(DataPlugPair,self).__init__()
        self._source_DataPlug=None
        self._target_DataPlug=None

    def setSourceDataPlugs(self,variable):
        self._source_DataPlug=variable
        return self._source_DataPlug
    def getSourceDataPlugs(self):
        return self._source_DataPlug
    
    def setTargetDataPlugs(self,variable):
        self._target_DataPlug=variable
        return self._target_DataPlug
    def getTargetDataPlugs(self):
        return self._target_DataPlug

class DataWeight(bLB.SelfOrigin):
    def __init__(self):
        super(DataWeight,self).__init__()
        self._weight_DataAttributeWeightArrays=[]

    def setDataAttributeWeightArrays(self,variable):
        self._weight_DataAttributeWeightArrays=variable
        return self._weight_DataAttributeWeightArrays
    def getDataAttributeWeightArrays(self):
        return self._weight_DataAttributeWeightArrays

class DataMesh(bLB.SelfOrigin):
    def __init__(self):
        super(DataMesh,self).__init__()
        self._polygon_DataFaces=[]

    def setDataFaces(self,variables):
        self._polygon_DataFaces=variables
        return self._polygon_DataFaces
    def getDataFaces(self):
        return self._polygon_DataFaces

class DataSurface(bLB.SelfOrigin):
    def __init__(self):
        super(DataSurface,self).__init__()

class DataCurve(bLB.SelfOrigin):
    def __init__(self):
        super(DataCurve,self).__init__()

#ObjectArray Data
class DataNodeArray():
    def __init__(self):
        super(DataNodeArray,self).__init__()
        self._node_DataNodes=[]

    def __len__(self):
        return len(self._node_DataNodes)

    def __getitem__(self,index):
        return self._node_DataNodes[index]

    def __setitem__(self,index,value):
        self._node_DataNodes[index]=value

    def __delitem__(self,index):
        del self._node_DataNodes[index]

    def __iter__(self):
        return iter(self._node_DataNodes)

    #Setting Function
    def setDataNodes(self,variables):
        self._node_DataNodes=variables
        return self._node_DataNodes
    def addDataNodes(self,variables):
        self._node_DataNodes+=variables
        return self._node_DataNodes
    def getDataNodes(self):
        return self._node_DataNodes

class DataPlugArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataPlugArray,self).__init__()
        self._plug_DataPlugs=[]

    def __len__(self):
        return len(self._plug_DataPlugs)

    def __getitem__(self,index):
        return self._plug_DataPlugs[index]

    def __setitem__(self,index,value):
        self._plug_DataPlugs[index]=value

    def __delitem__(self,index):
        del self._plug_DataPlugs[index]

    def __iter__(self):
        return iter(self._plug_DataPlugs)

    #Setting Function
    def setDataPlugs(self,variables):
        self._plug_DataPlugs=variables
        return self._plug_DataPlugs
    def addDataPlugs(self,variables):
        self._plug_DataPlugs+=variables
        return self._plug_DataPlugs
    def getDataPlugs(self):
        return self._plug_DataPlugs

class DataPlugPairArray(bLB.SelfOrigin):
    def __init__(self):
        super(DataPlugPairArray,self).__init__()
        self._connection_DataPlugPairs=[]

    def __len__(self):
        return len(self._connection_DataPlugPairs)

    def __getitem__(self,index):
        return self._connection_DataPlugPairs[index]

    def __setitem__(self,index,value):
        self._connection_DataPlugPairs[index]=value

    def __delitem__(self,index):
        del self._connection_DataPlugPairs[index]

    def __iter__(self):
        return iter(self._connection_DataPlugPairs)

    #Setting Function
    def setDataPlugPairs(self,variables):
        self._connection_DataPlugPairs=variables
        return self._connection_DataPlugPairs
    def addDataPlugPairs(self,variables):
        self._connection_DataPlugPairs+=variables
        return self._connection_DataPlugPairs
    def getDataPlugPairs(self):
        return self._connection_DataPlugPairs

#Action Data
class DataBind(bLB.SelfOrigin):
    def __init__(self):
        super(DataBind,self).__init__()
        self._mesh_DataNode=None
        self._joint_DataNodes=[]
        self._skicWeight_DataAttributeWeightArrays=[]
    
    #Setting Function
    def setMeshDataNode(self,variable):
        self._mesh_DataNode=variable
        return self._mesh_DataNode
    def getMeshDataNode(self):
        return self._mesh_DataNode

    def setJointDataNode(self,variables):
        self._joint_DataNodes=variables
        return self._joint_DataNodes
    def addJointDataNode(self,variables):
        self._joint_DataNodes+=variables
        return self._joint_DataNodes
    def getJointDataNode(self):
        return self._joint_DataNodes
    
    def setDataAttributeWeightArrays(self,variables):
        self._skicWeight_DataAttributeWeightArrays=variables
        return self._skicWeight_DataAttributeWeightArrays
    def addDataAttributeWeightArrays(self,variables):
        self._skicWeight_DataAttributeWeightArrays+=variables
        return self._skicWeight_DataAttributeWeightArrays
    def getDataAttributeWeightArrays(self):
        return self._skicWeight_DataAttributeWeightArrays

class DataKeyable(bLB.SelfOrigin):
    def __init__(self):
        super(DataKeyable,self).__init__()
        self._node_DataNode=None
        self._keyable_DataKeyArrays=[]

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataKeyArrays(self,variables):
        self._keyable_DataKeyArrays=variables
        return self._keyable_DataKeyArrays
    def addDataKeyArrays(self,variables):
        self._keyable_DataKeyArrays+=variables
        return self._keyable_DataKeyArrays
    def getDataKeyArrays(self):
        return self._keyable_DataKeyArrays

class DataKeyableWithMatrix(DataKeyable):
    def __init__(self):
        super(DataKeyable,self).__init__()
        #self._node_DataNode=None
        #self._keyable_DataKeyArrays=[]
        self._matrix_DataMatrixs=[]

    #Setting Function
    def setDataMatrix(self,variable):
        self._matrix_DataMatrix=variable
        return self._matrix_DataMatrix
    def getDataMatrix(self):
        return self._matrix_DataMatrix

class DataMatch(bLB.SelfOrigin):
    def __init__(self):
        super(DataMatch,self).__init__()
        self._node_DataNode=None
        self._match_DataNode=None
        self._match_DataMatrix=None

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setMatchDataNode(self,variable):
        self._match_DataNode=variable
        return self._match_DataNode
    def getMatchDataNode(self):
        return self._match_DataNode
    
    def setMatchDataMatrix(self,variable):
        self._match_DataMatrix=variable
        return self._match_DataMatrix
    def getMatchDataMatrix(self):
        return self._match_DataMatrix

class DataMirror(bLB.SelfOrigin):
    def __init__(self):
        super(DataMirror,self).__init__()
        self._node_DataNode=None
        self._pivot_DataNode=None
        self._pivot_DataMatrix=None
        self._mirrorAxis_str="x"
        self._mirrorOrientVector_str="z"

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setPivotDataNode(self,variable):
        self._pivot_DataNode=variable
        return self._pivot_DataNode
    def getPivotDataNode(self):
        return self._pivot_DataNode
    
    def setPivotDataMatrix(self,variable):
        self._pivot_DataMatrix=variable
        return self._pivot_DataMatrix
    def getPivotDataMatrix(self):
        return self._pivot_DataMatrix
    
    def setMirrorAxis(self,variable):
        self._mirrorAxis_str=variable
        return self._mirrorAxis_str
    def getMirrorAxis(self):
        return self._mirrorAxis_str

    def setMirrorOrientVector(self,variable):
        self._mirrorOrientVector_str=variable
        return self._mirrorOrientVector_str
    def getMirrorOrientVector(self):
        return self._mirrorOrientVector_str

class DataDrivenKey(bLB.SelfOrigin):
    def __init__(self):
        super(DataDrivenKey,self).__init__()
        self._node_DataNode=None
        self._source_DataPlugs=[]
        self._drivenKey_DataKeyArrays=[]

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataPlugs(self,variables):
        self._source_DataPlugs=variables
        return self._source_DataPlugs
    def addDataPlugs(self,variables):
        self._source_DataPlugs+=variables
        return self._source_DataPlugs
    def getDataPlugs(self):
        return self._source_DataPlugs

    def setDataKeyArrays(self,variables):
        self._drivenKey_DataKeyArrays=variables
        return self._drivenKey_DataKeyArrays
    def addDataKeyArrays(self,variables):
        self._drivenKey_DataKeyArrays+=variables
        return self._drivenKey_DataKeyArrays
    def getDataKeyArrays(self):
        return self._drivenKey_DataKeyArrays