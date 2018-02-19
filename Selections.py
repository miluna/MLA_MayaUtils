import maya.cmds as cmds
from Vertex import Vertex


class Selection:
	firstObjectPosition = []
	firstObjectPivot = []
	firstObjectVertices = []

	@staticmethod
	def getSelected():
		return cmds.ls(selection=True, flatten=True)

	@staticmethod
	def getSelectedInOrder():
		if cmds.selectPref(query=True, trackSelectionOrder=True) == False:
			cmds.selectPref(trackSelectionOrder=True)
		return cmds.ls(orderedSelection=True)

	@staticmethod
	def getChildren(groupName):
		return cmds.listRelatives(groupName, children=True)

	@staticmethod
	def roundList(numbersList):
		i=0
		for n in numbersList:
			numbersList[i] = round (n,3)
			i+=1
		return numbersList

	@staticmethod
	def getPosition(queriedObject):
		pos = cmds.xform(queriedObject, query=True, translation=True)
		pos = Selection.roundList(pos)
		return pos

	@staticmethod
	def getWorldPosition(queriedObject):
		pos = cmds.xform(queriedObject, query=True, worldSpace=True, translation=True)
		pos = Selection.roundList(pos)
		return pos

	@staticmethod
	def getRotation(queriedObject):
		rot = cmds.xform(queriedObject, query=True, rotation=True)
		rot = Selection.roundList(rot)
		return rot

	@staticmethod
	def getScale(queriedObject):
		scale = []
		sclX = cmds.getAttr(queriedObject + ".scaleX")
		scale.append(sclX)
		sclY = cmds.getAttr(queriedObject + ".scaleY")
		scale.append(sclY)
		sclZ = cmds.getAttr(queriedObject + ".scaleZ")
		scale.append(sclZ)
		scale = Selection.roundList(scale)
		return scale

	@staticmethod
	def getPivot(queriedObject):
		piv = cmds.xform(queriedObject, query=True, rotatePivot=True)
		piv = Selection.roundList(piv)
		return piv

	@staticmethod
	def getWorldPivot(queriedObject):
		piv = cmds.xform(queriedObject, query=True, worldSpace=True, rotatePivot=True)
		piv = Selection.roundList(piv)
		return piv

	@staticmethod
	def getRGB (model):
		try:
			RGB = []
			colorR = cmds.getAttr(model + ".colorR")
			colorG = cmds.getAttr(model + ".colorG")
			colorB = cmds.getAttr(model + ".colorB")

			RGB.append(colorR)
			RGB.append(colorG)
			RGB.append(colorB)
			RGB = Selection.roundList(RGB)
			return RGB
		except:
			RGB = [0, 0, 0]
			return RGB


	@staticmethod
	def storeSelection(transform="pivot", list=firstObjectPivot):
		'''
		Stores the selected objects inside of a Python list for future actions.
		You can get the transforms using pivot or translation parameters
		Recomended lists are firstObjectPivot = [] and firstObjectPosition = []
		'''
		if list:
			del list[:]

		transformation = []
		if transform == "pivot":
			transformation = cmds.xform(Selection.getSelected(), query=True, rotatePivot=True)
		if transform == "position":
			transformation = cmds.xform(Selection.getSelected(), query=True, translation=True)

		for number in transformation:
			list.append(number)

	@staticmethod
	def storeVertexSelection(list=firstObjectVertices):
		'''
		Converts selection to vertices, adds the vertices to the Vertex class and appends them to the list
		Recomended lists are firstObjectVertices = [] and secondObjectVertices = []
		'''
		if list:
			del list[:]
		cmds.select(cmds.polyListComponentConversion(cmds.ls(selection=True, flatten=True), toVertex=True))
		selection = Selection.getSelected()
		for i in xrange(0, len(selection)):
			vertex = Vertex(selection[i])
			list.append(vertex)

	@staticmethod
	def xformPaste(transform="pivot", list=firstObjectPivot):
		'''
		Pastes the stored first selection pivot or translation from a list to the selected objects
		Recomended lists are firstObjectPivot = [] and firstObjectPosition = []
		'''
		if transform == "pivot":
			cmds.xform(Selection.getSelected(), rotatePivot=[list[0], list[1], list[2]])
		if transform == "position":
			cmds.xform(Selection.getSelected(), translation=[list[0], list[1], list[2]])

	@staticmethod
	def getVertexCount():
		return cmds.polyEvaluate(Selection.getSelected(), v=True)

	@staticmethod
	def getDistanceBetweenVertices(vertexA, vertexB):
		'''
		This is a mathematic method which calculates the distance:
		squareRoot[ <(point1.x - point2.x)^2> + <(point1.y - point2.y)^2> + <(point1.z - point2.z)^2> ]
		'''

		vertexAx, vertexAy, vertexAz = vertexA.getWorldPosition()
		vertexBx, vertexBy, vertexBz = vertexB.getWorldPosition()

		distance = ((vertexAx - vertexBx) ** 2 + (vertexAy - vertexBy) ** 2 + (vertexAz - vertexBz) ** 2) ** 0.5
		return distance
	
	@staticmethod
	def getDistanceBetween (obj1Pos, obj2Pos):
		sumX = 0
		sumY = 0
		sumZ = 0

		i = 0
		for p in obj1Pos:
			if i == 0:
				print p
				sumX += p
			if i == 1:
				sumY += p
			if i == 2:
				sumZ += p
			i += 1

		i = 0
		for p in obj2Pos:
			if i == 0:
				sumX += p
			if i == 1:
				sumY += p
			if i == 2:
				sumZ += p
			i += 1

		middleposition = [sumX / 2, sumY / 2, sumZ / 2]
		return middleposition
