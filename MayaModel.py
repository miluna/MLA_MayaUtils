'''
Author: Miguel Angel Luna
'''
import maya.cmds as cmds

class MayaModel:
	'''
	MayaModel class is used to interact with common Maya geometries and transform nodes using standard maya.cmds commands with OOP
	'''
	def __init__(self, name):
		self.nameSpace = ""
		self.hierarchy = ""
		self.name = ""
		self.getNames(name)
		self.fullname = name

		#Attributes made private because they change while being used with Maya. You should use getters to access
		self._position = []
		self._worldPosition = []
		self._pivot = []
		self._rotation = []
		self._scale = []


	def getNames(self, name):
		try:
			self.nameSpace = name.split(":")[0]
			self.name = name.split(":")[1]
		except:
			self.nameSpace = None
			self.name = name
		try:
			self.hierarchy = name.split("|")[0:-1]
			self.name = name.split("|")[-1]
		except:
			self.hierarchy = None
			self.name = name

	def getPosition(self):
		del self._position[:]
		self._position = cmds.xform(self.fullname, query=True, translation=True)
		return self._position

	def getWorldPosition(self):
		del self._worldPosition[:]

		self._worldPosition = cmds.xform(self.fullname, query=True, worldSpace=True, translation=True)
		return self._worldPosition

	def getRotation(self):
		del self._rotation[:]

		self._rotation = cmds.xform(self.fullname, query=True, rotation=True)
		return self._rotation

	def getScale(self):
		del self._scale[:]

		self.scaleX = cmds.getAttr(self.fullname + ".scaleX")
		self.scaleY = cmds.getAttr(self.fullname + ".scaleY")
		self.scaleZ = cmds.getAttr(self.fullname + ".scaleZ")
		self._scale.append(self.scaleX)
		self._scale.append(self.scaleY)
		self._scale.append(self.scaleZ)
		return self._scale

	def getPivot(self):
		self._pivot = cmds.xform(self.fullname, query=True, worldSpace=True, rotatePivot=True)
		return self._pivot

	def setPosition(self, positionArray):
		cmds.xform (self.fullname,translation=positionArray)

	def setRotation(self, rotationArray):
		cmds.xform(self.fullname, rotation=rotationArray)

	def setScale(self, scaleArray):
		cmds.xform(self.fullname, scale=scaleArray)

	def setPivot(self, pivotArray):
		cmds.xform(self.fullname, rotatePivot=pivotArray)
		cmds.xform(self.fullname, scalePivot=pivotArray)
		
	def toJson(self):
		dictionary = {
			"namespace":self.nameSpace,
			"hierarchy":self.hierarchy,
			"name":self.name,
			"pivot":self.getPivot(),
			"position":self.getPosition(),
			"rotation":self.getRotation(),
			"scale":self.getScale()
		}
		return json.dumps(dictionary, sort_keys=True, indent=4, separators=(',', ': '))
