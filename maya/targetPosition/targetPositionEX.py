# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import targetPositionLB as tpLB
cit.reloads([tpLB])

def main():
    node_strs=cmds.ls(sl=True,fl=True)

    targetSet=tpLB.SourceToTarget()
    targetSet.setTargetNode(node_strs[-1])
    for source_str in node_strs[:-1]:
        targetSet.setSourceNode(source_str)
        targetSet.moveToTarget()