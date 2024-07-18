# -*- coding: iso-8859-15 -*-
import math
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from . import openMayaLB as omLB
from . import nameLB as nnLB
from . import matrixLB as mLB
cit.reloads([bLB,omLB,nnLB,mLB])

class DataNode(bLB.DataOrigin):
    def __init__(self,*dataTuple):
        super(DataNode,self).__init__(*dataTuple)
        if (0 == len(dataTuple) or 
            2 <= len(dataTuple)):
            self._nodeName_str=None
            self._nodeType_str=None
            self._dataChoice_strs=[
                "Name",
                "Type"
            ]
        elif 1 == len(dataTuple):
            if isinstance(dataTuple[0],DataNode):
                self._nodeName_str=dataTuple[0].getName()
                self._nodeType_str=dataTuple[0].getType()
            elif isinstance(dataTuple[0],om2.MObject):
                node_MFnDependencyNode=om2.MFnDependencyNode(dataTuple[0])
                self._nodeName_str=node_MFnDependencyNode.name()
                self._nodeType_str=node_MFnDependencyNode.typeName
                self._dataChoice_strs=[
                    "Name",
                    "Type"
                ]

    def __str__(self):
        return str(self._nodeName_str)
    
    #Setting Function
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
    
    #Public Function
    def readDict(self, setting_dict=None):
        return super().readDict(setting_dict)
    def readXML(self, dataPath=None):
        return super().readXML(dataPath)

class AppNode(omLB.AppOpenMayaBase):
    def __init__(self):
        super(AppNode,self).__init__()
        self._node_DataNode=None
        self._parent_DataNode=None
        self._child_DataNodes=[]

    #Inheritance Function
    def _parent_edit_func(self,node_str,parent_str):
        node_MObject=self.node_query_MObject(node_str)
        
        parent_MObject=self.node_query_MObject(parent_str)

        parent_MDagModifier=om2.MDagModifier()
        parent_MDagModifier.reparentNode(node_MObject,parent_MObject)
        parent_MDagModifier.doIt()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode
    
    def setParentDataNode(self,variable):
        self._parent_DataNode=variable
        return self._parent_DataNode
    def currentParentDataNode(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        self._parent_DataNode=DataNode(parent_MObject)
        return self._parent_DataNode
    def getParentDataNode(self):
        return self._parent_DataNode
    
    def setChildDataNodes(self,variables):
        self._child_DataNodes=variables
        return self._child_DataNodes
    def currentChildDataNodes(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        self._child_DataNodes=[]
        for child_MObject in child_MObjects:
            child_DataNode=DataNode(child_MObject)
            self._child_DataNodes.append(child_DataNode)
        return self._child_DataNodes
    def getChildDataNodes(self):
        return self._child_DataNodes
    
    #Public Function
    def create(self):
        node_MObject=self.node_create_MObject(self._node_DataNode.getType(),self._node_DataNode.getName())
        node_DataNode=DataNode(node_MObject)
        return node_DataNode

    def moveParent(self):
        self._parent_edit_func(self._node_DataNode.getName(),self._parent_DataNode.getName())

    def worldParent(self):
        cmds.parent(self._node_DataNode.getName(),w=True)

    def addChilds(self):
        for _child_DataNode in self._child_DataNodes:
            self._parent_edit_func(_child_DataNode.getName(),self._node_DataNode.getName())

    def removeChilds(self):
        for _child_DataNode in self._child_DataNodes:
            cmds.parent(_child_DataNode.getName(),w=True)

    def queryName(self):
        nodeName_str=self._node_DataNode.getName()
        return nodeName_str

    def queryFullPathName(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        fullPathName_str=node_MFnDagNode.fullPathName()
        return fullPathName_str

    def queryParentName(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_MFnDependencyNode=om2.MFnDependencyNode(parent_MObject)
        parentName_str=parent_MFnDependencyNode.name()
        return parentName_str

    def queryFullPathParentName(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_MDagPath=self.convertMObject_query_MDagPath(parent_MObject)
        node_MFnDagNode=om2.MFnDagNode(parent_MDagPath)
        fullPathName_str=node_MFnDagNode.fullPathName()
        if fullPathName_str is "" or fullPathName_str is None:
            return None
        return fullPathName_str

    def queryChildNames(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        if child_MObjects is None:
            return None
        childName_strs=[]
        for child_MObject in child_MObjects:
            child_MFnDependencyNode=om2.MFnDependencyNode(child_MObject)
            childName_str=child_MFnDependencyNode.name()
            childName_strs.append(childName_str)
        return childName_strs

    def queryFullPathChildNames(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath)
        if child_MObjects is None:
            return None
        fullPathName_strs=[]
        for child_MObject in child_MObjects:
            child_MDagPath=self.convertMObject_query_MDagPath(child_MObject)
            child_MFnDagNode=om2.MFnDagNode(child_MDagPath)
            fullPathName_str=child_MFnDagNode.fullPathName()
            fullPathName_strs.append(fullPathName_str)
        return fullPathName_strs

    def queryShapeNames(self):
        node_MObject=self.node_query_MObject(self._node_DataNode.getName())
        node_MDagPath=self.convertMObject_query_MDagPath(node_MObject)
        shape_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=True)
        shapeName_strs=[]
        for shape_MObject in shape_MObjects:
            shape_MFnDependencyNode=om2.MFnDependencyNode(shape_MObject)
            shapeName_str=shape_MFnDependencyNode.name()
            shapeName_strs.append(shapeName_str)
        return shapeName_strs
    
class SelfDGNode(bLB.SelfOrigin):
    def __init__(self,selfObject=None):
        super(SelfDGNode,self).__init__(selfObject)
        if selfObject is None:
            self._node_DataNode=None
            self._name_DataNodeName=None
            self._create_DataNode=None
            self._create_DataPlugs=None
            self._edit_DataPlugs=None
            self._connect_DataConnectPlugs=None
            self._anim_DataKeyable=None
            self._driven_DataKeyable=None
        elif isinstance(selfObject,SelfDGNode):
            self._node_DataNode=selfObject.getDataNode()
            self._name_DataNodeName=selfObject.getDataNodeName()
            self._create_DataNode=selfObject.getCreateDataNode()
            self._create_DataPlugs=selfObject.getCreateDataPlugs()
            self._edit_DataPlugs=selfObject.getEditDataPlugs()
            self._connect_DataPlugConnects=selfObject.getDataConnectPlugs()
            self._anim_DataKeyable=selfObject.getAnimDataKeyable()
            self._driven_DataKeyable=selfObject.getDrivenDataKeyable()

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataNodeName(self,variable):
        self._name_DataNodeName=variable
        return self._name_DataNodeName
    def getDataNodeName(self):
        return self._name_DataNodeName

    def setCreateDataNode(self,variable):
        self._create_DataNode=variable
        return self._create_DataNode
    def getCreateDataNode(self):
        return self._create_DataNode
    
    def setCreateDataPlugs(self,variable):
        self._create_DataPlugs=variable
        return self._create_DataPlugs
    def getCreateDataPlugs(self):
        return self._create_DataPlugs

    def setEditDataPlugs(self,variable):
        self._edit_DataPlugs=variable
        return self._edit_DataPlugs
    def getEditDataPlugs(self):
        return self._edit_DataPlugs

    def setDataConnectPlugs(self,variable):
        self._connect_DataConnectPlugs=variable
        return self._connect_DataConnectPlugs
    def getDataConnectPlugs(self):
        return self._connect_DataConnectPlugs
    
    def setAnimDataKeyable(self,variable):
        self._anim_DataKeyable=variable
        return self._anim_DataKeyable
    def getAnimDataKeyable(self):
        return self._anim_DataKeyable
        
    def setDrivenDataKeyable(self,variable):
        self._driven_DataDrivenKey=variable
        return self._driven_DataDrivenKey
    def getDrivenDataKeyable(self):
        return self._driven_DataDrivenKey

    #Public Function
    def createNode(self,dataNode=None,dataName=None):
        _create_DataNode=dataNode or self._create_DataNode
        _name_DataNodeName=dataName or self._name_DataNodeName

        name_AppName=nnLB.AppNodeName()
        name_AppName.setDataNodeName(_name_DataNodeName)
        name_str=name_AppName.create()
        _create_DataNode.setName(name_str)

        node_AppNode=AppNode()
        node_AppNode.setDataNode(_create_DataNode)
        self._node_DataNode=node_AppNode.create()
        return self._node_DataNode
    
    def createNodeNormal(self,dataNode=None):
        _create_DataNode=dataNode or self._create_DataNode

        node_AppNode=AppNode()
        node_AppNode.setDataNode(_create_DataNode)
        self._node_DataNode=node_AppNode.create()
        return self._node_DataNode

    def createAttrs(self,dataPlugs=None):
        pass

    def rename(self,dataNode=None,dataName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _name_DataNodeName=dataName or self._name_DataNodeName

        rename_AppNodeName=nnLB.AppNodeName()
        rename_AppNodeName.setDataNode(_node_DataNode)
        rename_AppNodeName.setDataNodeName(_name_DataNodeName)
        rename_str=rename_AppNodeName.rename()
        return rename_str
    
    def editRename(self,dataNode=None,dataName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _name_DataNodeName=dataName or self._name_DataNodeName

        rename_AppNodeName=nnLB.AppNodeName()
        rename_AppNodeName.setDataNode(_node_DataNode)
        rename_AppNodeName.setDataNodeName(_name_DataNodeName)
        rename_str=rename_AppNodeName.editRename()
        return rename_str

    def editAttrs(self,dataPlugs=None):
        pass
    
    def editConnects(self,dataPlugPairs=None):
        pass
    
    def editKeyable(self,dataKeyable=None):
        pass
    
    def editDrivenKey(self,dataDrivenKey=None):
        pass

    def queryName(self):
        nodeName_str=self._node_DataNode.getName()
        return nodeName_str
        
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        nodeName_str=node_AppNode.queryName()
        return nodeName_str
    
    def queryAttributes(self):
        pass

    def queryConnects(self):
        pass

    def queryKeyable(self):
        pass
    
    def queryDrivenKey(self):
        pass

class SelfDAGNode(SelfDGNode):
    def __init__(self,selfObject=None):
        super(SelfDAGNode,self).__init__(selfObject)
        if selfObject is None:
            self._parent_DataNode=None
            self._child_DataNodes=None
            self._shape_DataNodes=None
            self._edit_DataMatrix=None
            self._translate_DataTranslate=None
            self._rotate_DataRotation=None
            self._quaternion_DataQuaternion=None
            self._scale_DataScale=None
            self._match_DataMatch=None
            self._mirror_DataMirror=None
        elif isinstance(selfObject,SelfDAGNode):
            self._parent_DataNode=selfObject.getParentDataNode()
            self._child_DataNodes=selfObject.getChildDataNodes()
            self._shape_DataNodes=selfObject.getShapeDataNodes()
            self._edit_DataMatrix=selfObject.getDataMatrix()
            self._translate_DataTranslate=selfObject.getDataTranslate()
            self._rotate_DataRotation=selfObject.getDataRotation()
            self._quaternion_DataQuaternion=selfObject.getDataQuaternion()
            self._scale_DataScale=selfObject.getDataScale()
            self._match_DataMatch=selfObject.getDataMatch()
            self._mirror_DataMirror=selfObject.getDataMirror()
    
    #Setting Function
    def setParentDataNode(self,variable):
        self._parent_DataNode=variable
        return self._parent_DataNode
    def currentParentDataNode(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        self._parent_DataNode=node_AppNode.currentParentDataNode()
        return self._parent_DataNode
    def getParentDataNode(self):
        return self._parent_DataNode
    
    def setChildDataNodes(self,variable):
        self._child_DataNodes=variable
        return self._child_DataNodes
    def currentChildDataNodes(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        self._child_DataNodes=node_AppNode.currentChildDataNodes()
        return self._child_DataNodes
    def getChildDataNodes(self):
        return self._child_DataNodes
    
    def setShapeDataNodes(self,variable):
        self._shape_DataNodes=variable
        return self._shape_DataNodes
    def getShapeDataNodes(self):
        return self._shape_DataNodes

    def setDataMatrix(self,variable):
        self._edit_DataMatrix=variable
        return self._edit_DataMatrix
    def getDataMatrix(self):
        return self._edit_DataMatrix
    
    def setDataTranslate(self,variable):
        self._translate_DataTranslate=variable
        return self._translate_DataTranslate
    def getDataTranslate(self):
        return self._translate_DataTranslate
    
    def setDataRotation(self,variable):
        self._rotate_DataRotation=variable
        return self._rotate_DataRotation
    def getDataRotation(self):
        return self._rotate_DataRotation
    
    def setDataQuaternion(self,variable):
        self._quaternion_DataQuaternion=variable
        return self._quaternion_DataQuaternion
    def getDataQuaternion(self):
        return self._quaternion_DataQuaternion
    
    def setDataScale(self,variable):
        self._scale_DataScale=variable
        return self._scale_DataScale
    def getDataScale(self):
        return self._scale_DataScale

    def setDataMatch(self,variable):
        self._match_DataMatch=variable
        return self._match_DataMatch
    def getDataMatch(self):
        return self._match_DataMatch
    
    def setDataMirror(self,variable):
        self._mirror_DataMirror=variable
        return self._mirror_DataMirror
    def getDataMirror(self):
        return self._mirror_DataMirror
    
    #Public Function
    def moveParent(self,dataNode=None,parentDataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        _parent_DataNode=parentDataNode or self._parent_DataNode

        node_AppNode=AppNode()
        node_AppNode.setDataNode(_node_DataNode)
        node_AppNode.setParentDataNode(_parent_DataNode)
        node_AppNode.moveParent()

    def worldParent(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        node_AppNode=AppNode()
        node_AppNode.setDataNode(_node_DataNode)
        node_AppNode.worldParent()

    def addChilds(self,dataNode=None,childDataNodes=None):
        _node_DataNode=dataNode or self._node_DataNode
        _child_DataNodes=childDataNodes or self._child_DataNodes

        node_AppNode=AppNode()
        node_AppNode.setDataNode(_node_DataNode)
        node_AppNode.setChildDataNodes(_child_DataNodes)
        node_AppNode.addChilds()

    def removeChilds(self,childDataNodes=None):
        _child_DataNodes=childDataNodes or self._child_DataNodes

        node_AppNode=AppNode()
        node_AppNode.setChildDataNodes(_child_DataNodes)
        node_AppNode.removeChilds()

    def editTransform(self):
        pass
    
    def editTransformByMatrix(self):
        _node_DataNode=self._node_DataNode
        _edit_DataMatrix=self._edit_DataMatrix

        edit_AppDAGNode=AppDAGNode()
        edit_AppDAGNode.setDataNode(_node_DataNode)
        edit_AppDAGNode.setDataMatrix(_edit_DataMatrix)
        edit_AppDAGNode.editTransform()

    def editTranslate(self):
        pass
    
    def editTranslateByMatrix(self):
        pass

    def editRotation(self):
        pass
    
    def editRotationByMatrix(self):
        pass

    def editQuaternion(self):
        pass

    def editAimVector(self):
        pass

    def editScale(self):
        pass
    
    def editScaleByMatrix(self):
        pass
    
    def editShear(self):
        pass

    def matchTransform(self):
        pass
    
    def matchTransformByMatrix(self):
        pass
    
    def matchTranslate(self):
        pass
    
    def matchTranslateByMatrix(self):
        pass

    def matchRotation(self):
        pass
    
    def matchRotationByMatrix(self):
        pass
    
    def matchQuaternion(self):
        pass
    
    def matchAimVector(self):
        pass
    
    def matchScale(self):
        pass
    
    def matchScaleByMatrix(self):
        pass
    
    def matchShear(self):
        pass

    def mirrorTransform(self):
        pass

    def mirrorTranslate(self):
        pass
    
    def mirrorRotation(self):
        pass

    def mirrorQuaternion(self):
        pass

    def mirrorScale(self):
        pass

    def queryFullPathName(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        fullPathName_str=node_AppNode.queryFullPathName()
        return fullPathName_str
    
    def queryParentName(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        parentName_str=node_AppNode.queryParentName()
        return parentName_str
    
    def queryFullPathParentName(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        fullPathParentName_str=node_AppNode.queryFullPathParentName()
        return fullPathParentName_str
    
    def queryParentOfDataNode(self):
        pass

    def queryChildNames(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        childName_strs=node_AppNode.queryChildNames()
        return childName_strs
    
    def queryFullPathChildNames(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        fullPathChildName_strs=node_AppNode.queryFullPathChildNames()
        return fullPathChildName_strs
    
    def queryChildOfDataNodes(self):
        pass

    def queryShapeNames(self):
        node_AppNode=AppNode()
        node_AppNode.setDataNode(self._node_DataNode)
        shapeName_strs=node_AppNode.queryShapeNames()
        return shapeName_strs

    def queryTranslate(self):
        pass
    
    def queryDataTranslate(self):
        pass

    def queryRotation(self):
        pass
    
    def queryDataRotation(self):
        pass

    def queryQuaternion(self):
        pass
    
    def queryDataQuaternion(self):
        pass

    def queryScale(self):
        pass
    
    def queryDataScale(self):
        pass

    def queryNormalDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryWorldDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryParentDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryInverseNormalDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryInverseWorldDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
    
    def queryInverseParentDataMatrix(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        node_DataMatrix=None
        return node_DataMatrix
