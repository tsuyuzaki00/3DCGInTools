import maya.cmds as cmds

class AppSceneClean():
    def __init__(self):
        self._nodeName_str=None
    
    #Single Function
    @staticmethod
    def unlocks_edit_func(nodeName_str,attrs=["tx","ty","tz","rx","ry","rz","sx","sy","sz","visibility"]):
        for attr in attrs:
            cmds.setAttr(nodeName_str+"."+attr,l=False)

    @staticmethod
    def delUnknownNode_edit_func():
        unknown_nodes=cmds.ls(type="unknown")
        cmds.delete(unknown_nodes)
        unknown_plugins=cmds.unknownPlugin(q=True,l=True)
        if unknown_plugins:
            for unknown_plugin in unknown_plugins:
                cmds.unknownPlugin(unknown_plugin,r=True)
                print("Removed unknown plugin : "+unknown_plugin)

    @staticmethod
    def delGarbageReference_edit_func():
        count=0
        refs=cmds.ls(type="reference")
        for ref in refs:
            try:
                cmds.referenceQuery(ref,f=True)
            except Exception as e:
                if type(e) == RuntimeError and 'is not associated with a reference file' in e.message:
                    print(e+" Deleting: "+ ref)
                    cmds.lockNode(ref,lock=False)
                    cmds.delete(ref)
                    count += 1

        print("Total errors found: " + str(count))

    #Multi Function
    def _delFRHThree_edit_func(self,nodeName_str):
        self.unlocks_edit_func(nodeName_str)#Prevention of unlock errors
        cmds.makeIdentity(nodeName_str,apply=True,t=True,r=True,s=True,pn=True)#Freeze Transformations
        cmds.makeIdentity(nodeName_str,apply=False,t=True,r=True,s=True)#Reset Transformations
        cmds.delete(nodeName_str,ch=True)#Delete by Type History
        cmds.select(cl=True)

    #Setting Function
    def setNodeName(self,variable):
        self._nodeName_str=variable
        return self._nodeName_str
    def getNodeName(self):
        return self._nodeName_str
    
    #Public Function
    def delFRH(self):
        self._delFRHThree_edit_func(self._nodeName_str)

    def delUnknownNode(self):
        self.delUnknownNode_edit_func()

    def delGarbageReference(self):
        self.delGarbageReference_edit_func()