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
	def getPosition(queriedObject):
		pos = cmds.xform(queriedObject, query=True, translation=True)
		return pos

	@staticmethod
	def getWorldPosition(queriedObject):
		pos = cmds.xform(queriedObject, query=True, worldSpace=True, translation=True)
		return pos

	@staticmethod
	def getRotation(queriedObject):
		rot = cmds.xform(queriedObject, query=True, rotation=True)
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
		return scale

	@staticmethod
	def getPivot(queriedObject):
		piv = cmds.xform(queriedObject, query=True, rotatePivot=True)
		return piv

	@staticmethod
	def getWorldPivot(queriedObject):
		piv = cmds.xform(queriedObject, query=True, worldSpace=True, rotatePivot=True)
		return piv

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
	def vertexCount():
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
