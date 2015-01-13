#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

def printall (element):
	children = list(element.getchildren())
	if len(children) == 0:
		if element.text == None:
			print element.tag + ':<NONE>'
		else:
			print element.tag + ':' + element.text
	else:
		print element.tag
		children.sort(cmp=lambda x,y:cmp(x.tag, y.tag))
		for child in children:
			printall(element=child)

if len(sys.argv) > 1 :
	dom = ET.parse(sys.argv[1])
else :
	exit

root=dom.getroot()
printall(element=root)