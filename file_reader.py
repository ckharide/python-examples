import json

sampel_page = { "page": { "url": "url1", "update_time": "1415387875"}, "other_key": {} }
'''mycountries = json.load(open('./data/countries-data.json'))
jtopy=json.dumps(mycountries) #json.dumps take a dictionary as input and returns a string as output.'''

with open('./data/countries-data.json', 'r') as f:
  data = json.load(f)
  print(data)

s1 = json.dumps(sampel_page)
d2 = json.loads(s1)
print(d2)