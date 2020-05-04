#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import json

def handle_group(el, courses):
	data = el.attrib
	if 'minEcts' in data:
		data['minEcts'] = float(data['minEcts'])
	if 'maxEctsWithout' in data:
		data['maxEctsWithout'] = float(data['maxEctsWithout'])

	if 'required' in data:
		data['required'] = data['required'] in ('true', '1')

	if el.findall('group'):
		data['groups'] = [handle_group(group, courses) for group in el.findall('group')]
	else:
		data['courses'] = [c.get('name') for c in el.findall('cref')]
	return data

def handle_course(el, semester_recommendations):
	data = dict(
		name=el.get('name'),
		ects=float(el.get('ects')),
	)
	for idx, semester in enumerate(semester_recommendations, 1):
		if data['name'] in semester:
			data['semesterRecommendation'] = idx
			break
	return data

def handle_curriculum(el):
	data = el.attrib
	data['semesterRecommendation'] = [[c.get('name') for c in s] for s in el.find('semester-recommendation')]
	data['courses'] = {c.get('name'): handle_course(c, data['semesterRecommendation']) for c in el.find('courses')}
	data['group'] = handle_group(el.find('group'), data['courses'])
	data['constraints'] = [handle_group(g, data['courses']) for g in el.find('constraints')]
	return data

curricula = ET.parse('index.xml').getroot()

for curriculum in curricula:
	with open(curriculum.get('code') + '.json', 'w') as f:
		json.dump(handle_curriculum(ET.parse(curriculum.get('code') + '.xml').getroot()), f)

with open('index.json', 'w') as f:
	json.dump([el.attrib for el in curricula], f)
