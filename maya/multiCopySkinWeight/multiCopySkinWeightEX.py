# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    node_strs=cmds.ls(sl=True,l=True)
    if len(node_strs) < 2:
        cmds.warning("At less 2 objects must be selected")
        return None
    else:
        sourceNode_str=node_strs[0]
        targetNode_strs=node_strs[1:]

    multiCopy_AppCopySkinWeight=sLB.AppCopySkinWeight()
    multiCopy_AppCopySkinWeight.setSourceNodeName(sourceNode_str)
    for targetNode_str in targetNode_strs:
        multiCopy_AppCopySkinWeight.setTargetNodeName(targetNode_str)
        multiCopy_AppCopySkinWeight.copyBind()
        multiCopy_AppCopySkinWeight.copySkinWeights()