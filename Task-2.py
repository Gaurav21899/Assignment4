import arcpy
import os
gdb_path = r"D:\Sem-3\Programming for GIS-3\P4_Working_With_Selection\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
crime_fc_name_path = os.path.join(gdb_path, crime_fc_name)

# Converting a feature class to feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_layer")
arcpy.management.MakeFeatureLayer(crime_fc_name_path, "crime_layer")

arcpy.management.SelectLayerByLocation("crime_layer", "WITHIN_A_DISTANCE", "restaurant_layer", "500 meters")

output_crime_restaurant = "crime_within_500meters"
output_crime_restaurant_path = os.path.join(gdb_path, output_crime_restaurant)

Crime_count = arcpy.GetCount_management("crime_layer")
print("The Count of Crime within 500 meters of distance from all the restaurants is ", Crime_count)
print("Process Complete")

