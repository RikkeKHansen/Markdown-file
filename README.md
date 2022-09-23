# Markdown-file
The mark-down file for the script (group 18)


•	Describe the use case you have chosen
We have choosen to investigate a use case within the Build/Operate topic and focuses mainly on the user phase of the building. 
The use case investigates how BIM can provide ventilation information based on a BIM file in IFC format. 

•	Who is the use case for?
For relevant stakeholders with very little prior knowledge within the ventilation field.  The tool is for actors interested in estimating the air flow rate needed for a low polluted building in the early stages of a building design. The tool is representative for buildings in Denmark and complies with the Danish standards and regulations. The tool requires as a minimum, that all rooms are classified into types and have an area with in the same building being analysed.  

•	What disciplinary (non-BIM) expertise did you use to solve the use case
Python are used in the BIM program to take out relevant information using a script, therefore, a simple knowledge to programming is necessary. Also standards as the danish building code, are nessesary in order to provide the correct estimate.

•	What IFC concepts did you use in your script (would you use in your script)
We are using IFCOpenShell and our use case requires data extractions using the IFC concept: We use the concept of IfcObjectDefinition when reading area. Here we will more specifically look into the type of IFC objects classified as IFCSpaces.
We when use the IfcPropertyDefinition finding the type of room and type of building from the IFC file.
Afterwards we use the concept of IfcRelationship in terms of linking the extracted data to each other. The reason for using relationship is to make sure that spaces are correctly corresponding to the related data.
•	What disciplinary analysis does it require?
Knowledge of ventilation systems, standards and regulations for buildings(DS/EN 13779). Further analysis will also require knowledge of indoor climate quality and occupancy hours. 

•	What building elements are you interested in?
-	Floor area in each room
-	Type of rooms
-	Type of building

•	What (use cases) need to be done before you can start your use case?
The minimum requirements that needs to be done before is a floor plan. The floor plan has to be related to true sizes (=the areas should be m2), so that the area of each room can be found. Also, the rule for using the tool(code) is that the room must be within one unit (The building must be defined as one and cannot be two separate units). 

•	What is the input data for your use case?
Local IFC file for the program to read the informations specified in the file.
Potentially user defined inputs such as building type, occupancy or others.

•	What other use cases are waiting for your use case to complete?
The cost
Code validation
Energy use
LCA
Indoor climate analysis










