# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from cgInTools.maya.library import curveLB as cLB
cit.reloads([cLB])

def main():
    sourceNode=cmds.ls(sl=True)[0]
    targetNodes=cmds.ls(sl=True)[1:]

    replace=cLB.AppCurve()
    replace.setSourceCurve(sourceNode)
    for targetNode in targetNodes:
        replace.setTargetCurve(targetNode)
        replace.replaceShape()