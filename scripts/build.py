#!/usr/bin/env python3
import xml.etree.ElementTree as ET
import json
import html
import glob

import markdown

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

curricula = []

for filename in glob.glob('*.xml'):
	print(filename)
	root = ET.parse(filename).getroot()
	if root.tag == 'curriculum':
		data = handle_curriculum(root)
		with open(data['code'] + '.json', 'w') as f:
			json.dump(data, f)
		curricula.append(data)
	else:
		print('unhandled root', filename)

curricula.sort(key=lambda c: c['code'])

with open('index.json', 'w') as f:
	json.dump([dict(name=c['name'], code=c['code']) for c in curricula], f)

with open('index.xml', 'w') as f:
	f.write('<curricula>')
	for c in curricula:
		f.write('<curriculum code="{}" name="{}"/>'.format(c['code'], html.escape(c['name'])))
	f.write('</curricula>')

with open('index.html', 'w') as f:
	table = '<table><tr><th>Code</th><th>Name</th><th>Links</th></tr>'
	for c in curricula:
		code = c.get('code')
		table += "<tr><td>{code}</td><td>{name}</td>".format(code=code, name=html.escape(c.get('name')))
		table += '<td><a href="{pdf}">PDF</a> <a href="{code}.xml">XML</a> <a href="{code}.json">JSON</a></td></tr>'.format(pdf=c["source"], code=code)
	table += '</table><script src="api.js"></script>'

	with open('README.md') as readme:
		f.write('<!doctype html><html><head>')
		f.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
		f.write('<meta charset=utf-8></head><body>')
		f.write(markdown.markdown(readme.read()).replace('<!--table-->', table))
		f.write('</body></html>')
