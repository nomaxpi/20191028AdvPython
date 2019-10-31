#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('nasa_rss.xml')

channel = doc.find('channel')
channel_title = channel.findtext('title')
print(channel_title.upper(), '\n')

for item in channel.findall('item'):
    item_title = item.findtext('title')
    print(item_title)
    print()
    item_description = item.findtext('description')
    print(item_description)
    print('-' * 20)

