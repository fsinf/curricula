#!/usr/bin/env python3
import lxml.etree
import sys

with open(sys.argv[1], 'rb') as f:
	curriculum = lxml.etree.fromstring(f.read())

def sort_group(group):
	if group.find('group') is None:
		return
	subgroups = sorted(group, key=lambda g: g.get('name'))
	group.getchildren().clear()
	for sg in subgroups:
		group.append(sg)
		sort_group(sg)

sort_group(curriculum.find('group'))

with open(sys.argv[1], 'w') as f:
	f.write(lxml.etree.tostring(curriculum, encoding='unicode') + '\n')
