# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
form .. import AttributeLB as aLB
cit.reloads([bLB,jLB])

class DataNode(bLB.SelfOrigin):
    def __init__(self,dataNode=None):
        super(DataNode,self).__init__()
        if dataNode is None:
            self._nodeName_str=None
            self._nodeType_str=None
        elif type(dataNode) is DataNode:
            self._nodeName_str=dataNode.getName()
            self._nodeType_str=dataNode.getType()
        elif type(dataNode) is om2.MObject:
            node_MFnDependencyNode=om2.MFnDependencyNode(dataNode)
            self._nodeName_str=node_MFnDependencyNode.name()
            self._nodeType_str=node_MFnDependencyNode.typeName

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

class SelfDGNode(bLB.SelfOrigin):
    def __init__(self,selfDGNode=None):
        super(SelfDGNode,self).__init__()
        if type(selfDGNode) is SelfDGNode:
            self._node_DataNode=selfDGNode.getDataNode()
            self._name_DataName=selfDGNode.getDataName()
            self._attrName_str=None
        else:
            self._node_DataNode=None
            self._name_DataName=None
            self._attrName_str=None
        self._dataChoice_strs+=[
            "DataNode",
            "DataName",
            "AttributeName"
        ]
        self._doIt_strs+=[
            "createNode",
            "duplicateNode",
            "rename",
            "searchDataAttribute",
            "searchDataPlug"
        ]
    
    #Single Function
    def node_query_MObject(self,node):
        if node == None:
            return None
        elif not isinstance(node,str):
            om2.MGlobal.displayError("Please insert one string in value")
            sys.exit()
        node_MSelectionList=om2.MGlobal.getSelectionListByName(node)
        node_MObject=node_MSelectionList.getDependNode(0)
        return node_MObject
    
    def node_create_func(self,nodeName_str,nodeType_str):
        node_MFnDependencyNode=om2.MFnDependencyNode()
        node_MFnDependencyNode.create(nodeType_str)
        node_MFnDependencyNode.setName(nodeName_str)

    def findAttr_create_DataAttribute(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        attr_MObject=node_MFnDependencyNode.findAlias(attrName_str)
        plug_DataAttribute=aLB.DataAttribute(attr_MObject)
        return plug_DataAttribute
    
    def findPlug_create_DataPlug(self,node_MObject,attrName_str):
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        plug_MPlug=node_MFnDependencyNode.findPlug(attrName_str,False)
        plug_DataPlug=aLB.DataPlug(plug_MPlug)
        return plug_DataPlug

    #Setting Function
    def setDataNode(self,variable):
        self._node_DataNode=variable
        return self._node_DataNode
    def getDataNode(self):
        return self._node_DataNode

    def setDataName(self,variable):
        self._name_DataName=variable
        return self._name_DataName
    def getDataName(self):
        return self._name_DataName
    
    def setAttributeName(self,variable):
        self._attrName_str=variable
        return self._attrName_str
    def getAttributeName(self):
        return self._attrName_str
    
    #Public Function
    def createNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        self.node_create_func(_node_DataNode.getName(),_node_DataNode.getType())

    def duplicateNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

    def rename(self):
        pass

    def searchDataAttribute(self,dataNode=None,attrName=None):
        _node_DataNode=dataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(_node_DataNode.getName())
        attr_DataAttribute=self.findAttr_create_DataAttribute(node_MObject,_attrName_str)
        return attr_DataAttribute

    def searchDataPlug(self,node_DataNode=None,attrName=None):
        _node_DataNode=node_DataNode or self._node_DataNode
        _attrName_str=attrName or self._attrName_str

        node_MObject=self.node_query_MObject(_node_DataNode.getName())
        plug_DataPlug=self.findPlug_create_DataPlug(node_MObject,_attrName_str)
        return plug_DataPlug

    def queryName(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=self._node_DataNode.getName()
        return nodeName_str

    def queryUUID(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=self._node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
        uuid_MUuid=node_MFnDependencyNode.uuid()
        return uuid_MUuid

class SelfDAGNode(SelfDGNode):
    def __init__(self):
        super(SelfDAGNode,self).__init__()
        #self._node_DataNode=None
        #self._name_DataName=None
        #self._attrName_strs=[]
        self._matrix_DataMatrix=None
        self._parent_DataNode=None
        self._child_DataNodes=[]
        self._match_DataNode=None
        self._pivot_DataNode=None

        self._dataChoice_strs+=[
            "DataMatrix",
            "FullPath"
        ]
        self._doIt_strs+=[
            "parent",
            "replaceByParent",
            "replaceByChild",
            "replaceByShape"
        ]
    
    #Single Function
    def convertMObject_create_MDagPath(self,node_MObject):
        node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
        return node_MDagPath
    
    def shape_query_MObject(self,node_MDagPath):
        shape_MDagPath=node_MDagPath.extendToShape()
        shape_MObject=shape_MDagPath.node()
        return shape_MObject

    def parent_query_MObject(self,node_MDagPath):
        node_MFnDagNode=om2.MFnDagNode(node_MDagPath)
        parent_MObject=node_MFnDagNode.parent(0)
        return parent_MObject

    def child_query_MObjects(self,node_MDagPath,shapeOnly=False):
        childs=[]
        for num in range(node_MDagPath.childCount()):
            child_MObject=node_MDagPath.child(num)
            if shapeOnly:
                if child_MObject.hasFn(om2.MFn.kShape):
                    childs.append(child_MObject)
            else:
                if not child_MObject.hasFn(om2.MFn.kShape):
                    childs.append(child_MObject)
        if childs == []:
            return None
        else:
            return childs

    #Setting Function
    def setDataMatrix(self,variable):
        self._matrix_DataMatrix=variable
        return self._matrix_DataMatrix
    def getDataMatrix(self):
        return self._matrix_DataMatrix
    
    def setParentDataNode(self,variable):
        self._parent_DataNode=variable
        return self._parent_DataNode
    def getParentDataNode(self):
        return self._parent_DataNode
    
    def setChildDataNodes(self,variables):
        self._child_DataNodes=variable
        return self._child_DataNodes
    def addChildDataNodes(self,variables):
        self._child_DataNodes+=variables
        return self._child_DataNodes
    def getChildDataNodes(self):
        return self._child_DataNodes
    
    def setMatchDataNode(self,variable):
        self._match_DataNode=variable
        return self._match_DataNode
    def getMatchDataNode(self):
        return self._match_DataNode
    
    def setPivotDataNode(self,variable):
        self._pivot_DataNode=variable
        return self._pivot_DataNode
    def getPivotDataNode(self):
        return self._pivot_DataNode
    
    #Public Function
    def doParent(self,dataNode=None,parentDataNode=None):
        _node_DataNode=dataNode or self._node_DataNode
        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)

        _parent_DataNode=parentDataNode or self._parent_DataNode
        parentName_str=_parent_DataNode.getName()
        parent_MObject=self.node_query_MObject(parentName_str)
        parent_MDagPath=self.convertMObject_create_MDagPath(parent_MObject)

        parent_MDagModifier=om2.MDagModifier()
        parent_MDagModifier.reparentNode(node_MDagPath,parent_MDagPath)
        parent_MDagModifier.doIt()

    def doChilds(self,dataNode=None,childDataNodes=None):
        _node_DataNode=dataNode or self._node_DataNode
        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)

        _child_DataNodes=childDataNodes or self._child_DataNodes
        for _child_DataNode in _child_DataNodes:
            childName_str=_child_DataNode.getName()
            child_MObject=self.node_query_MObject(childName_str)
            child_MDagPath=self.convertMObject_create_MDagPath(child_MObject)

            child_MDagModifier=om2.MDagModifier()
            child_MDagModifier.reparentNode(child_MDagPath,node_MDagPath)
            child_MDagModifier.doIt()

    def queryFullPathName(self):
        nodeName_str=self._node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)

        name_str=node_MDagPath.fullPathName()
        return name_str

    def queryShapeSelfDAGNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        shape_MObject=self.shape_query_MObject(node_MDagPath)
        shape_DataNode=DataNode(shape_MObject)

        shape_SelfDAGNode=SelfDAGNode()
        shape_SelfDAGNode.setDataNode(shape_DataNode)
        return shape_SelfDAGNode

    def queryParentSelfDAGNode(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        parent_MObject=self.parent_query_MObject(node_MDagPath)
        parent_DataNode=DataNode(parent_MObject)

        parent_SelfDAGNode=SelfDAGNode()
        parent_SelfDAGNode.setDataNode(parent_DataNode)
        return parent_SelfDAGNode
    
    def queryChildSelfDAGNodes(self,dataNode=None):
        _node_DataNode=dataNode or self._node_DataNode

        nodeName_str=_node_DataNode.getName()
        node_MObject=self.node_query_MObject(nodeName_str)
        node_MDagPath=self.convertMObject_create_MDagPath(node_MObject)
        child_MObjects=self.child_query_MObjects(node_MDagPath,shapeOnly=False)

        child_SelfDAGNodes=[]
        for child_MObject in child_MObjects:
            child_DataNode=DataNode(child_MObject)
            child_SelfDAGNode=SelfDAGNode()
            child_SelfDAGNode.setDataNode(child_DataNode)
            child_SelfDAGNodes.append(child_SelfDAGNode)

        return child_SelfDAGNodes
    
    def editTransform(self):
        pass

    def editTranslate(self):
        pass

    def editRotation(self):
        pass

    def editQuaternion(self):
        pass

    def editScale(self):
        pass

    def editShear(self):
        pass

    def matchTransform(self):
        pass
    
    def matchTranslate(self):
        pass

    def matchRotation(self):
        pass
    
    def matchQuaternion(self):
        pass
    
    def matchAimVector(self):
        pass
    
    def matchScale(self):
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
    
    def mirrorShear(self):
        pass
