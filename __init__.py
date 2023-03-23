# -*- coding: iso-8859-15 -*-
import os,sys,inspect

def reloads(ps=[]):
    if ps == [] or ps == None:
        return None
    for p in ps:
        if sys.version.startswith("2"):
            reload(p)
        elif sys.version.startswith("3"):
            import importlib
            importlib.reload(p)

def printFunction(function):
    signature=inspect.signature(function)
    args=[]
    for name,value in signature.parameters.items():
        valueType=str(type(value.default))
        args.append(f"{name}={valueType}")
    output=f"{function.__name__}({','.join(args)})"
    print(output)

root_dir=os.path.dirname(__file__) #.../cgInTools/
ui_dir=os.path.join(root_dir,"ui")
menu_dir=os.path.join(root_dir,"_menu")
settings_dir=os.path.join(root_dir,"_settings")
library_dir=os.path.join(root_dir,"library")
execute_dir=os.path.join(root_dir,"execute")

maya_dir=os.path.join(root_dir,"maya")
mayaDefSetProject_dir=os.path.join(maya_dir,"__defSetProject")
mayaSettings_dir=os.path.join(maya_dir,"_settings")
mayaData_dir=os.path.join(maya_dir,"data")
mayaExecute_dir=os.path.join(maya_dir,"execute")
mayaLibrary_dir=os.path.join(maya_dir,"library")
mayaManager_dir=os.path.join(maya_dir,"manager")
mayaOption_dir=os.path.join(maya_dir,"option")
mayaSetup_dir=os.path.join(maya_dir,"setup")

mgear_dir=os.path.join(root_dir,"mgear")
mgearSettings_dir=os.path.join(mgear_dir,"_settings")
mgearData_dir=os.path.join(mgear_dir,"data")
mgearExecute_dir=os.path.join(mgear_dir,"execute")
mgearLibrary_dir=os.path.join(mgear_dir,"library")
mgearManager_dir=os.path.join(mgear_dir,"manager")
