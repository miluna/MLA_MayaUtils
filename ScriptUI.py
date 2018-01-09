'''
Author: Miguel Angel Luna
Updated: 1/2018

'''

import maya.cmds as cmds

class ScriptUI:
	'''
	Script main UI class helps to create new script windows based on common procedures
	'''
	def __init__(self, name="New Script Window", id="ScriptUIWindow", width=300, height=500):
		self.id = id
		self.name = name
		
		if cmds.window(self.id, exists = True):
			cmds.deleteUI(self.id)
		
		cmds.window (self.id, title= name, iconName= name, sizeable=True, widthHeight=(width, height) )
		
	def addLayout (self, type="grid", id=""):
		'''
		Valid layouts are grid, column, tab and row. All buttons, text and sliders after the layout are parented to it.
		For adding a new layout to a tab, use cmds.setParent( '..' ) before adding it
		'''
		if type == "grid":
			return cmds.gridLayout(id, numberOfColumns=2, cellWidthHeight=(150, 30))
		if type == "column":
			return cmds.columnLayout(id)
		if type == "tab":
			return cmds.tabLayout(id, innerMarginWidth=5, innerMarginHeight=5)
		if type == "row":
			return cmds.rowLayout(id, numberOfColumns=4, columnWidth3=(80, 75, 150), adjustableColumn=2)
	
		
	def addText (self, labeling=""):
		return cmds.text(label= labeling)
	
	def addButton(self, text="", action=""):
		'''
		Adds a button to the UI. Use the action parameter in a string. 
		For a close window button use 'cmds.deleteUI("")' with the same ID name as your window as action parameter
		'''
		return cmds.button( label= text, command= action)
		
	def addSeparator (self, amount=1, styling="none"):
		if amount== 1:
			return cmds.separator( style= styling)
		else:
			for i in range(0, amount):
				cmds.separator( style= styling)
		
	def addField (self, type='int', id='newField'):
		'''
		Valid fields are text, int and float. 
		'''
		if type == "text":
			return cmds.textField(id)
		if type == "int":
			return cmds.intField(id, value= 0)
		if type == "float":
			return cmds.floatField(id, value= 0)
	
	def queryField (self, type='text', id='newField'):
		'''
		Valid fields are text, int and float. Query is based on the id of the field.
		'''
		if type == "text":
			return cmds.textField(id, query= True, text= True)
		if type == "int":
			return cmds.intField(id, query= True, value= True)
		if type == "float":
			return cmds.floatField(id, query= True, value= True)
			
	def addSlider (self, type='int', id='newField', minV= 100, maxV= 0, stepChange= 1):	
		'''
		Valid sliders are int and float.
		'''
		if type == "int":
			return cmds.intSliderGrp(id, field= True, min= minV, max= maxV, value=0, step= stepChange)
		else:
			return cmds.floatSliderGrp(id, field= True, min= minV, max= maxV, value=0, step= stepChange )

	def querySlider (self, type='int', id='newField'):
		'''
		Valid sliders are int and float. Query is based on the id of the field.
		'''
		if type == "int":
			return cmds.intSliderGrp(id, query= True, value= True)
		else:
			return cmds.floatSliderGrp(id, query= True, value= True)
	
	def showWindow(self):
		return cmds.showWindow(self.id)
