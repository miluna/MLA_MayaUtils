'''
Author: Miguel Angel Luna
Updated: 1/2018

'''

import json
import maya.cmds as cmds


def fileSelector(filetipe, filefilter):
    '''
    filetipe has values from 0 to 4: 0, any file (exists or not), 1 existing file, 2 directory and file, 3 directory, 4 names of one or more existing files
    '''
    if filefilter == "csv":
        return cmds.fileDialog2(fileMode=filetipe, fileFilter="Comma Separated Values (*.csv)", dialogStyle=2)
    if filefilter == "json":
        return cmds.fileDialog2(fileMode=filetipe, fileFilter="Json file (*.json)", dialogStyle=2)
    else:
        return cmds.fileDialog2(fileMode=filetipe, fileFilter=filefilter, dialogStyle=2)


def readJsonFile():
    try:
        file = fileSelector(1, "json")
        with open(file[0], 'r') as jsonFile:
            return json.load(jsonFile)
    except:
        cmds.error("Could not read json file")


def writeJsonFile(content):
    try:
        file = fileSelector(0, "json")
        with open(file[0], "w") as jsonFile:
            json.dump(content, jsonFile, sort_keys=True, indent=4, separators=(',', ': '))
            print "Data was successfully written",
        except:
        cmds.error("Could not write json file")


def readCsvFile():
    try:
        file = fileSelector(1, "csv")
        with open(file[0], "r") as csvfile:
            reader = csv.reader(csvfile)
            return reader
    except:
        cmds.error("Could not read csv file")


def saveCsvFile(content, header=""):
    try:
        file = fileSelector(0)
        with open(file[0], "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\')
            writer.writerow(header)
            writer.writerow(content)
    except:
        cmds.error("Could not write csv file")
