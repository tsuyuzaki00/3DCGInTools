# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import cgInTools as cit
#from cgInTools.maya.manager import paintWeightValueMN as MN
from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.library import fkikLB as LB
#from cgInTools.maya.execute import infJntRemoveEditEX as EX
cit.reloads([OP])

def main():
    OP.main()
    #MN.main()
    #EX.main()
    """
    fkik=LB.FKIK()
    fkik.setSourceNode("joint1")
    fkik.setTargetNode("joint3")
    fkik.setThirdNode("joint2")
    fkik.setUI("UIsan")
    fkik.createThreeJoints()
    replace=LB.Constrain()
    replace.setSourceNode(sourceNode)
    replace.setTargetNode(targetNode)
    replace.proximityPin()
    """

main()