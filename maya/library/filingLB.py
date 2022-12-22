# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import os
import shutil

import cgInTools as cit
from . import setBaseLB as sbLB
from . import cleanLB as cLB
from . import checkLB as chLB
from . import jsonLB as jLB
cit.reloads([sbLB,cLB,chLB,jLB])

RULE_DICT=jLB.getJson(cit.mayaSettings_dir,"library")
PROJECTFOLDER=cit.mayaDefSetProject_dir

class Path(sbLB.BasePath):
    def __init__(self):
        super(Path,self).__init__()
        scene=cmds.file(q=True,sceneName=True).split("/")[-1]
        self._file=scene.split(".")[0]
        self._extension=scene.split(".")[1]

    def __loading(self):
        self._path=os.path.normpath(self._path)

    #Public Function
    def clean(self):
        self.__loading()

    def getSplitPathOfIndex(self):
        norm_path=os.path.normpath(self._path)
        split_str=norm_path.split("\\")[self._index]
        return split_str

    def getSplitNameOfIndex(self):
        split_str=self._name.split(self._split)[self._index]
        return split_str

class Project(sbLB.BasePath):
    def __init__(self):
        super(Project,self).__init__()
        self.defSetProjectFolder=PROJECTFOLDER
        self._workPath=cmds.workspace(q=True,rd=True,o=True)
        self._defPath=os.path.abspath(os.path.join(self._workPath,".."))
        self._projectPathName="_newProject"

    def __loading(self):
        self._workPath=cmds.workspace(q=True,rd=True)
        self._defPath=os.path.abspath(os.path.join(self._workPath,".."))

    #Single Function
    def isPath_check_str(self,path):
        boolean=os.path.isdir(path)
        if boolean:
            return path
        else :
            cmds.error(path+" path does not exist.")

    def notSamePath_check_str(self,path):
        boolean=os.path.isdir(path)
        if boolean:
            cmds.error(path+" folder with the same name already exists")
        else :
            return path

    def setProject_edit_str(self,path,name):
        workPath=os.path.join(path,name)
        cmds.workspace(workPath,o=True)
        workPath=cmds.workspace(q=True,rd=True)
        return workPath

    #Multi Function
    def _isPathAndSamePath_check_func(self,path,name):
        checkPath=os.path.join(path,name)
        self.isPath_check_str(checkPath)
        self.notSamePath_check_str(checkPath)

    #Private Function
    def _setProject_create_str(self,path,name):
        workPath=os.path.join(path,name)
        shutil.copytree(self.defSetProjectFolder,workPath)
        cmds.workspace(workPath,o=True)
        workPath=cmds.workspace(q=True,rd=True)
        return workPath

    #Public Function
    def queryInDefPath(self,variable):
        inDefPath=os.path.abspath(os.path.join(self._defPath,variable))
        return inDefPath

    def createProject(self):
        self._isPathAndSamePath_check_func(self._path,self._projectName)
        self._workPath=self._setProject_create_str(self._path,self._projectName)
        return self._workPath

    def editProject(self):
        self._isPathAndSamePath_check_func(self._path,self._projectName)
        self._workPath=self.setProject_edit_str(self._path,self._projectName)
        return self._workPath

    def createInProject(self):
        self.__loading()
        self._isPathAndSamePath_check_func(self._defPath,self._projectName)
        self._workPath=self._setProject_create_str(self._defPath,self._projectName)
        return self._workPath

    def editInProject(self):
        self.__loading()
        self._isPathAndSamePath_check_func(self._defPath,self._projectName)
        self._workPath=self.setProject_edit_str(self._defPath,self._projectName)
        return self._workPath
 
class File(sbLB.BaseFile):
    def __init__(self):
        self._fileType_dict=RULE_DICT["fileType_dict"]
        workPath=cmds.workspace(q=True,sn=True)
        self._path=workPath
        self._file=work_path.split("/")[-1]

    #Single Function
    def fileSave_edit_func(self,file,exType="mayaAscii"):
        currentScenePath=cmds.file(q=True,sn=True)
        root=os.path.dirname(currentScenePath)
        if root == "":
            cmds.file(rename=file)
        cmds.file(save=True,op="v=0",type=exType)

    def exportMAMB_create_func(self,objs,path,file,ex="ma",exType="mayaAscii"):
        cmds.select(objs)
        fullPath=os.path.join(path,file+"."+ex)
        cmds.file(fullPath,f=True,options="v=0;",typ=exType,pr=True,es=True)
    
    def exportOBJFBX_create_func(self,objs,path,file,ex="obj",exType="OBJexport"):
        cmds.select(objs)
        fullPath=os.path.join(path,file+"."+ex)
        cmds.file(fullPath,f=True,options="v=0;",groups=1,ptgroups=1,materials=1,smoothing=1,normals=1,typ=exType,pr=True,es=True)
    
    def grpsDuplicate_create_list(self,grps):
        exportGrps=[]
        for grp in grps:
            cmds.rename(grp,grp+"_original")
            cmds.duplicate(grp+"_original")
            exportGrp=cmds.rename(grp+"_original1",grp)
            exportGrps.append(exportGrp)
            return exportGrps

    def undoDuplicate_edit_func(self,grps,delGrps):
        cmds.delete(delGrps)
        for grp in grps:
            cmds.rename(grp+"_original",grp)

    #Multi Function
    def _judgeFileType_create_func(objs,path,file,extension,fileType_dict):
        fileType=fileType_dict[extension]
        if extension is "ma" or extension is "mb":
            self.exportMAMB_create_func(objs,path,file,extension,fileType)
        elif extension is "obj" or extension is "fbx":
            self.exportOBJFBX_create_func(objs,path,file,extension,fileType)

    #Public Function
    def addPath(self,variable):
        addPath=os.path.abspath(os.path.join(self._path,variable))
        return addPath

    def save(self):
        self.fileSave_edit_func(self._file,self._fileType[1])

    def exportFile(self):
        self._judgeFileType_create_func(self._objs,self._path,self._file,self._extension,self._fileType_dict)

    def grpsExport(self):
        uncleanObjs=[]
        dupGrps=self.grpsDuplicate_create_list(self._objs)
        for dupGrp in dupGrps:
            uncleans=cmds.listRelatives(dupGrp,c=True,f=True)
            uncleanObjs=uncleanObjs+uncleans
        cLB.delFRHThree_edit_func(uncleanObjs)
        cLB.defaultMaterial_edit_func(uncleanObjs)
        self._judgeFileType_create_func(self._objs,self._path,self._file,self._extension,self._fileType_dict)
        self.undoDuplicate_edit_func(self._objs,dupGrps)