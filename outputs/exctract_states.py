import json


with open('all_aus_postcodes.json', 'r') as fh:
	jd = json.load(fh)

states = ['nsw', 'qld', 'vic']

for state in states:
	codes = sorted([pc['postcode'] for pc in jd if pc['state'].lower() == state])
	with open(state+'.json', 'w') as outfile:
		json.dump(codes, outfile)
	print state
	print codes