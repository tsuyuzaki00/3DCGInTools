import cgInTools as cit
from ...library import dataLB as dLB
from . import menuBarLB as mLB
cit.reloads([dLB,mLB])
        
def main(readFile_str="menuBarEX"):
    menu_DataPath=dLB.DataPath()
    menu_DataPath.setAbsoluteDirectory(cit.maya_dir)
    menu_DataPath.setRelativeDirectory("menuBar")
    menu_DataPath.setFile(readFile_str)
    menu_DataPath.setExtension("json")

    menu_DataMenu=mLB.DataMenu()
    menu_DataMenu.setOriginDataPath(menu_DataPath)
    menu_DataMenu.readJson()

    menu_SelfMenu=mLB.SelfMenu()
    menu_SelfMenu.setDataMenu(menu_DataMenu)
    menu_SelfMenu.create()