'''
Program: rop_preset
Author: Taos Myers
 This is a shelf tool that will create a .preset file from the selected ROP designated as master 
'''
import hou

if(hou.selectedNodes()):
    selected = hou.selectedNodes(0)
    for rop in selected:
    selectedRop = rop.path()
        name = rop.name()
        roppath = rop.path()
        print roppath
        savepath = "/show/path/houdini/presets/Driver/" + name + ".preset"
        hou.hscript('oppresetsavefile %s "%s"' %(roppath, savepath))
        hou.ui.displayMessage("ROP preset saved to " + str(savepath))
else:
    hou.ui.displayMessage("No ROP selected", severity=hou.severityType.Warning)
