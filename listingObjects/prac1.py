import maya.cmds as cmds
import math
import random


cmds.file(f=True, new=True)

radius = 12
targetCount = 10
currentCount = 0

prefix = "Prefix_"

angleUnit = 360.0 / targetCount
centerCube = cmds.polyCube() [0]

allTypesOfNodes = cmds.allNodeTypes()

# create 100 random cube
while currentCount < targetCount:
    if random.random() < 0.5:
        newNode = cmds.polyCube (name="Prefix_") [0]

        if random.random() < 0.1:
    		cmds.aimConstraint (centerCube, newNode)
    elif random.random() < 0.5:
        newNode = cmds.polyCube () [0]
        print cmds.objectType(newNode)

        if random.random() < 0.1:
    		cmds.aimConstraint (centerCube, newNode)
        
    else:
    	a = random.randint(0, len (allTypesOfNodes))

    	# don't create manipulator
    	if allTypesOfNodes[a] != "Manipulator" and allTypesOfNodes[a] != "createEPManip" and allTypesOfNodes[a] != "cameraPlaneManip":

    		print allTypesOfNodes[a]
    		newNode = cmds.createNode(allTypesOfNodes[a])
    

    x = math.cos(angleUnit * i * (math.pi/180)) * radius
    z = math.sin(angleUnit * i * (math.pi/180)) * radius
    
    if cmds.objExists(newNode + ".translateX"):
    	cmds.setAttr (newNode + ".translateX", x)
    if cmds.objExists(newNode + ".translateX"):
    	cmds.setAttr (newNode + ".translateZ", z)

    print "ls count: ", len (cmds.ls())
    print cmds.ls(fl=True)
    currentCount = len (cmds.ls())


# Get objects start with "Prefix_"
transforms = cmds.ls ("%s*"%(prefix), type="transform")
print transforms
