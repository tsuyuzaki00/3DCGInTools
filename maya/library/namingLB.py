# -*- coding: iso-8859-15 -*-
import itertools
import maya.cmds as cmds

import cgInTools as cit
from . import setBaseLB as sbLB
from . import jsonLB as jLB
from . import attributeLB as aLB
cit.verReload(aLB)

class Naming(sbLB.SetName):
    def __init__(self):
        self._object=""
        self._name=""
        self._title=""
        self._node=""
        self._side=""
        self._hierarchy="A"
        self._replace=None #(beforeName,aftarName)
        self._number=00
        self._num=str(self._number).zfill(2)
        # fullAuto setAuto mark name
        self._switch="fullAuto"
        # title node side num titleNum nodeNum sideNum titleHie scene
        self._orders=["title","node","side","num"]

    def loading(self):
        self._titleNum=self._title+self.rangeNumber_query_str(self._title)
        self._nodeNum=self._node+self.rangeNumber_query_str(self._node)
        self._sideNum=self._side+self.rangeNumber_query_str(self._side)
        self._titleHie=self._title+self.rangeAlphabet_query_str(self._title)
        print(self._titleHie)
        self._scene=self.scene_query_str()
        self._num=self.replaceNumber(self._orders)

    def __getStringAttr(self):
        addStringAttrs=[
            {"attrName":"titleName","attrString":self._title},
            {"attrName":"nodeName","attrString":self._node},
            {"attrName":"sideName","attrString":self._side},
            {"attrName":"numberName","attrString":self._num},
            {"attrName":"hierarchyName","attrString":self._hierarchy},
        ]
        return addStringAttrs

#Public function
    def setOrders(self,variable):
        self._orders=variable
        return self._orders
    def getOrders(self):
        return self._orders

    def setSwitch(self,variable):
        self._switch=variable
        return self._switch
    def getSwitch(self):
        return self._switch

    def titleName(self,obj):
        splitObjs=obj.split("_")
        self.nodeName_query_str(obj)
        self.sideName_query_str(obj)

        for l in range(len(splitObjs)):
            if not splitObjs[l].isdigit():
                name=self.smashNumbers_edit_str(splitObjs[l])
                if not name==self.nodeName_query_str(obj) and\
                   not name==self.sideName_query_str(obj) and\
                   not name==None:
                    return name

    def replaceNumber(self,orders):
        if "num" in orders:
            index=orders.index("num")
            orderName=self.orderName(orders)
            for num in range(100):
                splitNum=orderName.split("_")[index]
                replaceName=orderName.replace(splitNum,str(num).zfill(2))
                if not cmds.objExists(replaceName):
                    return str(num).zfill(2)
        else:
            return str(0).zfill(2)

    def orderName(self,orders):
        order_list=[]
        nullDel_list=[order for order in orders if order != ""]
        for chengeSelf in nullDel_list:
            add=eval("self._"+chengeSelf)
            order_list.append(add)
        self._orderName = "_".join(order_list)
        return self._orderName

    def rename(self):
        if self._switch=="fullAuto":
            self._title=self.titleName(self._object)
            self._node=self.nodeName_query_str(self._object)
            self._side=self.sideName_query_str(self._object)
            self.loading()
            name=self.orderName(self._orders)

        elif self._switch=="setAuto":
            self.loading()
            name=self.orderName(self._orders)

        elif self._switch=="mark":
            _addStringAttrs=self.__getStringAttr()
            self._title=cmds.getAttr(self._object+"."+_addStringAttrs[0]["attrName"])
            self._side=cmds.getAttr(self._object+"."+_addStringAttrs[1]["attrName"])
            self._node=cmds.getAttr(self._object+"."+_addStringAttrs[2]["attrName"])
            self._num=cmds.getAttr(self._object+"."+_addStringAttrs[3]["attrName"])
            self._hierarchy=cmds.getAttr(self._object+"."+_addStringAttrs[4]["attrName"])
            self.loading()
            name=self.orderName(self._orders)

        elif self._switch=="name":
            if type(self._replace) is tuple:
                name=self._object
                name.replace(self._replace[0],self._replace[1])
            else:
                name=self._name

        else:
            cmds.error("Unknown string in swicth value.")

        rename=cmds.rename(self._object,name)
        return rename

    def markAttr(self):
        self.loading()
        if self._switch=="fullAuto":
            self.__autoNameSetting(self._object)
        mark=aLB.Attribute()
        mark.setObject(self._object)
        mark.setAttrType("string")
        _addStringAttrs=self.__getStringAttr()
        for _addStringAttr in _addStringAttrs:
            mark.setAttr(_addStringAttr["attrName"])
            mark.setStringName(_addStringAttr["attrString"])
            mark.addAttr()

#Private function
    def nodeName_query_str(self,obj):
        nodeType=jLB.Json()
        nodeType.setPath(cit.mayaSettings_path)
        nodeType.setFile("autoRename")
        nodeType.setExtension("json")
        nodeType_dict=nodeType.read()
        getNode_str=self.isNodeType_query_str(obj)
        nodeName_str=nodeType_dict["node_renames"][getNode_str]
        return nodeName_str

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

    def sideName_query_str(self,obj,about=1):
        trsX=cmds.xform(obj,q=True,ws=True,t=True)[0]
        if trsX>about:
            return "L"
        elif trsX<about*-1:
            return "R"
        else:
            return "C"

    def smashNumbers_edit_str(self,name):
        while name[-1].isdigit():
            name=name[:-1]
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
            if not cmds.objExists("*"+name+str(i).zfill(2)+"*"):
                return str(i).zfill(2)

    def rangeAlphabet_query_str(self,name):
        for i in range(65, 91):
            if i is None:
                cmds.error("Can't go over Z.")
            if name[-1].isupper():
                name=name[:-1]
            if not cmds.objExists("*"+name+chr(i)+"*"):
                return chr(i)

    def scene_query_str(self):
        sceneName=cmds.file(q=True,sn=True).split("/")[-1]
        sceneName=sceneName.split(".")[0]
        sceneParent=cmds.workspace(q=True,sn=True).split("/")[-1]
        if sceneName == "":
            self.scene=sceneParent
        else:
            self.scene=sceneName
        return self.scene
