from xml.dom.minidom import parse
filename = "employees.xml"
doc = parse(filename)
# print(doc.toprettyxml(),end='')
# !!!! don't works!!!!!

# get elements as list
emloyeeNodeList = doc.getElementsByTagName("Employee")
print(len(emloyeeNodeList))
for employeeNode in emloyeeNodeList:

# get elements first name
firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)

# get text NODE and it's value
firstName = firstNameNode.firstChild.nodeValue.strip()
print (firstName)