import maya.cmds as cmds

joints = cmds.ls(type="joint")

for joint in joints:
    parents = cmds.listRelatives(joint, p=True);
    if parents == None:
        print "Root: " + joint
        break

for joint in joints:
	children = cmds.listRelatives(joint, c=True);
	if children == None:
		print "Found Leaf: " + joint