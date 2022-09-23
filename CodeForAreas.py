import ifcopenshell
from blenderbim.bim.ifc import IfcStore
file = IfcStore.get_file()
import bpy

#Now import the file in the right viewport under Scene properties (marked with a logo with a rain drop)

#Now we pull out the class type (here the spaces) which we are interested in
spaces = file.by_type('IfcSpace')
#we can look up the number of spaces
len(spaces)

# and print their names which is a property
#for space in spaces: 
 #  print (space.LongName)
   
for space in spaces:
    for definition in space.IsDefinedBy:
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            #print(property_set.Name)
            
        if property_set.Name == "PSet_Revit_Dimensions":
            for property in property_set.HasProperties:
                if property.Name == "Area":
                    print(property.NominalValue, space.LongName)
                
         
    