import maya.cmds as cmds
import math
import random


cmds.file(f=True, new=True)

radius = 12
targetCount = 100
currentCount = 0

prefix = "Prefix_"

angleUnit = 360.0 / targetCount
centerSphere = cmds.polySphere() [0]

# allTypesOfNodes = cmds.allNodeTypes()

typeWhiteList = ("mesh", "transform", "cube", "cone", "sphere")
createNodes = []

# create 100 random cube
while currentCount < targetCount:
	selectedIndex = random.randint (0, len(typeWhiteList))
	selectedType = typeWhiteList[selectedIndex]

	newNode = None

	if selectedType == "cone":
		newNode = cmds.polyCone()[0]
		if random.random() < 0.5:
			cmds.aimConstraint (centerSphere, newNode)
	elif selectedType == "cube":
		newNode = cmds.polyCube()[0]
		if random.random() < 0.5:
			cmds.aimConstraint (centerSphere, newNode)
	elif selectedType == "sphere":
		newNode = cmds.polySphere()[0]
	else:
		newNode = cmds.createNode(selectedType)

	createNodes.append(newNode)


	x = math.cos(angleUnit * currentCount * (math.pi/180)) * radius
	z = math.sin(angleUnit * currentCount * (math.pi/180)) * radius

	if cmds.objExists(newNode + ".translateX"):
		cmds.setAttr (newNode + ".translateX", x)
	if cmds.objExists(newNode + ".translateX"):
		cmds.setAttr (newNode + ".translateZ", z)

	print "ls count: ", len (cmds.ls())
	print cmds.ls(fl=True)

	currentCount = len (createNodes)


# Get objects start with "Prefix_"
# transforms = cmds.ls ("%s*"%(prefix), type="transform")
meshes = cmds.ls ("%s*"%(prefix), type="mesh")

print meshes
