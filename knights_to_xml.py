#!/usr/bin/env python
import lxml.etree as ET

root = ET.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        e = ET.SubElement(root, 'knight', title=title)
        ET.SubElement(e, 'name').text = name
        ET.SubElement(e, 'color').text = color
        ET.SubElement(e, 'quest').text = quest
        ET.SubElement(e, 'comment').text = comment


print(ET.tostring(root, pretty_print=True, xml_declaration=True).decode())

document = ET.ElementTree(root)
document.write('knights.xml', pretty_print=True, xml_declaration=True)
