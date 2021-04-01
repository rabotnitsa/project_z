
'''
Program: mantra_qc_tool
Author: Taos Myers
Layout  Mantra QC Render Tool
'''
import hou
import sys
import os 
import glob
import re
from os import listdir
from os.path import isfile, join
from mpi.api import asset

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

#Load .hip File
hou.hipFile.clear(suppress_save_prompt=False)
source_file = "path/to/*.hip"
hou.hipFile.merge(source_file, node_pattern="*", overwrite_on_conflict=False, ignore_load_warnings=True)
hou.session.houdiniSessionManager.update_production_variables(override=True)
hou.session.houdiniSessionManager.update_frame_variables(override=True)
print bcolors.OKBLUE + "Successfully loaded: " + bcolors.ENDC + source_file

#Save the .hip file
def save_file():
	Job = os.getenv('M_JOB')
	Shot = os.getenv('M_SHOT')
	Seq = os.getenv('M_SEQUENCE')
	Task = os.getenv('M_TASK')

#Set the path to the save directory. Check if dir exists. If not, create it
mypath = os.path.join("/jobs/" + Job + "/" + Seq + "/" + Shot + "/TASKS/layout/houdini/layoutQCRender/")
save_file()
print bcolors.OKBLUE + "Save Directory is: " + bcolors.ENDC + mypath

if os.path.exists(mypath):
	print bcolors.OKBLUE + "Directory structure exists" + bcolors.ENDC
	pass
else:
	os.mkdir(mypath)
	print bcolors.OKBLUE + "Path " + mypath + " does not exist. Creating path now."

myfirstfile = os.path.join("/jobs/" + Job + "/" + Seq + "/" + Shot + "/TASKS/layout/houdini/layoutQCRender
/" + Shot + "_layoutQCRender_v0001.hip")
hou.session.houdiniSessionManager.update_frame_variables(override=True)

#Look through hip dir and save if empty
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
if(len(onlyfiles)<1):
	print "No hip files exist \n"
	hou.session.houdiniSessionManager.update_production_variables(override=True)
	hou.session.houdiniSessionManager.update_frame_variables(override=True)
	hou.hipFile.save(myfirstfile)
	print bcolors.OKBLUE + "Saving hip file to: " + bcolors.ENDC + myfirstfile

#Add a camera and set work_in/out
add_camera = hou.node("/obj")
mycam = add_camera.createNode('ms::alembic_shotcam::1.0')

#Get highest Cam version
camDir = os.path.join("/jobs/" + Job + "/" + Seq + "/" + Shot + "/PRODUCTS/instances/shotcam1_main
/default/")
i = 0
for (path, dirs, files) in os.walk(camDir):
	i += 1
	if i == 1:
		camList = dirs
		highestCam = max(camList)
		startPath = camDir + highestCam
		endPath = os.path.join("/camera/abc/" + Shot +"_shotcam1_main_default_camera_" + highestCam + ".abc")
		fullCamPath = startPath + endPath
		print fullCamPath

#Get URI
av = asset.search_asset_versions(path=fullCamPath)
for i in av:
	URI = i.asset_uri
	print "URI name is " + URI
	itemSplit = highestCam.split("0")
	uri_number = ":" + "".join(itemSplit[1:])
	print "URI number is " + uri_number
	URI += uri_number
	print "Full URI is " + URI

#Set fileName attr and URI
mycam.parm('fileName').set(str(fullCamPath))
mycam.parm('camuri').set(str(URI))
mycam.parm('camera').set(str(URI))
mycam.parm('refresh_all').set(True)
mycam.parm('refresh_all').set(0)
mycam.parm('invisparm').pressButton()
mycam.hm().clear_cache()
mycam.parm('refresh_all').set(True)
mycam.parm('camera').pressButton()
mycam.parm('resx').set('3414')
mycam.parm('resy').set('2198')

#Iterate through files in the dir and split out the version numbers
onlyfiles = sorted(onlyfiles)
print(onlyfiles)
mysplit = re.findall("_v" + '(\d+)', onlyfiles[-1])
print("\n")

#Find the highest file number in the list of files in the save dir
highest = mysplit[-1]
print bcolors.OKBLUE + "Highest file number is: " + bcolors.ENDC
print highest
print "\n"

#If highest file in dir is higher than v0001, increment by one
intNumber = 0001
if highest > intNumber:
	intNumber = intHighest + 0001

#Convert 'intNumber' to a string and assign to a new variable
number = "%04d" % (intNumber)

#Save incremented file to disk
filetosave = os.path.join("/jobs/" + Job + "/" + Seq + "/" + Shot + "/TASKS/layout/houdini
/layoutQCRender/" + Shot + "_layoutQCRender_v" + number + ".hip")
print bcolors.OKBLUE + "Saving v" + number + " hip file to: " + bcolors.ENDC + filetosave + "\n"
hou.session.houdiniSessionManager.update_production_variables(override=True)
hou.session.houdiniSessionManager.update_frame_variables(override=True)
hou.hipFile.save(filetosave)

#Add a camera and set work_in/out
user_camera  = hou.node("/obj")
mycamb = user_camera.createNode('ms::alembic_shotcam::1.0')

#Get highest Cam version
camDir = os.path.join("/jobs/" + Job + "/" + Seq + "/" + Shot + "/PRODUCTS/instances/shotcam1_main/default/")
i = 0
for (path, dirs, files) in os.walk(camDir):
	i += 1
	if i == 1:
		camList = dirs
		highestCam = max(camList)
		startPath = camDir + highestCam
		endPath = os.path.join("/camera/abc/" + Shot +"_shotcam1_main_default_camera_" + highestCam + ".abc")
		fullCamPath = startPath + endPath
		print fullCamPath

#Get URI
av = asset.search_asset_versions(path=fullCamPath)
for i in av:
	URI = i.asset_uri
	print "URI name is " + URI
	itemSplit = highestCam.split("0")
	uri_number = ":" + "".join(itemSplit[1:])
	print "URI number is " + uri_number
	URI += uri_number
	print "Full URI is " + URI

#Save .hip file
hou.hipFile.save(filetosave)
print bcolors.OKBLUE + "Updated vars and saving hip file to: " + bcolors.ENDC + filetosave + "\n"
save_file()