# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import jointLB as jntLB
cit.reloads([jntLB])

def main():
    node_strs=cmds.ls(sl=True)
    if node_strs == []:
        jntLB.jointOnly()
        cmds.select(cl=True)
    else :
        for node_str in node_strs:
            trs=cmds.xform(node_str,q=True,ws=True,t=True)
            jntLB.jointOnly(p=trs)