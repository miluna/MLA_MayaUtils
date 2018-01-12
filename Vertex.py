import maya.cmds as cmds


class Vertex:
	"""
	This class is used to treat vertices as objects and get all their attributes with a common methodology
	"""

	def __init__(self, name):
		self.name = name

	def getObjectName(self):
		return self.name.split('.')[0]

	def getWorldPosition(self):
		return cmds.pointPosition(self.name, world=True)