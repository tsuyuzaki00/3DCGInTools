# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ...library import dataLB as dLB
from ...library import jsonLB as jLB
cit.reloads([dLB,jLB])

class AppColor():
    def __init__(self):
        super().__init__()
        colorIndex_DataPath=dLB.DataPath()
        colorIndex_DataPath.setAbsoluteDirectory(cit.ui_dir)
        colorIndex_DataPath.setFile("ui")
        colorIndex_DataPath.setExtension("json")
        
        colorIndex_AppJson=jLB.AppJson()
        colorIndex_AppJson.setDataPath(colorIndex_DataPath)
        self.__colorIndex_dicts=colorIndex_AppJson.read().get("colorIndex_dicts")
        self._node_str=None
        self._color_value=None

    #Single Function
    @staticmethod
    def drawingOverrideShape_query_strs(node_str):
        if cmds.nodeType(node_str)=="transform":
            shape_strs=cmds.listRelatives(node_str,type="nurbsCurve")
            if not shape_strs == None:
                return shape_strs
        elif cmds.nodeType(node_str)=="joint":
            return [node_str]
        else :
            cmds.error("Attribute Drowing Overrides is missing")

    @staticmethod
    def overrideColor_edit_func(shape_strs,color_value):
        use_int=0
        mode_int=0
        indexColor_int=0
        rgbColor_floats=[0,0,0]
        if isinstance(color_value,int):
            use_int=1
            indexColor_int=color_value
        elif isinstance(color_value,list) or isinstance(color_value,tuple):
            use_int=1
            mode_int=1
            rgbColor_floats=color_value
        for shape_str in shape_strs:
            cmds.setAttr(shape_str+".overrideEnabled",use_int)
            cmds.setAttr(shape_str+".overrideRGBColors",mode_int)
            cmds.setAttr(shape_str+".overrideColor",indexColor_int)
            cmds.setAttr(shape_str+".overrideColorRGB",*rgbColor_floats,type="double3")

    @staticmethod
    def wireColorShape_query_strs(curve_str):
        shape_strs=cmds.listRelatives(curve_str,shapes=True,ni=True,pa=True)
        curveAndShape_strs=[curve_str]+shape_strs
        return curveAndShape_strs

    @staticmethod
    def wireframeColor_edit_func(curveAndShape_strs,color_value,colorIndex_dicts):
        if isinstance(color_value,int):
            use_int=2
            color_value=colorIndex_dicts[color_value]["Wire"]
        elif isinstance(color_value,list) or isinstance(color_value,tuple):
            use_int=2
        else:
            use_int=0
            color_value=(0,0,0)
        for curveAndShape_str in curveAndShape_strs:
            cmds.setAttr(curveAndShape_str+'.useObjectColor',use_int)
            cmds.setAttr(curveAndShape_str+'.wireColorRGB',*color_value)

    #Setting Function
    def setNode(self,variable):
        self._node_str=variable
    def getNode(self):
        return self._node_str
    
    def setColor(self,variable):
        self._color_value=variable
    def getColor(self):
        return self._color_value

    #Public Function
    def overrideColor(self,node=None,color=None):
        _node_str=node or self._node_str 
        _color_value=color or self._color_value 

        shape_strs=self.drawingOverrideShape_query_strs(_node_str)
        self.overrideColor_edit_func(shape_strs,_color_value)
    
    def wireframeColor(self,node=None,color=None):
        _node_str=node or self._node_str
        _color_value=color or self._color_value
        
        nodeAndShape_strs=self.wireColorShape_query_strs(_node_str)
        self.wireframeColor_edit_func(nodeAndShape_strs,_color_value,self.__colorIndex_dicts)
