import maya.cmds as cmds
import math
import random

radius = 12
count = 80
angleUnit = 360.0 / count
centerCube = cmds.polyCube()[0]

for i in range(0,count):
    if random.random() < 0.5:
        newNode = cmds.polyCube (name="Prefix_")        
    else:
        newNode = cmds.polyCube ()
    
    x = math.cos(angleUnit * i * (math.pi/180)) * radius
    z = math.sin(angleUnit * i * (math.pi/180)) * radius
    
    cmds.setAttr (newNode[0] + ".translateX", x)
    cmds.setAttr (newNode[0] + ".translateZ", z)
    
    cmds.aimConstraint (centerCube, newNode[0])


transforms = cmds.ls ("Prefix_*", type="transform")
print transforms
