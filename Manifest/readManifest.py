from glob import glob
import xml.etree.ElementTree as ET

def getQuery(f):
	tree = ET.parse(f)
	schema="schema"
	fields, tables=[],[]
	for table in tree.iter('table'):
		tables.append(schema+"."+table.attrib["mysqlcode"])	
		columns=table.findall("field")
		for field in columns:
			fields.append(schema+"."+table.attrib["mysqlcode"] +"." +field.attrib["mysqlcode"])
	query = "select "+",".join(fields) +" from " +",".join(tables)
	print query
	print "-------------"

files = glob("*.xml")
for f in files:
	print f
	getQuery(f)
