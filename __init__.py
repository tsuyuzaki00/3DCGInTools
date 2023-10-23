# -*- coding: iso-8859-15 -*-
import os,sys,shutil

def reloads(ps=[]):
    if ps == [] or ps == None:
        return None
    for p in ps:
        if sys.version.startswith("2"):
            reload(p)
        elif sys.version.startswith("3"):
            import importlib
            importlib.reload(p)

def checkScriptsData(folderName_str,setting_dir,cgInToolsData_dir):
    setting_dir=os.path.join(setting_dir,folderName_str)
    folder_dir=os.path.join(cgInToolsData_dir,folderName_str)
    
    file_strs=[file_str for file_str in os.listdir(setting_dir) if "init" in file_str]

    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)

    file_path=os.path.join(folder_dir,file_strs[0])
    setting_path=os.path.join(setting_dir,file_strs[0])
    
    if not os.path.isfile(file_path):
        shutil.copy2(setting_path,file_path)
    return setting_path,file_path

root_dir=os.path.dirname(__file__) #.../cgInTools/
ui_dir=os.path.join(root_dir,"ui")
settings_dir=os.path.join(root_dir,"_settings")
library_dir=os.path.join(root_dir,"library")
execute_dir=os.path.join(root_dir,"execute")

maya_dir=os.path.join(root_dir,"maya")
mayaDefSetProject_dir=os.path.join(maya_dir,"__defSetProject")
mayaSettings_dir=os.path.join(maya_dir,"_settings")
mayaExecute_dir=os.path.join(maya_dir,"execute")
mayaLibrary_dir=os.path.join(maya_dir,"library")
mayaManager_dir=os.path.join(maya_dir,"manager")
mayaOption_dir=os.path.join(maya_dir,"option")
mayaSetup_dir=os.path.join(maya_dir,"setup")

mgear_dir=os.path.join(maya_dir,"mgear")
mgearSettings_dir=os.path.join(mgear_dir,"_settings")
mgearExecute_dir=os.path.join(mgear_dir,"execute")
mgearLibrary_dir=os.path.join(mgear_dir,"library")
mgearManager_dir=os.path.join(mgear_dir,"manager")
mgearOption_dir=os.path.join(mgear_dir,"option")
mgearSetup_dir=os.path.join(mgear_dir,"setup")

blender_dir=os.path.join(root_dir,"blender")
blenderSettings_dir=os.path.join(blender_dir,"_settings")
blenderExecute_dir=os.path.join(blender_dir,"execute")
blenderLibrary_dir=os.path.join(blender_dir,"library")
blenderManager_dir=os.path.join(blender_dir,"manager")
blenderOption_dir=os.path.join(blender_dir,"option")
blenderSetup_dir=os.path.join(blender_dir,"setup")