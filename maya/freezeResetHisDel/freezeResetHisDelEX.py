# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import sceneCleanLB as scLB
cit.reloads([scLB])

def main():
    node_strs=cmds.ls(sl=True,dag=True,tr=True)
    for node_str in node_strs:
        FRH_AppSceneClean=scLB.AppSceneClean()
        FRH_AppSceneClean.setNodeName(node_str)
        FRH_AppSceneClean.delFRH()