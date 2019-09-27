import maya.cmds as cmds

class SetupIK:
    global R_hipLoc
    global R_kneeLoc
    global R_ankleLoc
    global R_footLoc
    global R_toesLoc

    global L_hipLoc
    global L_kneeLoc
    global L_ankleLoc
    global L_footLoc
    global L_toesLoc

    global C_hipLoc

    global R_shoulderLoc
    global R_elbowLoc
    global R_wristLoc
    global R_handLoc
    global R_thumb1
    global R_thumb2
    global R_thumb3
    global R_index1
    global R_index2
    global R_index3
    global R_index4
    global R_middle1
    global R_middle2
    global R_middle3
    global R_middle4
    global R_ring1
    global R_ring2
    global R_ring3
    global R_ring4
    global R_small1
    global R_small2
    global R_small3
    global R_small4

    global R_clavicle

    global L_shoulderLoc
    global L_elbowLoc
    global L_wristLoc
    global L_handLoc
    global L_thumb1
    global L_thumb2
    global L_thumb3
    global L_index1
    global L_index2
    global L_index3
    global L_index4
    global L_middle1
    global L_middle2
    global L_middle3
    global L_middle4
    global L_ring1
    global L_ring2
    global L_ring3
    global L_ring4
    global L_small1
    global L_small2
    global L_small3
    global L_small4

    global L_clavicle

    global lowerBack
    global back
    global neck
    global head
    global headTop
  
    def __init__(self):
        if(cmds.window("rIKRig", exists=True)):
            cmds.deleteUI("rIKRig")

        self.win = cmds.window("rIKRig", title="IK Rig", widthHeight=(300,1000))
        cmds.columnLayout()

        cmds.iconTextButton(style="textOnly", label="(Adjust the locators according to your character)")
        cmds.button(label="Make Locators", command=self.makeLocators, width=300)        
        cmds.button(label="Setup Bones/Joints", command=self.setupJoints, width=300)

        cmds.separator(style="double", height=5)

        self.rbgAim = cmds.radioButtonGrp(label="Aim Axis:", numberOfRadioButtons=3, labelArray3=("X","Y","Z"), select=2, columnWidth4=(80,40,40,40))
        self.cbRevAim = cmds.checkBox(label="Reverse Aim", value=False)
        self.rbgUp = cmds.radioButtonGrp(label="Up Axis:", numberOfRadioButtons=3, labelArray3=("X","Y","Z"), select=1, columnWidth4=(80,40,40,40))
        self.cbRevUp=cmds.checkBox(label="Reverse Up", value=False)

        cmds.separator(style="double", height=5)

        self.ffgUpDir = cmds.floatFieldGrp(numberOfFields=3, label="World Up Dir:", value1=1.0, value2=0.0, value3=0.0, columnWidth4=(80,50,50,50))

        cmds.iconTextButton(style="textOnly", label="(Select the joints that you want to orient)")
        cmds.button(label="Orient", command=self.orientJointsUI, width=300)        

        cmds.button(label="Setup IK", command=self.setupIK, width=300)

        cmds.iconTextButton(style="textOnly", label="(Select the character GEO to also bind the skin)")
        cmds.button(label="Bind Skin", command=self.bindSkin, width=300)        

        cmds.button(label="Create Controls", command=self.createControls, width=300)

        cmds.button(label="Select all Joints", command=self.selectJoints)

        cmds.button(label="Obtain all variables (not working)", command=self.obtainAllVariables)

        cmds.showWindow(self.win)

    def makeLocators(self, *args):  
        global R_hipLoc
        global R_kneeLoc
        global R_ankleLoc
        global R_footLoc
        global R_toesLoc

        global L_hipLoc
        global L_kneeLoc
        global L_ankleLoc
        global L_footLoc
        global L_toesLoc

        global C_hipLoc

        global R_shoulderLoc
        global R_elbowLoc
        global R_wristLoc
        global R_handLoc
        global R_thumb1
        global R_thumb2
        global R_thumb3
        global R_index1
        global R_index2
        global R_index3
        global R_index4
        global R_middle1
        global R_middle2
        global R_middle3
        global R_middle4
        global R_ring1
        global R_ring2
        global R_ring3
        global R_ring4
        global R_small1
        global R_small2
        global R_small3
        global R_small4

        global R_clavicle

        global L_shoulderLoc
        global L_elbowLoc
        global L_wristLoc
        global L_handLoc
        global L_thumb1
        global L_thumb2
        global L_thumb3
        global L_index1
        global L_index2
        global L_index3
        global L_index4
        global L_middle1
        global L_middle2
        global L_middle3
        global L_middle4
        global L_ring1
        global L_ring2
        global L_ring3
        global L_ring4
        global L_small1
        global L_small2
        global L_small3
        global L_small4

        global L_clavicle

        global lowerBack
        global back
        global neck
        global head
        global headTop

        #create the name and type of global objects
        R_hipLoc = cmds.spaceLocator(name="R_hipLoc")
        R_kneeLoc = cmds.spaceLocator(name="R_kneeLoc")
        R_ankleLoc = cmds.spaceLocator(name="R_ankleLoc")
        R_footLoc = cmds.spaceLocator(name="R_footLoc")
        R_toesLoc = cmds.spaceLocator(name="R_toesLoc")

        L_hipLoc = cmds.spaceLocator(name="L_hipLoc")
        L_kneeLoc = cmds.spaceLocator(name="L_kneeLoc")
        L_ankleLoc = cmds.spaceLocator(name="L_ankleLoc")
        L_footLoc = cmds.spaceLocator(name="L_footLoc")
        L_toesLoc = cmds.spaceLocator(name="L_toesLoc")

        C_hipLoc = cmds.spaceLocator(name="C_hipLoc")

        R_shoulderLoc = cmds.spaceLocator(name="R_shoulderLoc")
        R_elbowLoc = cmds.spaceLocator(name="R_elbowLoc")
        R_wristLoc = cmds.spaceLocator(name="R_wristLoc")
        R_handLoc = cmds.spaceLocator(name="R_handLoc")
        R_thumb1 = cmds.spaceLocator(name="R_thumb1")
        R_thumb2 = cmds.spaceLocator(name="R_thumb2")
        R_thumb3 = cmds.spaceLocator(name="R_thumb3")
        R_index1 = cmds.spaceLocator(name="R_index1")
        R_index2 = cmds.spaceLocator(name="R_index2")
        R_index3 = cmds.spaceLocator(name="R_index3")
        R_index4 = cmds.spaceLocator(name="R_index4")
        R_middle1 = cmds.spaceLocator(name="R_middle1")
        R_middle2 = cmds.spaceLocator(name="R_middle2")
        R_middle3 = cmds.spaceLocator(name="R_middle3")
        R_middle4 = cmds.spaceLocator(name="R_middle4")
        R_ring1 = cmds.spaceLocator(name="R_ring1")
        R_ring2 = cmds.spaceLocator(name="R_ring2")
        R_ring3 = cmds.spaceLocator(name="R_ring3")
        R_ring4 = cmds.spaceLocator(name="R_ring4")
        R_small1 = cmds.spaceLocator(name="R_small1")
        R_small2 = cmds.spaceLocator(name="R_small2")
        R_small3 = cmds.spaceLocator(name="R_small3")
        R_small4 = cmds.spaceLocator(name="R_small4")

        R_clavicle = cmds.spaceLocator(name="R_clavicle")

        L_shoulderLoc = cmds.spaceLocator(name="L_shoulderLoc")
        L_elbowLoc = cmds.spaceLocator(name="L_elbowLoc")
        L_wristLoc = cmds.spaceLocator(name="L_wristLoc")
        L_handLoc = cmds.spaceLocator(name="L_handLoc")
        L_thumb1 = cmds.spaceLocator(name="L_thumb1")
        L_thumb2 = cmds.spaceLocator(name="L_thumb2")
        L_thumb3 = cmds.spaceLocator(name="L_thumb3")
        L_index1 = cmds.spaceLocator(name="L_index1")
        L_index2 = cmds.spaceLocator(name="L_index2")
        L_index3 = cmds.spaceLocator(name="L_index3")
        L_index4 = cmds.spaceLocator(name="L_index4")
        L_middle1 = cmds.spaceLocator(name="L_middle1")
        L_middle2 = cmds.spaceLocator(name="L_middle2")
        L_middle3 = cmds.spaceLocator(name="L_middle3")
        L_middle4 = cmds.spaceLocator(name="L_middle4")
        L_ring1 = cmds.spaceLocator(name="L_ring1")
        L_ring2 = cmds.spaceLocator(name="L_ring2")
        L_ring3 = cmds.spaceLocator(name="L_ring3")
        L_ring4 = cmds.spaceLocator(name="L_ring4")
        L_small1 = cmds.spaceLocator(name="L_small1")
        L_small2 = cmds.spaceLocator(name="L_small2")
        L_small3 = cmds.spaceLocator(name="L_small3")
        L_small4 = cmds.spaceLocator(name="L_small4")

        L_clavicle = cmds.spaceLocator(name="L_clavicle")

        lowerBack = cmds.spaceLocator(name="lowerBack")
        back = cmds.spaceLocator(name="back")
        neck = cmds.spaceLocator(name="neck")
        head = cmds.spaceLocator(name="head")
        headTop = cmds.spaceLocator(name="headTop")

        cmds.xform(R_hipLoc, absolute=True, translation=(-6.25, 40, 1))
        cmds.xform(R_kneeLoc, absolute=True, translation=(-6.25, 25, 2))  
        cmds.xform(R_ankleLoc, absolute=True, translation=(-6.25, 7, 0.5))
        cmds.xform(R_footLoc, absolute=True, translation=(-6.25, 2, 4))
        cmds.xform(R_toesLoc, absolute=True, translation=(-6.25, 2, 10))

        cmds.xform(L_hipLoc, absolute=True, translation=(6.25, 40, 1))
        cmds.xform(L_kneeLoc, absolute=True, translation=(6.25, 25, 2))
        cmds.xform(L_ankleLoc, absolute=True, translation=(6.25, 7, 0.5))
        cmds.xform(L_footLoc, absolute=True, translation=(6.25, 2, 4))
        cmds.xform(L_toesLoc, absolute=True, translation=(6.25, 2, 10))

        cmds.xform(C_hipLoc, absolute=True, translation=(0, 42, 1))

        cmds.xform(R_shoulderLoc, absolute=True, translation=(-10, 67, -1))
        cmds.xform(R_elbowLoc, absolute=True, translation=(-20, 65.5, -1.5))
        cmds.xform(R_wristLoc, absolute=True, translation=(-31, 65.5, -1))
        cmds.xform(R_handLoc, absolute=True, translation=(-35, 65.5, -0.7))
        cmds.xform(R_thumb1, absolute=True, translation=(-35.5, 64.5, 2))
        cmds.xform(R_thumb2, absolute=True, translation=(-37.5, 63.5, 3.25))
        cmds.xform(R_thumb3, absolute=True, translation=(-38, 63, 3.8))
        cmds.xform(R_index1, absolute=True, translation=(-38, 65.8, 1))
        cmds.xform(R_index2, absolute=True, translation=(-39, 65.8, 1))
        cmds.xform(R_index3, absolute=True, translation=(-40.7, 65.7, 1))
        cmds.xform(R_index4, absolute=True, translation=(-42, 65.5, 1.1))
        cmds.xform(R_middle1, absolute=True, translation=(-38, 66, -0.6))
        cmds.xform(R_middle2, absolute=True, translation=(-39.8, 66, -0.6))
        cmds.xform(R_middle3, absolute=True, translation=(-41.5, 65.7, -0.6))
        cmds.xform(R_middle4, absolute=True, translation=(-42.8, 65.5, -0.6))
        cmds.xform(R_ring1, absolute=True, translation=(-37.5, 66, -2))
        cmds.xform(R_ring2, absolute=True, translation=(-39.5, 66, -2))
        cmds.xform(R_ring3, absolute=True, translation=(-41, 65.8, -2))
        cmds.xform(R_ring4, absolute=True, translation=(-42.2, 65.5, -2))
        cmds.xform(R_small1, absolute=True, translation=(-37, 65.8, -3.3))
        cmds.xform(R_small2, absolute=True, translation=(-39, 65.8, -3.45))
        cmds.xform(R_small3, absolute=True, translation=(-40.2, 65.6, -3.5))
        cmds.xform(R_small4, absolute=True, translation=(-41.2, 65.6, -3.6))

        cmds.xform(R_clavicle, absolute=True, translation=(-4.5, 65, 0))

        cmds.xform(L_shoulderLoc, absolute=True, translation=(10, 67, -1))
        cmds.xform(L_elbowLoc, absolute=True, translation=(20, 65.5, -1.5))
        cmds.xform(L_wristLoc, absolute=True, translation=(31, 65.5, -1))
        cmds.xform(L_handLoc, absolute=True, translation=(35, 65.5, -0.7))
        cmds.xform(L_thumb1, absolute=True, translation=(35.5, 64.5, 2))
        cmds.xform(L_thumb2, absolute=True, translation=(37.5, 63.5, 3.25))
        cmds.xform(L_thumb3, absolute=True, translation=(38, 63, 3.8))
        cmds.xform(L_index1, absolute=True, translation=(38, 65.8, 1))
        cmds.xform(L_index2, absolute=True, translation=(39, 65.8, 1))
        cmds.xform(L_index3, absolute=True, translation=(40.7, 65.7, 1))
        cmds.xform(L_index4, absolute=True, translation=(42, 65.5, 1.1))
        cmds.xform(L_middle1, absolute=True, translation=(38, 66, -0.6))
        cmds.xform(L_middle2, absolute=True, translation=(39.8, 66, -0.6))
        cmds.xform(L_middle3, absolute=True, translation=(41.5, 65.7, -0.6))
        cmds.xform(L_middle4, absolute=True, translation=(42.8, 65.5, -0.6))
        cmds.xform(L_ring1, absolute=True, translation=(37.5, 66, -2))
        cmds.xform(L_ring2, absolute=True, translation=(39.5, 66, -2))
        cmds.xform(L_ring3, absolute=True, translation=(41, 65.8, -2))
        cmds.xform(L_ring4, absolute=True, translation=(42.2, 65.5, -2))
        cmds.xform(L_small1, absolute=True, translation=(37, 65.8, -3.3))
        cmds.xform(L_small2, absolute=True, translation=(39, 65.8, -3.45))
        cmds.xform(L_small3, absolute=True, translation=(40.2, 65.6, -3.5))
        cmds.xform(L_small4, absolute=True, translation=(41.2, 65.6, -3.6))

        cmds.xform(L_clavicle, absolute=True, translation=(4.5, 65, 0))

        cmds.xform(lowerBack, absolute=True, translation=(0, 48, 1))
        cmds.xform(back, absolute=True, translation=(0, 60, 0.5))
        cmds.xform(neck, absolute=True, translation=(0, 69, 0))
        cmds.xform(head, absolute=True, translation=(0, 74, 0.5))
        cmds.xform(headTop, absolute=True, translation=(0, 99.5, -2))

    def setupJoints(self, *args):
        global R_hipLoc
        global R_kneeLoc
        global R_ankleLoc
        global R_footLoc
        global R_toesLoc

        global L_hipLoc
        global L_kneeLoc
        global L_ankleLoc
        global L_footLoc
        global L_toesLoc

        global C_hipLoc

        global R_shoulderLoc
        global R_elbowLoc
        global R_wristLoc
        global R_handLoc
        global R_thumb1
        global R_thumb2
        global R_thumb3
        global R_index1
        global R_index2
        global R_index3
        global R_index4
        global R_middle1
        global R_middle2
        global R_middle3
        global R_middle4
        global R_ring1
        global R_ring2
        global R_ring3
        global R_ring4
        global R_small1
        global R_small2
        global R_small3
        global R_small4

        global R_clavicle

        global L_shoulderLoc
        global L_elbowLoc
        global L_wristLoc
        global L_handLoc
        global L_thumb1
        global L_thumb2
        global L_thumb3
        global L_index1
        global L_index2
        global L_index3
        global L_index4
        global L_middle1
        global L_middle2
        global L_middle3
        global L_middle4
        global L_ring1
        global L_ring2
        global L_ring3
        global L_ring4
        global L_small1
        global L_small2
        global L_small3
        global L_small4

        global L_clavicle

        global lowerBack
        global back
        global neck
        global head
        global headTop
        
        #LEFT FOOT
        cmds.select(clear=True)

        pos = cmds.xform(L_hipLoc, query=True, translation=True, worldSpace=True)
        self.L_hipJoint = cmds.joint(position=pos, name="L_hipJoint")#stored in self. for ik later

        pos = cmds.xform(L_kneeLoc, query=True, translation=True, worldSpace=True)
        L_kneeJoint = cmds.joint(position=pos, name="L_kneeJoint")
        # there's more
        # prevents the knee joint from rotating around either the x or y axes
        cmds.setAttr(L_kneeJoint + ".jointTypeX", 0)
        cmds.setAttr(L_kneeJoint + ".jointTypeY", 0)
        # makes the knee rotate from -90 to 0 degrees only
        # the 1,1 at enableRotationZ states that there is a limit in the maximum and minimum
        cmds.transformLimits(L_kneeJoint, rotationZ=(-90, 0), enableRotationZ=(1,1))


        pos = cmds.xform(L_ankleLoc, query=True, translation=True, worldSpace=True)
        self.L_ankleJoint = cmds.joint(position=pos, name="L_ankleJoint")#stored in self. for ik later

        pos = cmds.xform(L_footLoc, query=True, translation=True, worldSpace=True)
        L_footJoint = cmds.joint(position=pos, name="L_footJoint")

        pos = cmds.xform(L_toesLoc, query=True, translation=True, worldSpace=True)
        L_toesJoint = cmds.joint(position=pos, name="L_toesJoint")
        
        #cmds.ikHandle(startJoint=L_hipJoint, endEffector=L_ankleJoint, name="L_LegIKH") #IK COULD BE DONE HERE?


        #RIGHT FOOT
        cmds.select(clear=True)

        pos = cmds.xform(R_hipLoc, query=True, translation=True, worldSpace=True)
        self.R_hipJoint = cmds.joint(position=pos, name="R_hipJoint")#stored in self. for ik later

        pos = cmds.xform(R_kneeLoc, query=True, translation=True, worldSpace=True)
        R_kneeJoint = cmds.joint(position=pos, name="R_kneeJoint")
        # there's more
        # prevents the knee joint from rotating around either the x or y axes
        cmds.setAttr(R_kneeJoint + ".jointTypeX", 0)
        cmds.setAttr(R_kneeJoint + ".jointTypeY", 0)
        # makes the knee rotate from -90 to 0 degrees only
        # the 1,1 at enableRotationZ states that there is a limit in the maximum and minimum
        cmds.transformLimits(R_kneeJoint, rotationZ=(-90, 0), enableRotationZ=(1,1))


        pos = cmds.xform(R_ankleLoc, query=True, translation=True, worldSpace=True)
        self.R_ankleJoint = cmds.joint(position=pos, name="R_ankleJoint")#stored in self. for ik later

        pos = cmds.xform(R_footLoc, query=True, translation=True, worldSpace=True)
        R_footJoint = cmds.joint(position=pos, name="R_footJoint")

        pos = cmds.xform(R_toesLoc, query=True, translation=True, worldSpace=True)
        R_toesJoint = cmds.joint(position=pos, name="R_toesJoint")

        #cmds.ikHandle(startJoint=R_hipJoint, endEffector=R_ankleJoint, name="R_LegIKH") #IK COULD BE DONE HERE?

        #create centre hip joint
        cmds.select(clear=True)

        pos = cmds.xform(C_hipLoc, query=True, translation=True, worldSpace=True)
        self.C_hipJoint = cmds.joint(position=pos, name="C_hipJoint")#stored in self. for ik later

        #join the legs with the centre hip
        cmds.select(clear=True)

        #cmds.parent(L_hipJoint, 'L_LegIKH', C_hipJoint)
        #cmds.parent(R_hipJoint, 'R_LegIKH', C_hipJoint)
        cmds.parent(self.L_hipJoint, self.C_hipJoint)
        cmds.parent(self.R_hipJoint, self.C_hipJoint)

        #LEFT ARM
        cmds.select(clear=True)

        pos = cmds.xform(L_shoulderLoc, query=True, translation=True, worldSpace=True)
        self.L_shoulderJoint = cmds.joint(position=pos, name="L_shoulderJoint")#stored in self. for ik later

        pos = cmds.xform(L_elbowLoc, query=True, translation=True, worldSpace=True)
        L_elbowJoint = cmds.joint(position=pos, name="L_elbowJoint")   

        pos = cmds.xform(L_wristLoc, query=True, translation=True, worldSpace=True)
        self.L_wristJoint = cmds.joint(position=pos, name="L_wristJoint")#stored in self. for ik later

        pos = cmds.xform(L_handLoc, query=True, translation=True, worldSpace=True)
        L_handJoint = cmds.joint(position=pos, name="L_handJoint")

        pos = cmds.xform(L_thumb1, query=True, translation=True, worldSpace=True)
        L_thumb1Joint = cmds.joint(position=pos, name="L_thumb1Joint")

        pos = cmds.xform(L_thumb2, query=True, translation=True, worldSpace=True)
        L_thumb2Joint = cmds.joint(position=pos, name="L_thumb2Joint")

        pos = cmds.xform(L_thumb3, query=True, translation=True, worldSpace=True)
        L_thumb3Joint = cmds.joint(position=pos, name="L_thumb3Joint")

        cmds.select(clear=True)
        pos = cmds.xform(L_index1, query=True, translation=True, worldSpace=True)
        L_index1Joint = cmds.joint(position=pos, name="L_index1Joint")

        pos = cmds.xform(L_index2, query=True, translation=True, worldSpace=True)
        L_index2Joint = cmds.joint(position=pos, name="L_index2Joint")

        pos = cmds.xform(L_index3, query=True, translation=True, worldSpace=True)
        L_index3Joint = cmds.joint(position=pos, name="L_index3Joint")

        pos = cmds.xform(L_index4, query=True, translation=True, worldSpace=True)
        L_index4Joint = cmds.joint(position=pos, name="L_index4Joint")

        cmds.select(clear=True)
        cmds.parent(L_index1Joint, L_handJoint)

        cmds.select(clear=True)
        pos = cmds.xform(L_middle1, query=True, translation=True, worldSpace=True)
        L_middle1Joint = cmds.joint(position=pos, name="L_middle1Joint")

        pos = cmds.xform(L_middle2, query=True, translation=True, worldSpace=True)
        L_middle2Joint = cmds.joint(position=pos, name="L_middle2Joint")

        pos = cmds.xform(L_middle3, query=True, translation=True, worldSpace=True)
        L_middle3Joint = cmds.joint(position=pos, name="L_middle3Joint")

        pos = cmds.xform(L_middle4, query=True, translation=True, worldSpace=True)
        L_middle4Joint = cmds.joint(position=pos, name="L_middle4Joint")

        cmds.select(clear=True)
        cmds.parent(L_middle1Joint, L_handJoint)

        cmds.select(clear=True)
        pos = cmds.xform(L_ring1, query=True, translation=True, worldSpace=True)
        L_ring1Joint = cmds.joint(position=pos, name="L_ring1Joint")

        pos = cmds.xform(L_ring2, query=True, translation=True, worldSpace=True)
        L_ring2Joint = cmds.joint(position=pos, name="L_ring2Joint")

        pos = cmds.xform(L_ring3, query=True, translation=True, worldSpace=True)
        L_ring3Joint = cmds.joint(position=pos, name="L_ring3Joint")

        pos = cmds.xform(L_ring4, query=True, translation=True, worldSpace=True)
        L_ring4Joint = cmds.joint(position=pos, name="L_ring4Joint")

        cmds.select(clear=True)
        cmds.parent(L_ring1Joint, L_handJoint)

        cmds.select(clear=True)
        pos = cmds.xform(L_small1, query=True, translation=True, worldSpace=True)
        L_small1Joint = cmds.joint(position=pos, name="L_small1Joint")

        pos = cmds.xform(L_small2, query=True, translation=True, worldSpace=True)
        L_small2Joint = cmds.joint(position=pos, name="L_small2Joint")

        pos = cmds.xform(L_small3, query=True, translation=True, worldSpace=True)
        L_small3Joint = cmds.joint(position=pos, name="L_small3Joint")

        pos = cmds.xform(L_small4, query=True, translation=True, worldSpace=True)
        L_small4Joint = cmds.joint(position=pos, name="L_small4Joint")

        cmds.select(clear=True)
        cmds.parent(L_small1Joint, L_handJoint)

        #cmds.ikHandle(startJoint=L_shoulderJoint, endEffector=L_wristJoint, name="L_ArmIKH")    #IK COULD BE DONE HERE?

        #join the arm with the clavicle
        cmds.select(clear=True)
        pos = cmds.xform(L_clavicle, query=True, translation=True, worldSpace=True)
        L_clavicleJoint = cmds.joint(position=pos, name="L_clavicleJoint")

        cmds.select(clear=True)

        #cmds.parent(L_shoulderJoint, 'L_ArmIKH', L_clavicleJoint)
        cmds.parent(self.L_shoulderJoint, L_clavicleJoint)

        #RIGHT ARM
        cmds.select(clear=True)

        pos = cmds.xform(R_shoulderLoc, query=True, translation=True, worldSpace=True)
        self.R_shoulderJoint = cmds.joint(position=pos, name="R_shoulderJoint")#stored in self. for ik later

        pos = cmds.xform(R_elbowLoc, query=True, translation=True, worldSpace=True)
        R_elbowJoint = cmds.joint(position=pos, name="R_elbowJoint")   

        pos = cmds.xform(R_wristLoc, query=True, translation=True, worldSpace=True)
        self.R_wristJoint = cmds.joint(position=pos, name="R_wristJoint")#stored in self. for ik later

        pos = cmds.xform(R_handLoc, query=True, translation=True, worldSpace=True)
        R_handJoint = cmds.joint(position=pos, name="R_handJoint")

        pos = cmds.xform(R_thumb1, query=True, translation=True, worldSpace=True)
        R_thumb1Joint = cmds.joint(position=pos, name="R_thumb1Joint")

        pos = cmds.xform(R_thumb2, query=True, translation=True, worldSpace=True)
        R_thumb2Joint = cmds.joint(position=pos, name="R_thumb2Joint")

        pos = cmds.xform(R_thumb3, query=True, translation=True, worldSpace=True)
        R_thumb3Joint = cmds.joint(position=pos, name="R_thumb3Joint")

        cmds.select(clear=True)
        pos = cmds.xform(R_index1, query=True, translation=True, worldSpace=True)
        R_index1Joint = cmds.joint(position=pos, name="R_index1Joint")

        pos = cmds.xform(R_index2, query=True, translation=True, worldSpace=True)
        R_index2Joint = cmds.joint(position=pos, name="R_index2Joint")

        pos = cmds.xform(R_index3, query=True, translation=True, worldSpace=True)
        R_index3Joint = cmds.joint(position=pos, name="R_index3Joint")

        pos = cmds.xform(R_index4, query=True, translation=True, worldSpace=True)
        R_index4Joint = cmds.joint(position=pos, name="R_index4Joint")

        cmds.select(clear=True)
        cmds.parent(R_index1Joint, R_handJoint)

        cmds.select(clear=True)
        pos = cmds.xform(R_middle1, query=True, translation=True, worldSpace=True)
        R_middle1Joint = cmds.joint(position=pos, name="R_middle1Joint")

        pos = cmds.xform(R_middle2, query=True, translation=True, worldSpace=True)
        R_middle2Joint = cmds.joint(position=pos, name="R_middle2Joint")

        pos = cmds.xform(R_middle3, query=True, translation=True, worldSpace=True)
        R_middle3Joint = cmds.joint(position=pos, name="R_middle3Joint")

        pos = cmds.xform(R_middle4, query=True, translation=True, worldSpace=True)
        R_middle4Joint = cmds.joint(position=pos, name="R_middle4Joint")

        cmds.select(clear=True)
        cmds.parent(R_middle1Joint, R_handJoint)

        cmds.select(clear=True)
        pos = cmds.xform(R_ring1, query=True, translation=True, worldSpace=True)
        R_ring1Joint = cmds.joint(position=pos, name="R_ring1Joint")

        pos = cmds.xform(R_ring2, query=True, translation=True, worldSpace=True)
        R_ring2Joint = cmds.joint(position=pos, name="R_ring2Joint")

        pos = cmds.xform(R_ring3, query=True, translation=True, worldSpace=True)
        R_ring3Joint = cmds.joint(position=pos, name="R_ring3Joint")

        pos = cmds.xform(R_ring4, query=True, translation=True, worldSpace=True)
        R_ring4Joint = cmds.joint(position=pos, name="R_ring4Joint")

        cmds.select(clear=True)
        cmds.parent(R_ring1Joint, R_handJoint)

        cmds.select(clear=True)
        pos = cmds.xform(R_small1, query=True, translation=True, worldSpace=True)
        R_small1Joint = cmds.joint(position=pos, name="R_small1Joint")

        pos = cmds.xform(R_small2, query=True, translation=True, worldSpace=True)
        R_small2Joint = cmds.joint(position=pos, name="R_small2Joint")

        pos = cmds.xform(R_small3, query=True, translation=True, worldSpace=True)
        R_small3Joint = cmds.joint(position=pos, name="R_small3Joint")

        pos = cmds.xform(R_small4, query=True, translation=True, worldSpace=True)
        R_small4Joint = cmds.joint(position=pos, name="R_small4Joint")

        cmds.select(clear=True)
        cmds.parent(R_small1Joint, R_handJoint)

        #cmds.ikHandle(startJoint=R_shoulderJoint, endEffector=R_wristJoint, name="R_ArmIKH")    #IK COULD BE DONE HERE?

        #join the arm with the clavicle
        cmds.select(clear=True)
        pos = cmds.xform(R_clavicle, query=True, translation=True, worldSpace=True)
        R_clavicleJoint = cmds.joint(position=pos, name="R_clavicleJoint")

        cmds.select(clear=True)

        #cmds.parent(R_shoulderJoint, 'R_ArmIKH', R_clavicleJoint)
        cmds.parent(self.R_shoulderJoint, R_clavicleJoint)

        #SPINE
        cmds.select(clear=True)

        pos = cmds.xform(lowerBack, query=True, translation=True, worldSpace=True)
        lowerBackJoint = cmds.joint(position=pos, name="lowerBackJoint")

        pos = cmds.xform(back, query=True, translation=True, worldSpace=True)
        backJoint = cmds.joint(position=pos, name="backJoint")

        pos = cmds.xform(neck, query=True, translation=True, worldSpace=True)
        self.neckJoint = cmds.joint(position=pos, name="neckJoint")#stored in self. for ik later

        pos = cmds.xform(head, query=True, translation=True, worldSpace=True)
        self.headJoint = cmds.joint(position=pos, name="headJoint")

        pos = cmds.xform(headTop, query=True, translation=True, worldSpace=True)
        headTopJoint = cmds.joint(position=pos, name="headJointTop")

        #Join the spine with the hip
        cmds.select(clear=True)
        cmds.parent(lowerBackJoint, self.C_hipJoint)

        #Join the clavicle with the neck
        cmds.select(clear=True)
        cmds.parent(L_clavicleJoint, self.neckJoint)
        cmds.select(clear=True)
        cmds.parent(R_clavicleJoint, self.neckJoint)

    def orientJointsUI(self, *args):
        print("// cometJointOrient\n")

        nAimAxis = cmds.radioButtonGrp(self.rbgAim, query=True, select=True)
        nUpAxis = cmds.radioButtonGrp(self.rbgUp, query=True, select=True)
        aimAxis = [0.0, 0.0, 0.0]
        upAxis = [0.0, 0.0, 0.0]

        revAim = 1.0
        if(cmds.checkBox(self.cbRevAim, query=True, value=True)):
            revAim = -1.0

        revUp = 1.0
        if(cmds.checkBox(self.cbRevUp, query=True, value=True)):
            revUp = -1.0

        if(nAimAxis == nUpAxis):
            cmds.warning("The Aim and UP axis are the same! Orientation probably won't work!")

        aimAxis[(nAimAxis-1)] = revAim
        upAxis[(nUpAxis-1)] = revUp

        upDir = [0.0, 0.0, 0.0]
        upDir[0] = cmds.floatFieldGrp(self.ffgUpDir, query=True, value1=True)
        upDir[1] = cmds.floatFieldGrp(self.ffgUpDir, query=True, value2=True)
        upDir[2] = cmds.floatFieldGrp(self.ffgUpDir, query=True, value3=True)

        joints = cmds.ls(selection=True, type="joint")

        #now is where the magic happens
        self.orientJoints(joints, aimAxis, upAxis, upDir)

        #end with same stuff selected!
        cmds.select(joints, replace=True)

    def orientJoints(self, joints, aimAxis, upAxis, upDir, *args):
        '''
        This function is the real worker orient procedure

        joints - array of joints to orient
        aimAxis - xyz array of what axis of joint does aim
        upAxis - xyz array of what axis of joint does up
        upDir - what vector to use for up direction

        '''
        nJnt = len(joints)
        print(nJnt)

        prevUp = [0, 0, 0] # this should be a vector
        
        # Now orient each joint
        for i in range(nJnt):
            # First we need to unparent everything and then store that
            childs = cmds.listRelatives(joints[i], children=True, type=("transform", "joint"))
            if(childs != None and len(childs) > 0):
                childs = cmds.parent(childs, world=True) # unparent and get NEW names in case they changed

            # Find parent for later in case we need it.
            parents = cmds.listRelatives(joints[i], parent=True)
            if(parents != None):
                parent = parents[0]

            # Now if we have a child joint...aim to that.
            aimTgt=""
            if(childs != None):
                for child in childs:
                    if(cmds.nodeType(child) == "joint"):
                        aimTgt = child
                        break

            if(aimTgt != ""):
                upVec = [0.0, 0.0, 0.0]

                if(upVec[0] == 0.0 and upVec[1] == 0.0 and upVec[2] == 0.0):
                    upVec = upDir

                aCons = cmds.aimConstraint(aimTgt, joints[i], aimVector=(aimAxis[0], aimAxis[1], aimAxis[2]), upVector=(upAxis[0], upAxis[1], upAxis[2]), worldUpVector=(upVec[0], upVec[1], upVec[2]), worldUpType="vector", weight=1.0)

                cmds.delete(aCons)

                # Now compare the up we used to the previous one.
                curUp = [upVec[0], upVec[1], upVec[2]]
                curUp = self.normalizeList(curUp)
                dot = self.dotProduct(curUp, prevUp) # dot product for angle betweemn...
                prevUp = [upVec[0], upVec[1], upVec[2]] # store for later

                if(i > 0 and dot <= 0.0):
                    # adjust the rotation axis 180 if it looks like we've flopped the wrong way!
                    cmds.xform(joints[i], relative=True, objectSpace=True, rotateAxis=((aimAxis[0]*180.0),(aimAxis[1]*180.0), (aimAxis[2]*180.0)))
                    prevUp = [prevUp[0]*-1.0, prevUp[1]*-1.0, prevUp[2]*-1.0]

                # And now finish clearing out joint axis...
                cmds.joint(joints[i], e=True, zeroScaleOrient=True)
                cmds.makeIdentity(joints[i], apply=True)

            elif(aimTgt == ""):
                # Otherwise if there is no target, just dup orientation of parent...
                oCons = cmds.orientConstraint(parent, joints[i], weight=1.0)

                cmds.delete(oCons)

                #And now finish clearing out joints axis...
                cmds.joint(joints[i], e=True, zeroScaleOrient=True)
                cmds.makeIdentity(joints[i], apply=True)

            # Now that we are done...reparent
            if(childs != None and len(childs) > 0):
                cmds.parent(childs, joints[i])
            
    def normalizeList(self, listNormal, *args):
        maxValue = max(listNormal)
        minValue = min(listNormal)
        for i in range(len(listNormal)):
            listNormal[i] = (listNormal[i] - minValue) / (maxValue - minValue)
        return listNormal

    def dotProduct(self, vector1, vector2, *args):
        return sum(x*y for x,y in zip(vector1, vector2))

    def setupIK(self, *args):         
        
        #All these are stored in self. for the control function later
        self.L_IK_Leg = cmds.ikHandle(startJoint=self.L_hipJoint, endEffector=self.L_ankleJoint, name="L_IK_Leg")
        self.R_IK_Leg = cmds.ikHandle(startJoint=self.R_hipJoint, endEffector=self.R_ankleJoint, name="R_IK_Leg")
        self.L_IK_Arm = cmds.ikHandle(startJoint=self.L_shoulderJoint, endEffector=self.L_wristJoint, name="L_IK_Arm")
        self.R_IK_Arm = cmds.ikHandle(startJoint=self.R_shoulderJoint, endEffector=self.R_wristJoint, name="R_IK_Arm")
        self.C_IK_Spine = cmds.ikHandle(startJoint=self.C_hipJoint, endEffector=self.neckJoint, name="C_IK_Spine", solver="ikSplineSolver")
        self.C_IK_Spine[2] = cmds.rename(self.C_IK_Spine[2], "spineCurve")        

    def bindSkin(self, *args):

        #We also bind the skin by first selecting all the joints and then bind the skin        
        characterMesh = cmds.ls(selection=True, type="transform")
        cmds.select(clear=True)
        allJoints = cmds.ls(type="joint")
        cmds.select(allJoints, replace=True)
        cmds.select(characterMesh, toggle=True)
        cmds.bindSkin()  

    def createControls(self, *args):         
        #Start creating controls for the character        

        #LEFT LEG
        #Get the location of where it is going to be placed
        pos = cmds.xform(L_ankleLoc, query=True, translation=True, worldSpace=True)
        #Create a NURBS circle for the foot control
        L_footControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=10, name="L_footControl")        
        #Snap the circle to the location
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        #freeze the transformation of the circle
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)        
        #Create point constraint and orient constraint
        cmds.pointConstraint(L_footControl, self.L_IK_Leg[0], offset=(0, 0, 0), weight=1) # ERROR! IT USES THE EFFECTOR NOT THE IKHANDLE
        cmds.orientConstraint(L_footControl, self.L_ankleJoint, maintainOffset=True, weight=1)

        #Repeat for the rest
        #LEFT KNEE
        pos = cmds.xform(L_kneeLoc, query=True, translation=True, worldSpace=True)
        L_kneeControl = cmds.circle(center=(0, 0, 0), normal=(0, 0, 1), sweep=360, radius=4, name="L_kneeControl")
        cmds.move(pos[0], pos[1], (pos[2] + 8.0), rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.poleVectorConstraint(L_kneeControl, self.L_IK_Leg[0], weight=1) # ERROR! IT USES THE EFFECTOR NOT THE IKHANDLE

        #RIGHT LEG
        pos = cmds.xform(R_ankleLoc, query=True, translation=True, worldSpace=True)
        R_footControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=10, name="R_footControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.pointConstraint(R_footControl, self.R_IK_Leg[0], offset=(0, 0, 0), weight=1)
        cmds.orientConstraint(R_footControl, self.R_ankleJoint, maintainOffset=True, weight=1)

        #RIGHT KNEE
        pos = cmds.xform(R_kneeLoc, query=True, translation=True, worldSpace=True)
        R_kneeControl = cmds.circle(center=(0, 0, 0), normal=(0, 0, 1), sweep=360, radius=4, name="R_kneeControl")
        cmds.move(pos[0], pos[1], (pos[2] + 8.0), rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.poleVectorConstraint(R_kneeControl, self.R_IK_Leg[0], weight=1)

        #LEFT ARM
        pos = cmds.xform(L_wristLoc, query=True, translation=True, worldSpace=True)
        L_armControl = cmds.circle(center=(0, 0, 0), normal=(1, 0, 0), sweep=360, radius=8, name="L_armControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.pointConstraint(L_armControl, self.L_IK_Arm[0], offset=(0, 0, 0), weight=1)
        cmds.orientConstraint(L_armControl, self.L_wristJoint, maintainOffset=True, weight=1)

        #LEFT ELBOW
        pos = cmds.xform(L_elbowLoc, query=True, translation=True, worldSpace=True)
        L_elbowControl = cmds.circle(center=(0, 0, 0), normal=(0, 0, 1), sweep=360, radius=4, name="L_elbowControl")
        cmds.move(pos[0], (pos[1] - 5.0), pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.poleVectorConstraint(L_elbowControl, self.L_IK_Arm[0], weight=1)

        #RIGHT ARM
        pos = cmds.xform(R_wristLoc, query=True, translation=True, worldSpace=True)
        R_armControl = cmds.circle(center=(0, 0, 0), normal=(1, 0, 0), sweep=360, radius=8, name="R_armControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.pointConstraint(R_armControl, self.R_IK_Arm[0], offset=(0, 0, 0), weight=1)
        cmds.orientConstraint(R_armControl, self.R_wristJoint, maintainOffset=True, weight=1)

        #RIGHT ELBOW
        pos = cmds.xform(R_elbowLoc, query=True, translation=True, worldSpace=True)
        R_elbowControl = cmds.circle(center=(0, 0, 0), normal=(0, 0, 1), sweep=360, radius=4, name="R_elbowControl")
        cmds.move(pos[0], pos[1], (pos[2] - 8.0), rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.poleVectorConstraint(R_elbowControl, self.R_IK_Arm[0], weight=1)

        #SPINE
        #HIP
        pos = cmds.xform(C_hipLoc, query=True, translation=True, worldSpace=True)  
        cmds.move(pos[0], pos[1], pos[2], self.C_IK_Spine[2]+".scalePivot", self.C_IK_Spine[2]+".rotatePivot", rotatePivotRelative=True)#snap the curve created by the ikspline to the hip
        C_hipControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=15, name="C_hipControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.pointConstraint(C_hipControl, self.C_IK_Spine[2], offset=(0, 0, 0), weight=1)
        cmds.orientConstraint(C_hipControl, self.C_IK_Spine[2], maintainOffset=True, skip="y", weight=1)
        cmds.connectAttr("C_hipControl.rotate.rotateY", "C_IK_Spine.roll", force=True)#create a connection between the control and the ikroll

        #CHEST
        pos = cmds.xform(back, query=True, translation=True, worldSpace=True)
        C_chestControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=15, name="C_chestControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.connectAttr("C_chestControl.rotate.rotateY", "C_IK_Spine.twist", force=True)#create a connection between the control and the iktwist

        #NECK
        pos = cmds.xform(neck, query=True, translation=True, worldSpace=True)
        C_neckControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=5, name="C_neckControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1) 
        cmds.pointConstraint(C_neckControl, self.neckJoint, offset=(0, 0, 0), weight=1)
        cmds.orientConstraint(C_hipControl, self.neckJoint, maintainOffset=True, weight=1)

        #HEAD
        pos = cmds.xform(head, query=True, translation=True, worldSpace=True)
        C_headControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=10, name="C_headControl")
        cmds.move(pos[0], pos[1], pos[2], rotatePivotRelative=True)
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)
        cmds.orientConstraint(C_headControl, self.headJoint, maintainOffset=True, weight=1)

        #MASTER CONTROL
        masterControl = cmds.circle(center=(0, 0, 0), normal=(0, 1, 0), sweep=360, radius=15, name="masterControl")
        cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0, pn=1)

        #Change the control hierarchy
        cmds.parent(L_kneeControl, L_footControl)
        cmds.parent(R_kneeControl, R_footControl)
        cmds.parent(L_elbowControl, L_armControl)
        cmds.parent(R_elbowControl, R_armControl)

        cmds.parent(L_armControl, C_chestControl)
        cmds.parent(R_armControl, C_chestControl)
        cmds.parent(C_headControl, C_chestControl)

        cmds.parent(C_chestControl, C_hipControl)        

        cmds.parent(L_footControl, masterControl)
        cmds.parent(R_footControl, masterControl)
        cmds.parent(C_hipControl, masterControl)

    def selectJoints(self, *args):
        allJoints = cmds.ls(type="joint")
        cmds.select(allJoints, replace=True)

    def obtainAllVariables(self, *args):
        #This is used when reloading the program, the global and self variables will be empty and are needed
        #This kind of works but it only gets the name of the object stored
        R_hipLoc = cmds.ls("R_hipLoc")
        R_kneeLoc = cmds.ls("R_kneeLoc")
        R_ankleLoc = cmds.ls("R_ankleLoc")
        R_footLoc = cmds.ls("R_footLoc")
        R_toesLoc = cmds.ls("R_toesLoc")

        L_hipLoc = cmds.ls("L_hipLoc")
        L_kneeLoc = cmds.ls("L_kneeLoc")
        L_ankleLoc = cmds.ls("L_ankleLoc")
        L_footLoc = cmds.ls("L_footLoc")
        L_toesLoc = cmds.ls("L_toesLoc")

        C_hipLoc = cmds.ls("C_hipLoc")

        R_shoulderLoc = cmds.ls("R_shoulderLoc")
        R_elbowLoc = cmds.ls("R_elbowLoc")
        R_wristLoc = cmds.ls("R_wristLoc")
        R_handLoc = cmds.ls("R_wristLoc")
        R_thumb1 = cmds.ls("R_thumb1")
        R_thumb2 = cmds.ls("R_thumb2")
        R_thumb3 = cmds.ls("R_thumb3")
        R_index1 = cmds.ls("R_index1")
        R_index2 = cmds.ls("R_index2")
        R_index3 = cmds.ls("R_index3")
        R_index4 = cmds.ls("R_index4")
        R_middle1 = cmds.ls("R_middle1")
        R_middle2 = cmds.ls("R_middle2")
        R_middle3 = cmds.ls("R_middle3")
        R_middle4 = cmds.ls("R_middle4")
        R_ring1 = cmds.ls("R_ring1")
        R_ring2 = cmds.ls("R_ring2")
        R_ring3 = cmds.ls("R_ring3")
        R_ring4 = cmds.ls("R_ring4")
        R_small1 = cmds.ls("R_small1")
        R_small2 = cmds.ls("R_small2")
        R_small3 = cmds.ls("R_small3")
        R_small4 = cmds.ls("R_small4")

        R_clavicle = cmds.ls("R_clavicle")

        L_shoulderLoc = cmds.ls("L_shoulderLoc")
        L_elbowLoc = cmds.ls("L_elbowLoc")
        L_wristLoc = cmds.ls("L_wristLoc")
        L_handLoc = cmds.ls("L_handLoc")
        L_thumb1 = cmds.ls("L_thumb1")
        L_thumb2 = cmds.ls("L_thumb2")
        L_thumb3 = cmds.ls("L_thumb3")
        L_index1 = cmds.ls("L_index1")
        L_index2 = cmds.ls("L_index2")
        L_index3 = cmds.ls("L_index3")
        L_index4 = cmds.ls("L_index4")
        L_middle1 = cmds.ls("L_middle1")
        L_middle2 = cmds.ls("L_middle2")
        L_middle3 = cmds.ls("L_middle3")
        L_middle4 = cmds.ls("L_middle4")
        L_ring1 = cmds.ls("L_ring1")
        L_ring2 = cmds.ls("L_ring2")
        L_ring3 = cmds.ls("L_ring3")
        L_ring4 = cmds.ls("L_ring4")
        L_small1 = cmds.ls("L_small1")
        L_small2 = cmds.ls("L_small2")
        L_small3 = cmds.ls("L_small3")
        L_small4 = cmds.ls("L_small4")

        L_clavicle = cmds.ls("L_clavicle")

        lowerBack = cmds.ls("lowerBack")
        back = cmds.ls("back")
        neck = cmds.ls("neck")
        head = cmds.ls("head")
        headTop = cmds.ls("headTop")

        self.L_hipJoint = cmds.ls("L_hipJoint")
        self.L_ankleJoint = cmds.ls("L_ankleJoint")
        self.R_hipJoint = cmds.ls("R_hipJoint")
        self.R_ankleJoint = cmds.ls("R_ankleJoint")
        self.L_shoulderJoint = cmds.ls("L_shoulderJoint")
        self.L_wristJoint = cmds.ls("L_wristJoint")
        self.R_shoulderJoint = cmds.ls("R_shoulderJoint")
        self.R_wristJoint = cmds.ls("R_wristJoint")

        self.L_IK_Leg = cmds.ls("L_IK_Leg")
        self.L_IK_Arm = cmds.ls("L_IK_Arm")
        self.R_IK_Leg = cmds.ls("R_IK_Leg")
        self.R_IK_Arm = cmds.ls("R_IK_Arm")

SetupIK()
