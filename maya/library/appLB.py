# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

import cgInTools as cit
from ...library import baseLB as bLB
from ...library import jsonLB as jLB
cit.reloads([bLB,jLB])

class AppConnect(bLB.SelfOrigin):
    def __init__(self):
        self._source_SelfNode=None
        self._target_SelfNode=None
        self._source_SelfPlug=None
        self._target_SelfPlug=None
        self._proxy_bool=False

    #Setting Function
    def setSourceSelfNode(self,variable):
        self._source_SelfNode=variable
        return self._source_SelfNode
    def getSourceSelfNode(self):
        return self._source_SelfNode
        
    def setTargetSelfNode(self,variable):
        self._target_SelfNode=variable
        return self._target_SelfNode
    def getTargetSelfNode(self):
        return self._target_SelfNode
    
    def setSourceSelfPlug(self,variable):
        self._source_SelfPlug=variable
        return self._source_SelfPlug
    def getSourceSelfPlug(self):
        return self._source_SelfPlug
        
    def setTargetSelfPlug(self,variable):
        self._target_SelfPlug=variable
        return self._target_SelfPlug
    def getTargetSelfPlug(self):
        return self._target_SelfPlug
    
    #Public Function
    def connectNode(self):
        pass

    def connectPlug(self):
        pass

class AppParent(bLB.SelfOrigin):
    def __init__(self):
        self._node_SelfDAGNode=None
        self._parent_SelfDAGNode=None
        self._child_SelfDAGNodes=[]

    #Setting Function
    def setSelfDAGNode(self,variable):
        self._node_SelfDAGNode=variable
        return self._node_SelfDAGNode
    def getSelfDAGNode(self):
        return self._node_SelfDAGNode
        
    def setParentSelfDAGNode(self,variable):
        self._parent_SelfDAGNode=variable
        return self._parent_SelfDAGNode
    def getParentSelfDAGNode(self):
        return self._parent_SelfDAGNode
    
    def setChildSelfDAGNodes(self,variables):
        self._child_SelfDAGNodes=variables
        return self._child_SelfDAGNodes
    def addChildSelfDAGNodes(self,variables):
        self._child_SelfDAGNodes+=variables
        return self._child_SelfDAGNodes
    def getChildSelfDAGNodes(self):
        return self._child_SelfDAGNodes
    
    #Public Function
    def parent(self):
        pass

    def childs(self):
        pass



    