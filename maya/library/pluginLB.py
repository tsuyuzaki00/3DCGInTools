# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

def loadedOnOff_edit_func(pluginName_str=None):
    if pluginName_str == None:
        return
    if cmds.pluginInfo(pluginName_str,q=True,l=True):
        cmds.unloadPlugin(pluginName_str)
        print(pluginName_str+" OFF"),
    elif not cmds.pluginInfo(pluginName_str,q=True,l=True):
        cmds.loadPlugin(pluginName_str)
        print(pluginName_str+" ON")