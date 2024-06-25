# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds

import cgInTools as cit
from ..library import skinLB as sLB
cit.reloads([sLB])

def main():
    node_strs=cmds.ls(sl=True)
    renameSkc=sLB.AppCopySkinWeight()
    for node_str in node_strs:
        skc_str=renameSkc.geoSkinCluster_query_str(node_str)
        fix_str=renameSkc.clusterRename_create_str(node_str)
        cmds.rename(skc_str,fix_str)