import cgInTools as cit
from ..library import pluginLB as pLB
cit.reloads([pLB])

def main():
    pLB.loadedOnOff_edit_func(pluginName_str="3DxMaya.mll")