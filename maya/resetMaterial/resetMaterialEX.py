# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import resetMaterialLB as rmLB
cit.reloads([rmLB])

def main():
    node_strs=cmds.ls(sl=True)
    for node_str in node_strs:
        rmLB.defaultMaterial_edit_func(node_str)