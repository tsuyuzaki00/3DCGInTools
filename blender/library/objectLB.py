import bpy
import math
import bmesh

class SelfEditArmature(object):
    def __init__(self):
        self._armature_str=None
        self._bone_str=None
        self._head_list=None
        self._tail_list=None
        self._roll_float=None
        self._initChoices=[
            "armature_str",
            "bone_str",
            "head_list",
            "tail_list",
            "roll_float"
        ]

    def selectEditBone_query_EditBone(self,armatureName,boneName):
        armature_Object=bpy.data.objects[armatureName]
        bpy.context.view_layer.objects.active=armature_Object
        bpy.ops.object.mode_set(mode='EDIT')
        bone_EditBone=armature_Object.data.edit_bones[boneName]
        return bone_EditBone

    def headPos_edit_func(self,bone_EditBone,vector):
        for i in range(3):
            bone_EditBone.head[i]=vector[i]

    def headPos_query_list(self,bone_EditBone):
        head_list=[bone_EditBone.head[i] for i in range(3)]
        return head_list
    
    def tailPos_edit_func(self,bone_EditBone,vector):
        for i in range(3):
            bone_EditBone.tail[i]=vector[i]
    
    def tailPos_query_list(self,bone_EditBone):
        tail_list=[bone_EditBone.tail[i] for i in range(3)]
        return tail_list
    
    def roll_edit_func(self,bone_EditBone,value):
        bone_EditBone.roll=value

    def roll_query_float(self,bone_EditBone):
        roll_float=bone_EditBone.roll
        return roll_float

    #Setting Function
    def setInitChoice(self,variable):
        self._initChoices=variable
        return self._initChoices
    def getInitChoice(self):
        return self._initChoices

    def setArmature(self,variable):
        self._armature_str=variable
        return self._armature_str
    def getArmature(self):
        return self._armature_str
    
    def setBone(self,variable):
        self._bone_str=variable
        return self._bone_str
    def getBone(self):
        return self._bone_str
    
    def setHead(self,variable):
        self._head_list=variable
        return self._head_list
    def currentHead(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._head_list=self.headPos_query_list(bone_EditBone)
        return self._head_list
    def getHead(self):
        return self._head_list
    
    def setTail(self,variable):
        self._tail_list=variable
        return self._tail_list
    def currentTail(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._tail_list=self.tailPos_query_list(bone_EditBone)
        return self._tail_list
    def getTail(self):
        return self._tail_list
    
    def setRoll(self,variable):
        self._roll_float=variable
        return self._roll_float
    def currentRoll(self):
        bone_EditBone=self.selectEditBone_query_EditBone(self._armature_str,self._bone_str)
        self._roll_float=self.roll_query_float(bone_EditBone)
        return self._roll_float
    def getRoll(self):
        return self._roll_float

    #Public Function
    def writeDict(self,initChoices=None):
        _initChoices=initChoices or self._initChoices
        write_dict={}
        for _initChoice in _initChoices:
            variable=getattr(self,"_"+_initChoice)
            write_dict[_initChoice]=variable
        return write_dict

    def readDict(self,read_dict,initChoices=None):
        _initChoices=initChoices or self._initChoices
        for _initChoice in _initChoices:
            setattr(self,"_"+_initChoice,read_dict[_initChoice])

    def writeDict(self):
        write_dict={
            "armature_str":self._armature_str,
            "bone_str":self._bone_str,
            "head_list":self._head_list,
            "tail_list":self._tail_list,
            "roll_float":self._roll_float
        }
        return write_dict

    def readDict(self,read_dict):
        self._armature_str=read_dict["armature_str"]
        self._bone_str=read_dict["bone_str"]
        self._head_list=read_dict["head_list"]
        self._tail_list=read_dict["tail_list"]
        self._roll_float=read_dict["roll_float"]

    def editHead(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _head_list=vector or self._head_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.headPos_edit_func(bone_EditBone,_head_list)
    
    def editTail(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _tail_list=vector or self._tail_list
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.tailPos_edit_func(bone_EditBone,_tail_list)

    def editRoll(self,value=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _roll_float=value or self._roll_float
        bone_EditBone=self.selectEditBone_query_EditBone(_armature_str,_bone_str)
        self.roll_edit_func(bone_EditBone,_roll_float)
class SelfPoseArmature(object):
    def __init__(self):
        self._armature_str=None
        self._bone_str=None
        self._property_str=None
        self._translation_list=None
        self._rotation_list=None
        self._scale_list=None
        self._translationShape_list=None
        self._scaleShape_list=None
        self._ikfkShape_list=None
        self._curveIn_list=None
        self._curveOut_list=None
        self._customObject_str=None
        self._initChoices=[
            "armature_str",
            "bone_str",
            "property_str",
            "translation_list",
            "rotation_list",
            "scale_list",
            "translationShape_list",
            "scaleShape_list",
            "ikfkShape_list",
            "curveIn_list",
            "curveOut_list"
        ]

    #Single Function
    def selectPoseBone_query_PoseBone(self,armatureName,boneName):
        armature_Object=bpy.data.objects[armatureName]
        bpy.context.view_layer.objects.active=armature_Object
        bpy.ops.object.mode_set(mode='POSE')

        bone_PoseBone=armature_Object.pose.bones[boneName]
        return bone_PoseBone

    def translation_edit_func(self,bone_PoseBone,translation):
        bone_PoseBone.location=translation
    
    def translation_query_list(self,bone_PoseBone):
        translation_vector=bone_PoseBone.location
        translation_list=[translation_vector[0],translation_vector[1],translation_vector[2]]
        return translation_list
    
    def rotation_edit_func(self,bone_PoseBone,rotation):
        for i in range(len(rotation)):
            bone_PoseBone.rotation_euler[i]=math.radians(rotation[i])
    
    def rotation_query_list(self,bone_PoseBone):
        rotation_vector=bone_PoseBone.rotation_euler
        rotation_list=[math.degrees(math.pi/rotation_vector[i]) for i in range(len(rotation))]
        return rotation_list

    def scale_edit_func(self,bone_PoseBone,scale):
        bone_PoseBone.scale=scale
    
    def scale_query_list(self,bone_PoseBone):
        scale_vector=bone_PoseBone.scale
        scale_list=[scale_vector[0],scale_vector[1],scale_vector[2]]
        return scale_list

    def customShapeTranslation_edit_func(self,bone_PoseBone,translation):
        bone_PoseBone.custom_shape_translation=translation
    
    def customShapeTranslation_query_list(self,bone_PoseBone):
        translation_vector=bone_PoseBone.custom_shape_translation
        translation_list=[translation_vector[0],translation_vector[1],translation_vector[2]]
        return translation_list
    
    def customShapeScale_edit_func(self,bone_PoseBone,scale):
        bone_PoseBone.custom_shape_scale_xyz=scale
    
    def customShapeScale_query_list(self,bone_PoseBone):
        scale_vector=bone_PoseBone.custom_shape_scale_xyz
        scale_list=[scale_vector[0],scale_vector[1],scale_vector[2]]
        return scale_list

    def IKFKShape_edit_func(self,bone_PoseBone,property_str,param):
        for i in range(len(param)):
            bone_PoseBone[property_str][i]=param[i]

    def IKFKShape_query_list(self,bone_PoseBone,property_str):
        IKFKShape_list=[bone_PoseBone[property_str][i] for i in range(len(bone_PoseBone[property_str]))]
        return IKFKShape_list

    def bendyBone_edit_func(self,bone_PoseBone,curveIn,curveOut):
        #curveIn=(x,z),curveOut=(x,z)    
        bone_PoseBone.bbone_curveinx=curveIn[0]
        bone_PoseBone.bbone_curveinz=curveIn[1]
        bone_PoseBone.bbone_curveoutx=curveOut[0]
        bone_PoseBone.bbone_curveoutz=curveOut[1]
    
    def bendyBone_query_list_list(self,bone_PoseBone):
        #curveIn=(x,z),curveOut=(x,z)
        curveIn_list=[bone_PoseBone.bbone_curveinx,bone_PoseBone.bbone_curveinz]
        curveOut_list=[bone_PoseBone.bbone_curveoutx,bone_PoseBone.bbone_curveoutz]
        return curveIn_list,curveOut_list

    #Setting Function
    def setInitChoice(self,variable):
        self._initChoices=variable
        return self._initChoices
    def getInitChoice(self):
        return self._initChoices

    def setArmature(self,variable):
        self._armature_str=variable
        return self._armature_str
    def getArmature(self):
        return self._armature_str
    
    def setBone(self,variable):
        self._bone_str=variable
        return self._bone_str
    def getBone(self):
        return self._bone_str
    
    def setProperty(self,variable):
        self._property_str=variable
        return self._property_str
    def getProperty(self):
        return self._property_str
    
    def setTranslation(self,variable):
        self._translation_list=variable
        return self._translation_list
    def currentTranslation(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._translation_list=self.translation_query_list(bone_PoseBone)
        return self._translation_list
    def getTranslation(self):
        return self._translation_list
    
    def setRotation(self,variable):
        self._rotation_list=variable
        return self._rotation_list
    def currentRotation(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._rotation_list=self.rotation_query_list(bone_PoseBone)
        return self._rotation_list
    def getRotation(self):
        return self._rotation_list
    
    def setScale(self,variable):
        self._scale_list=variable
        return self._scale_list
    def currentScale(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._scale_list=self.scale_query_list(bone_PoseBone)
        return self._scale_list
    def getScale(self):
        return self._scale_list

    def setShapeTranslation(self,variable):
        self._translationShape_list=variable
        return self._translationShape_list
    def currentShapeTranslation(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._translationShape_list=self.customShapeTranslation_query_list(bone_PoseBone)
        return self._translationShape_list
    def getShapeTranslation(self):
        return self._translationShape_list
    
    def setShapeScale(self,variable):
        self._scaleShape_list=variable
        return self._scaleShape_list
    def currentShapeScale(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._scaleShape_list=self.customShapeScale_query_list(bone_PoseBone)
        return self._scaleShape_list
    def getShapeScale(self):
        return self._scaleShape_list
    
    def setIKFKShape(self,variable):
        self._ikfkShape_list=variable
        return self._ikfkShape_list
    def currentIKFKShape(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._ikfkShape_list=self.IKFKShape_query_list(bone_PoseBone,self._property_str)
        return self._ikfkShape_list
    def getIKFKShape(self):
        return self._ikfkShape_list
    
    def setCurveIn(self,variable):
        self._curveIn_list=variable
        return self._curveIn_list
    def currentCurveIn(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._curveIn_list=self.bendyBone_query_list_list(bone_PoseBone)[0]
        return self._curveIn_list
    def getCurveIn(self):
        return self._curveIn_list
    
    def setCurveOut(self,variable):
        self._curveOut_list=variable
        return self._curveOut_list
    def currentCurveOut(self):
        bone_PoseBone=self.selectPoseBone_query_PoseBone(self._armature_str,self._bone_str)
        self._curveOut_list=self.bendyBone_query_list_list(bone_PoseBone)[1]
        return self._curveOut_list
    def getCurveOut(self):
        return self._curveOut_list

    #Public Function
    def writeDict(self,initChoices=None):
        _initChoices=initChoices or self._initChoices
        write_dict={}
        for _initChoice in _initChoices:
            variable=getattr(self,"_"+_initChoice)
            write_dict[_initChoice]=variable
        return write_dict

    def readDict(self,read_dict,initChoices=None):
        _initChoices=initChoices or self._initChoices
        for _initChoice in _initChoices:
            setattr(self,"_"+_initChoice,read_dict[_initChoice])

    def editTranslation(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _translation_list=vector or self._translation_list
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.translation_edit_func(bone_PoseBone,_translation_list)
    
    def editRotation(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _rotation_list=vector or self._rotation_list
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.rotation_edit_func(bone_PoseBone,_rotation_list)
    
    def editScale(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _scale_list=vector or self._scale_list
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.scale_edit_func(bone_PoseBone,_scale_list)
    
    def editCustomShapeTranslation(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _translationShape_list=vector or self._translationShape_list
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.customShapeTranslation_edit_func(bone_PoseBone,_translationShape_list)
    
    def editCustomShapeScale(self,vector=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _scaleShape_list=vector or self._scaleShape_list
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.customShapeScale_edit_func(bone_PoseBone,_scaleShape_list)

    def editIKFKShape(self,param=None,property_str=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _ikfkShape_list=param or self._ikfkShape_list
        _property_str=property_str or self._property_str
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.IKFKShape_edit_func(bone_PoseBone,_property_str,_ikfkShape_list)

    def editBendyBone(self,curveIn=None,curveOut=None,boneName=None,armatureName=None):
        _armature_str=armatureName or self._armature_str
        _bone_str=boneName or self._bone_str
        _curveIn_list=curveIn or self._curveIn_list
        _curveOut_list=curveOut or self._curveOut_list
        bone_PoseBone=self.selectPoseBone_query_PoseBone(_armature_str,_bone_str)
        self.bendyBone_edit_func(bone_PoseBone,_curveIn_list,_curveOut_list)
