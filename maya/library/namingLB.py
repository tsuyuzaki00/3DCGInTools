# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
from . import attributeLB as aLB
cit.reloads([sbLB,jLB,aLB])

rules_dict=jLB.getJson(cit.mayaSettings_path,"namingLB")

class Naming(sbLB.BaseName):
    def __init__(self):
        super(Naming,self).__init__()

    def __loading(self):
        self._titleNum=self._title+self.rangeNumber_query_str(self._title)
        self._nodeNum=self._node+self.rangeNumber_query_str(self._node)
        self._sideNum=self._side+self.rangeNumber_query_str(self._side)
        self._num=self._numberName_query_str(self._orders)
        self._titleHie=self._title+self._hierarchy
        self._scene=self.scene_query_str()

    def __getStringAttr(self):
        addStringAttrs=[
            {"attrName":"titleName","attrString":self._title},
            {"attrName":"nodeName","attrString":self._node},
            {"attrName":"sideName","attrString":self._side},
            {"attrName":"numberName","attrString":self._num},
            {"attrName":"hierarchyName","attrString":self._hierarchy},
        ]
        return addStringAttrs

    #Single Function
    def isNodeType_query_str(self,obj):
        objType_str=cmds.objectType(obj)
        if objType_str=="transform":
            shape_list = cmds.listRelatives(obj,s=True)
            if shape_list==None:
                return "none"
            else :
                shapeType_str=cmds.objectType(shape_list[0])
                return shapeType_str
        else :
            objType_str=cmds.objectType(obj)
            return objType_str

    def sideName_query_str(self,obj,dist=1):
        boundingBox=cmds.xform(obj,q=True,bb=True,ws=True)
        minX=boundingBox[0]
        maxX=boundingBox[3]
        if minX > dist and maxX > dist:
            return "L"
        elif minX < -dist and maxX < -dist:
            return "R"
        else:
            return "C"

    def smashNumber_edit_str(self,name):
        if name == None:
            return None
        while name[-1].isdigit():
            name=name[:-1]
            if name=="":
                return None
        return name
    
    def smashAlphabet_edit_str(self,name):
        if name == None:
            return None
        while name[-1].isupper():
            name=name[:-1]
            if name=="":
                return None
        return name

    def rangeNumber_query_str(self,name):
        for i in range(100):
            if i is None:
                cmds.error("Can't go over 99.")
            while name[-1].isdigit():
                name=name[:-1]
            same_list=cmds.ls("*"+name+str(i).zfill(2)+"*",dag=True)
            if same_list == []:
                return str(i).zfill(2)

    def rangeAlphabet_query_str(self,name):
        for i in range(65, 91):
            if i is None:
                cmds.error("Can't go over Z.")
            if name[-1].isupper():
                name=name[:-1]
            same_list=cmds.ls("*"+name+chr(i)+"*",dag=True)
            if same_list == []:
                return chr(i)

    def firstLowerCaseOnly_edit_str(str):
        str=str[0].lower()+str[1:]
        return str

    def scene_query_str(self):
        sceneName=cmds.file(q=True,sn=True).split("/")[-1]
        sceneName=sceneName.split(".")[0]
        sceneParent=cmds.workspace(q=True,sn=True).split("/")[-1]
        if sceneName == "":
            self.scene=sceneParent
        else:
            self.scene=sceneName
        return self.scene

    #Multi Function
    def _nodeName_query_str(self,obj):
        getNode_str=self.isNodeType_query_str(obj)
        nodeName_str=rules_dict["nodeName_dict"][getNode_str]
        return nodeName_str

    #Private Function
    def _titleName_query_str(self,obj,delAlph=True):
        splitObjs=obj.split("_")
        self._nodeName_query_str(obj)
        self.sideName_query_str(obj)
        for l in range(len(splitObjs)):
            if delAlph:
                smashName=self.smashAlphabet_edit_str(splitObjs[l])
            else:
                smashName=splitObjs[l]
            if not splitObjs[l].isdigit():
                name=self.smashNumber_edit_str(smashName)
                if not name==self._nodeName_query_str(obj) and\
                   not name==self.sideName_query_str(obj) and\
                   not name==None:
                    return name

    def _numberName_query_str(self,orders):
        if "num" in orders:
            index=orders.index("num")
            orderName=self._orderName_query_str(orders)
            for num in range(100):
                splitNum=orderName.split("_")[index]
                replaceName=orderName.replace(splitNum,str(num).zfill(2))
                if not cmds.objExists(replaceName):
                    return str(num).zfill(2)
        else:
            return str(0).zfill(2)

    def _orderName_query_str(self,orders):
        self.__loading()
        nullDel_list=[]
        for order in orders:
            if not order == "none" and not order == "":
                nullDel_list.append(order)
        order_list=[]
        for chengeSelf in nullDel_list:
            add=eval("self._"+chengeSelf)
            order_list.append(add)
        self._orderName = "_".join(order_list)
        return self._orderName

    def _getAlphabet_query_str(self,obj):
        splitObjs=obj.split("_")
        for i in range(len(splitObjs)):
            if splitObjs[i][-1].isupper() and len(splitObjs[i])>1:
                return splitObjs[i][-1]

    #Public Function
    def rename(self):
        name=self.getRename()
        rename=cmds.rename(self._object,name)
        return rename

    def getRename(self):
        if self._switch=="fullAuto":
            self._title=self._titleName_query_str(self._object)
            self._node=self._nodeName_query_str(self._object)
            self._side=self.sideName_query_str(self._object)
            self._hierarchy=self.rangeAlphabet_query_str(self._title)
            name=self._orderName_query_str(self._orders)
            return name

        elif self._switch=="setAuto":
            self._title=self._titleName_query_str(self._object)
            self._hierarchy=self.rangeAlphabet_query_str(self._title)
            name=self._orderName_query_str(self._orders)
            return name

        elif self._switch=="mark":
            _addStringAttrs=self.__getStringAttr()
            self._title=cmds.getAttr(self._object+"."+_addStringAttrs[0]["attrName"])
            self._side=cmds.getAttr(self._object+"."+_addStringAttrs[1]["attrName"])
            self._node=cmds.getAttr(self._object+"."+_addStringAttrs[2]["attrName"])
            self._num=cmds.getAttr(self._object+"."+_addStringAttrs[3]["attrName"])
            self._hierarchy=cmds.getAttr(self._object+"."+_addStringAttrs[4]["attrName"])
            name=self._orderName_query_str(self._orders)
            return name

        elif self._switch=="replace":
            if not self._find == None and not self._replace == None:
                name=self._object
                name.replace(self._find,self._replace)
            else:
                name=self._name
                return name

        else:
            cmds.error("Unknown string in swicth value.")

    def markAttr(self):
        self.__loading()
        if self._switch=="fullAuto" or self._switch=="name":
            self._title=self._titleName_query_str(self._object)
            self._node=self._nodeName_query_str(self._object)
            self._side=self.sideName_query_str(self._object)
        mark=aLB.Attribute()
        mark.setObject(self._object)
        mark.setAttrType("string")
        _addStringAttrs=self.__getStringAttr()
        for _addStringAttr in _addStringAttrs:
            mark.setAttr(_addStringAttr["attrName"])
            mark.setStringName(_addStringAttr["attrString"])
            mark.addAttr()
