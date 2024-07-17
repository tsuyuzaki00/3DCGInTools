# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import dataLB as dLB
from ..library import nameLB as nnLB
from ..library import nodeLB as nLB
cit.reloads([dLB,nnLB,nLB])

def main():
    test_DataPath=dLB.DataPath()
    test_DataPath.setAbsoluteDirectory(cit.maya_dir)
    test_DataPath.setRelativeDirectory("autoNodeReName")
    test_DataPath.setFile("autoNodeReNameEX")
    test_DataPath.setExtension("json")

    test_DataNodeName=nnLB.DataNodoName()
    test_DataNodeName.setOriginDataPath(test_DataPath)
    test_DataNodeName.setTitle("hoge")
    test_DataNodeName.setTagType("geo")
    test_DataNodeName.setSide("C")
    test_DataNodeName.setNumbers([0])
    test_DataNodeName.setHierarchys(["A"])
    test_DataNodeName.setCustoms(["test"])
    test_DataNodeName.setOrders(["Title_Hierarchys_0","TagType","Side"])
    test_DataNodeName.setIncrease("Hierarchys_0")
    test_DataNodeName.writeJson()

    #test_DataNode=nLB.DataNode()
    #test_DataNode.setName("pCube1")
    #test_DataNode.setType("geometory")

    #test_AppNodeName=aLB.AppNodeName()
    #test_AppNodeName.setDataName(test_DataName)
    #test_AppNodeName.setDataNode(test_DataNode)

    #test_AppNodeName.editRename()

main()