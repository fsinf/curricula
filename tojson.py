#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import json

def handle_group(el, courses):
	data = el.attrib
	if 'minEcts' in data:
		data['minEcts'] = float(data['minEcts'])
	if 'maxEctsWithout' in data:
		data['maxEctsWithout'] = float(data['maxEctsWithout'])

	data['required'] = data.get('required') in ('true', '1')

	if el.findall('group'):
		data['groups'] = [handle_group(group, courses) for group in el.findall('group')]
	else:
		data['courses'] = [c.get('name') for c in el.findall('cref')]
	return data

def handle_curriculum(el):
	data = el.attrib
	data['minEcts'] = float(data['minEcts'])
	data['courses'] = {c.get('name'): dict(ects=float(c.get('ects'))) for c in el.find('courses')}
	data['groups'] = [handle_group(group, data['courses']) for group in el.find('groups')]
	data['semesterRecommendation'] = [[c.get('name') for c in s] for s in el.find('semester-recommendation')]
	return data

curricula = ET.parse('index.xml').getroot()

for curriculum in curricula:
	with open(curriculum.get('code') + '.json', 'w') as f:
		json.dump(handle_curriculum(ET.parse(curriculum.get('code') + '.xml').getroot()), f)

with open('index.json', 'w') as f:
	json.dump([el.attrib for el in curricula], f)
