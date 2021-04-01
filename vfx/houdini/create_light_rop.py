'''
Program: light_rop_presets_lighting
Author: Taos Myers
Creates a Light ROP with presets for LIGHTING.
Requires a preset to be saved out named in the manner of the ropnamelist
'''
from houdini_render import mantra_rop

#Render Pass Names
ropnamelist = [
"env__a__bty",
"env__b__bty",
"env__C__bty",
"env__MASTER"
]

#define parent node
parent_node = hou.node("/out")

for item in ropnamelist:

# Create regular mantra rop
    rman_node = parent_node.createNode("ris::22", node_name=item)
    preset = "light" # This can be "fx", "light" or "lookdev"
    m_node = parent_node.createNode("ms::rw_data::1", node_name=item)

# Setup node
    mantra_rop.init_mantra_rop_with_preset(rman_node, preset=preset)

# Until descriptive parm are fast, disable them
    rman_node.setGenericFlag(hou.nodeFlag.DisplayDescriptiveName, False)
    
# print "item is " + item
    prop_node.setFirstInput(rman_node, 0)
    rman_node.moveToGoodPosition()
    prop_node.moveToGoodPosition()

# Load preset file
    presetfile = "/path/to/user/houdini/presets/Driver/" + item + ".preset"
    print "presetfile path is " + presetfile
    rpath = rman_node.path()
    print "rpath is " + rpath
    hou.hscript('oppresetloadfile %s "%s"'%(rpath, presetfile))
