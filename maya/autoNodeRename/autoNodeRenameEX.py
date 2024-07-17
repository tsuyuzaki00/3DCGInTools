import maya.cmds as cmds

import cgInTools as cit
from ...library import dataLB as dLB
from ..library import nameLB as nnLB
from ..library import nodeLB as nLB
cit.reloads([dLB,nnLB,nLB])

def main():
    node_DataPath=dLB.DataPath()
    node_DataPath.setAbsoluteDirectory(cit.maya_dir)
    node_DataPath.setRelativeDirectory("autoNodeRename")
    node_DataPath.setFile("autoNodeRenameEX")
    node_DataPath.setExtension("json")

    node_DataName=nnLB.DataNodoName()
    node_DataName.setOriginDataPath(node_DataPath)
    node_DataName.readJson()
    
    objs=cmds.ls(sl=True)
    for obj in objs:
        node_DataNode=nLB.DataNode()
        node_DataNode.setName(obj)

        node_AppNodeName=nLB.SelfDGNode()
        node_AppNodeName.setDataNode(node_DataNode)
        node_AppNodeName.setDataNodoName(node_DataName)
        node_AppNodeName.editRename()