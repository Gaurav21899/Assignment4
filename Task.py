import arcpy
import os

gdb_path = r"D:\Sem-3\Programming for GIS-3\P4_Working_With_Selection\ProProject_Selections\ProProject_Selections.gdb"
Histdist_fc_name = "Wilson_Histdist"

Histdist_fc_path = os.path.join(gdb_path, Histdist_fc_name)
arcpy.management.MakeFeatureLayer(Histdist_fc_path, "Histdist_layer")

feature_count = arcpy.GetCount_management("Histdist_layer")
print("Count of the Histdist  is", feature_count)
