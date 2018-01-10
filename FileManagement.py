'''
Author: Miguel Angel Luna
Static class created to manage files within Maya

'''

import csv
import json
import maya.cmds as cmds

class FileManager:
    
    @staticmethod
    def fileSelector(filetype, filefilter):
        '''
        filetipe has values from 0 to 4: 0, any file (exists or not), 1 existing file, 2 directory and file, 3 directory, 4 names of one or more existing files
        '''
        if filefilter == "csv":
            return cmds.fileDialog2(fileMode=filetype, fileFilter="Comma Separated Values (*.csv)", dialogStyle=2)
        if filefilter == "json":
            return cmds.fileDialog2(fileMode=filetype, fileFilter="Json file (*.json)", dialogStyle=2)
        else:
            return cmds.fileDialog2(fileMode=filetype, fileFilter=filefilter, dialogStyle=2)

    @staticmethod
    def readJsonFile():
        try:
            file = fileSelector(1, "json")
            with open(file[0], 'r') as jsonFile:
                return json.load(jsonFile)
        except:
            cmds.error("Could not read json file")

    @staticmethod
    def writeJsonFile(content):
        try:
            file = fileSelector(0, "json")
            with open(file[0], "w") as jsonFile:
                json.dump(content, jsonFile, sort_keys=True, indent=4, separators=(',', ': '))
                print "Data was successfully written",
            except:
            cmds.error("Could not write json file")

    @staticmethod
    def readCsvFile():
        try:
            file = fileSelector(1, "csv")
            with open(file[0], "r") as csvfile:
                reader = csv.reader(csvfile)
                return reader
        except:
            cmds.error("Could not read csv file")

    @staticmethod
    def saveCsvFile(content, header=""):
        try:
            file = fileSelector(0)
            with open(file[0], "w") as csvfile:
                writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
                writer.writerow(header)
                writer.writerow(content)
        except:
            cmds.error("Could not write csv file")
