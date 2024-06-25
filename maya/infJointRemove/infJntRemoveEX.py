# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    node_str=cmds.ls(sl=True)[0]
    removeJoint=sLB.AppCopySkinWeight()
    removeJoint.setSourceNodeName(node_str)
    removeJoint.removeInfluenceJoint()