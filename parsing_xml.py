#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('DATA/solar.xml')

print(doc)

root = doc.getroot()

print(root)

for element in root:
    if element.tag.endswith('planets'):
        for planet in element:
            print(planet.get('planetname'))
print('-' * 60)

for element in root:
    if element.tag.endswith('planets'):
        for planet in element.findall('planet'):
            print(planet.get('planetname'))
            for moon in planet.findall('moon'):
                print("    {}".format(moon.text))
print('-' * 60)

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print("    {}".format(moon.text))
