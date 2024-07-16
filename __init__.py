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
    if not os.path.isdir(folder_dir):
        os.makedirs(folder_dir)
    
    file_strs=[file_str for file_str in os.listdir(setting_dir) if "init" in file_str or "execute" in file_str]
    for file_str in file_strs:
        file_path=os.path.join(folder_dir,file_str)
        if not os.path.isfile(file_path):
            setting_path=os.path.join(setting_dir,file_str)
            shutil.copy2(setting_path,file_path)
    return setting_dir,folder_dir

root_dir=os.path.dirname(__file__) #.../cgInTools/
library_dir=os.path.join(root_dir,"library")
ui_dir=os.path.join(root_dir,"ui")

maya_dir=os.path.join(root_dir,"maya")
mayaDefSetProject_dir=os.path.join(maya_dir,"__defSetProject")
mayaLibrary_dir=os.path.join(maya_dir,"library")
mayaSetup_dir=os.path.join(maya_dir,"setup")
mayaData_dir=os.environ.get("MAYACGINTOOLSDATA_DIRECTORY")

mgear_dir=os.path.join(maya_dir,"mgear")
mgearLibrary_dir=os.path.join(mgear_dir,"library")
mgearSetup_dir=os.path.join(mgear_dir,"setup")
mgearData_dir=os.environ.get("MGEARCGINTOOLSDATA_DIRECTORY")

blender_dir=os.path.join(root_dir,"blender")
blenderSettings_dir=os.path.join(blender_dir,"_settings")
blenderLibrary_dir=os.path.join(blender_dir,"library")
blenderSetup_dir=os.path.join(blender_dir,"setup")
blenderData_dir=os.environ.get("BLENDERCGINTOOLSDATA_DIRECTORY")