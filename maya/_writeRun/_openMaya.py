# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2
import maya.api.OpenMayaAnim as oma2
import sys,math

def node_query_MObject(nodeName_str):
    if nodeName_str == None:
        return None
    elif not isinstance(nodeName_str,str):
        om2.MGlobal.displayError("Please insert one string in value")
        sys.exit()
    node_MSelectionList=om2.MGlobal.getSelectionListByName(nodeName_str)
    node_MObject=node_MSelectionList.getDependNode(0)
    return node_MObject

def convertMObject_query_MDagPath(node_MObject):
    node_MDagPath=om2.MDagPath().getAPathTo(node_MObject)
    return node_MDagPath

def nodeAttr_query_MPlug(node_MObject,attr_str):
    node_MFnDependencyNode=om2.MFnDependencyNode(node_MObject)
    node_MPlug=node_MFnDependencyNode.findPlug(attr_str,False)
    return node_MPlug

def main():
    node_MObject=node_query_MObject("pCube1")
    
    node_MDagModifier=om2.MDagModifier()
    newNode_MObject=node_MDagModifier.createNode("mesh",node_MObject)
    node_MDagModifier.doIt()

main()