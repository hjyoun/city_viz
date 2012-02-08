import json, ast
from pprint import pprint
a = open("gmp2.js").read().replace('\n','').replace('  ','')
gmp = ast.literal_eval(a)
a = open("income2.js").read().replace('\n','').replace('  ','')
income = ast.literal_eval(a)
a = open("patents2.js").read().replace('\n','').replace('  ','')
patens = ast.literal_eval(a)
a = open("violent_crime2.js").read().replace('\n','').replace('  ','')
crime = ast.literal_eval(a)

msas = {}
for i in gmp: 
	if '2005' not in i['label']: continue
	msas[i['FIPS']]=i
for i in income: 
	if '2005' not in i['label']: continue
	msas[i['FIPS']]['income'] = i['income']
	msas[i['FIPS']]['income-residual'] = i['income-residual']

for i in patens:
	if '2005' not in i['label']: continue
	msas[i['FIPS']]['patents'] = i['patents']
	msas[i['FIPS']]['patents-residual'] = i['patents-residual']

for i in crime:
	if '2005' not in i['label']: continue
	msas[i['FIPS']]['crime'] = i['crime']
	msas[i['FIPS']]['crime-residual'] = i['crime-residual']

print json.dumps(msas)
