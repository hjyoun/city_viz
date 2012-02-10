name2code = {}

for i in open("/Users/visang/Works/EffDensity/EffDensityData/StateNameList.txt"):
    code, name, dummy = i.split()
    name2code[name.lower()] = code

fo = open("/Users/visang/Works/EffDensity/EffDensityData/state_alldata.txt")
fo.readline()
fm = "{"
for i in fo:
    name, nominal, effd1, effd2, effd3 = i.split()[0:5]
    code = name2code[name]
    fm = fm + '"'+code+'":'+nominal+','

fm = fm + '}'
print fm

    

