# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def defaultMaterial_edit_func(node_str,defMaterial_str="initialShadingGroup"):
    cmds.lockNode(defMaterial_str,l=False,lu=False)
    cmds.sets(node_str,e=True,forceElement=defMaterial_str)