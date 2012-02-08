import json, ast
from pprint import pprint
a = open("msa2005.json").read()
data = ast.literal_eval(a)
fips = []
gdp, gdp_res = [], []
crime, crime_res = [], []
income, income_res = [], []
patents, patents_res = [], []
state, msaname = [], []
url, latlong = [], []
pop = []

msadata = {}
for j, i in data.items():
	fips = fips + [i.get("FIPS", "NA")]
	gdp = gdp + [i.get("GDP", "NA")]
	gdp_res = gdp_res + [i.get("GDP-residual", "NA")]
	crime = crime + [i.get("crime", "NA")]
	crime_res = crime_res + [i.get("crime-residual", "NA")]
	income = income + [i.get("income", "NA")]
	income_res = income_res + [i.get("income-residual", "NA")]
	patents = patents + [i.get("patents", "NA")]
	patents_res = patents_res + [i.get("patents-residual", "NA")]
	state = state + [i.get("state", "NA")]
	latlong = latlong + [i.get("latLng", "NA")]
	url = url + [i.get("URL", "NA")]
	pop = pop + [i.get("population", "NA")]
	msaname.append(i["longname"])
	
msadata["name"]=msaname
msadata["FIPS"]=fips
msadata["population"]=pop
msadata["state"]=state
msadata["latlong"]=latlong
msadata["url"]=url
msadata["GDP"]=gdp
msadata["GDP_res"]=gdp_res
msadata["crime"]=crime
msadata["crime_res"]=crime_res
msadata["income"]=income
msadata["income_res"]=income_res
msadata["patents"]=patents
msadata["patents_res"]=patents_res

print json.dumps(msadata)
