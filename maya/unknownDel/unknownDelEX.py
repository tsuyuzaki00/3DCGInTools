# -*- coding: iso-8859-15 -*-
import cgInTools as cit
from ..library import sceneCleanLB as cLB
cit.reloads([cLB])

def main():
    delUnknown_AppSceneClean=cLB.AppSceneClean()
    delUnknown_AppSceneClean.delUnknownNode()