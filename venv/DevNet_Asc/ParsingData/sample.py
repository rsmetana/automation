import xml.etree.ElementTree as ET

#Get the XML file data
stream = open('sample.xml', 'r')

#Parse the data into the ElementTree object
xml = ET.parse(stream)

#get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root element
for e in root:
    #print the stringifired version of the element
    print(ET.tostring(e))
    print("")
#print the 'ID' attribute of the Element object
    print(e.get("Id"))

