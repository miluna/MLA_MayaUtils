'''
Author: Miguel Angel Luna
Description:
Class created to print useful information in a new window
'''

from ScriptUI import ScriptUI
from Selections import Selection
from Vertex import Vertex

class ScrollfieldPrinter:

	@staticmethod
	def removeNameSpace(objectName):
		try:
			modelClean = objectName.split(":")[1]
			return modelClean
		except:
			modelClean = objectName
			return modelClean

	@staticmethod
	def getTransforms(model, format="relative"):
		'''
		:param model: name of the object you want to process
		:param format: accepted formats are "relative", "world", "pivot" and "worldPivot"
		:return:
		'''
		if format == "relative":
			pos = Selection.getPosition(model)
		if format == "world":
			pos = Selection.getWorldPosition(model)
		if format == "pivot":
			pos = Selection.getPivot(model)
		else:
			pos = Selection.getWorldPivot(model)

		rot = Selection.getRotation(model)
		scale = Selection.getScale(model)

		transforms = [pos, rot, scale]
		return transforms

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
			return RGB
		except:
			RGB = [""]
			return RGB

	@staticmethod
	def printVertices ():
		ventana = ScriptUI
		ventana.addLayout("form")
		ventana.addScrollfield()

		vertices = Selection.getSelected()
		vertexCount = Selection.getVertexCount()
		for i in range(0, vertexCount + 1):
			currentVertex = Vertex(vertices[i])
			pos = currentVertex.getWorldPosition()
			printText = (str(round(pos[0], 4)) + " " + str(round(pos[1], 4)) + " " + str(round(pos[2], 4)) + "\n")
			ventana.addToScrollfield(printText)

	@staticmethod
	def printModel (transformType= "relative", format=""):
		ventana = ScriptUI
		ventana.addLayout("form")
		ventana.addScrollfield()

		for model in Selection.getSelected():
			modelName = ScrollfieldPrinter.removeNameSpace(model)

			transforms = ScrollfieldPrinter.getTransforms(model, transformType)
			translateX = round(transforms[0][0], 3)
			translateY = round(transforms[0][1], 3)
			translateZ = round(transforms[0][2], 3)

			rotateX = round(transforms[1][0], 3)
			rotateY = round(transforms[1][1], 3)
			rotateZ = round(transforms[1][2], 3)

			scaleX = round(transforms[2][0], 3)
			scaleY = round(transforms[2][1], 3)
			scaleZ = round(transforms[2][2], 3)

			if format == "":
				printText = (str(modelName) +
				       " t " + str(translateX) + " " + str(translateY) + " " + str(translateZ) +
				       " R " + str(rotateZ) + " " + str(rotateX) + " " + str(rotateY) +
				       " S " + str(scaleX) + " " + str(scaleY) + " " + str(scaleZ) + "\n")
				ventana.addToScrollfield(printText)

			if format == "light":
				RGB = ScrollfieldPrinter.getRGB(model)

				printText = ("#" + str(modelName) + " " +
				             " t " + str(translateX) + " " + str(translateY) + " " + str(translateZ) + " " +
				             " R " + str(rotateZ) + " " + str(rotateX) + " " + str(rotateY) + " " +
				             " C " + str(RGB[0]) + " " + str(RGB[1]) + " " + str(RGB[2]) + "\n")
				ventana.addToScrollfield(printText)



