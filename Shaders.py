import maya.cmds as cmds


class Shader:
	'''
	Shader class helps you automate shader and texture file creation inside of Maya
	'''

	@staticmethod
	def createShadingGroupNode(name):
		shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=name)

	@staticmethod
	def createShaderNode(name, shadername="lambert"):
		shadingNode = cmds.shadingNode(shadername, asShader=True, name=name)

	@staticmethod
	def createTextureNode(name, shadername="file", usePlace2d=True):
		textureNode = cmds.shadingNode(shadername, asTexture=True, name=name)
		cmds.setAttr(name + ".fileTextureName", name, type="string")

	@staticmethod
	def createUtilityNode(name, shadername="place2dTexture"):
		utilityNode = cmds.shadingNode(shadername, asUtility=True, name=name)

	@staticmethod
	def connectUtilityNodeToTextureNode(utilityNode, textureNode):
		cmds.connectAttr(utilityNode + ".outUV", textureNode + ".uvCoord")

	@staticmethod
	def connectTextureNodeToShaderNode(textureNode, shaderNode):
		cmds.connectAttr(textureNode + ".outColor", shaderNode + ".color")

	@staticmethod
	def connectShaderNodeToShadingGroupNode(shaderNode, shadingGroupNode):
		cmds.connectAttr(shaderNode + ".outColor", shadingGroupNode + ".surfaceShader")

	@staticmethod
	def getConnections(selected):
		connections = cmds.listConnections(selected, c=True)
		return connections

	@staticmethod
	def getShader(obj):
		cmds.select(obj)
		cmds.hyperShade(shaderNetworksSelectMaterialNodes=True)
		return cmds.ls(sl=True)  # Returns all shaders associated with the object (shape, face etc)

	@staticmethod
	def getShadersPerFace(shape):
		perFaceShaders = {}
		for f in range(cmds.polyEvaluate(shape, f=True)):
			face = shape + '.f[' + str(f) + ']'
			try:
				shader = Shader.getShader(face)
				perFaceShaders[face] = shader
			except:
				print 'Error: could not fetch shader for ' + face
		return perFaceShaders

	@staticmethod
	def createStandardShader(name):
		SG_name = "SG_" + name
		GS_name = "GS_" + name
		TX_name = "TX_" + name
		UtilNode_name = "2D_" + name

		Shader.createShadingGroupNode(SG_name)
		Shader.createShaderNode(GS_name)
		Shader.createTextureNode(TX_name)
		Shader.createUtilityNode(UtilNode_name)
		Shader.connectShaderNodeToShadingGroupNode(GS_name, SG_name)
		Shader.connectTextureNodeToShaderNode(TX_name, GS_name)
		Shader.connectUtilityNodeToTextureNode(UtilNode_name, TX_name)

	@staticmethod
	def createStingrayShader(name):
		#TODO
		pass

	@staticmethod
	def createArnoldStandardShader(name):
		#TODO
		pass

