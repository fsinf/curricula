#!/usr/bin/env python3
import glob
from pathlib import Path
import json

import yaml

JSON_DIR = Path('json')
JSON_DIR.mkdir(exist_ok=True)

curriculums = []

def add_ids(data):
	for subject in data['subjects']:
		for module in subject['modules']:
			for course in module['courses']:
				course['id'] = '{:0.1f} {}'.format(course['ects'], course['name'])
	return data

for filename in glob.glob('*-curricula.yml'):
	with open(filename) as src:
		data = add_ids(yaml.safe_load(src))

	data['transitions'] = []

	code = filename.split('-')[0]
	data['code'] = code

	for transition in glob.glob(code + '-transition-*.yml'):
		with open(transition) as f:
			data['transitions'].append(yaml.safe_load(f))

	outname = code + '.json'
	with JSON_DIR.joinpath(outname).open('w') as f:
		json.dump(data, f)

	curriculums.append(dict(name=data['name'],  type=data['type'], href=outname, code=code))

with JSON_DIR.joinpath('index.json').open('w') as f:
	json.dump(curriculums, f)
