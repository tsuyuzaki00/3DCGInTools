# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ...library import dataLB as dLB
from ..library import projectLB as pjLB
#from ..library import selfLB as sLB
from ..library import windowLB as wLB
cit.reloads([dLB,pjLB,wLB])

def main():
    project_dir,project_folder=wLB.mayaDirDialog_query_dir_folder("Edit",upRoot=True)
    if project_dir is None or project_folder is None:
        return

    project_DataPath=dLB.DataPath()
    project_DataPath.setAbsoluteDirectory(project_dir)
    project_DataPath.setRelativeDirectory(project_folder)

    project_SelfProject=pjLB.SelfProject()
    project_SelfProject.setProjectDataPath(project_DataPath)
    project_SelfProject.editProject()