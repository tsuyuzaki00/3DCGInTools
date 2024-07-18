import maya.cmds as cmds

import cgInTools as cit
from ...library import dataLB as dLB
from ..library import nameLB as nnLB
from ..library import nodeLB as nLB
cit.reloads([dLB,nnLB,nLB])

DATAFOLDER_STR="autoNodeRename"
RESET_DIR,DATA_DIR=cit.checkScriptsData(DATAFOLDER_STR,cit.maya_dir,cit.mayaData_dir)

def main():
    node_DataPath=dLB.DataPath()
    node_DataPath.setAbsoluteDirectory(cit.mayaData_dir)
    node_DataPath.setRelativeDirectory("autoNodeRename")
    node_DataPath.setFile("autoNodeRenameEX")
    node_DataPath.setExtension("json")

    node_DataNodeName=nnLB.DataNodeName()
    node_DataNodeName.setOriginDataPath(node_DataPath)
    node_DataNodeName.readJson()
    
    objs=cmds.ls(sl=True)
    for obj in objs:
        node_DataNode=nLB.DataNode()
        node_DataNode.setName(obj)

        node_AppNodeName=nLB.SelfDGNode()
        node_AppNodeName.setDataNode(node_DataNode)
        node_AppNodeName.setDataNodeName(node_DataNodeName)
        node_AppNodeName.editRename()