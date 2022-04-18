import json

sampel_page = { "page": { "url": "url1", "update_time": "1415387875"}, "other_key": {} }
'''mycountries = json.load(open('./data/countries-data.json'))
jtopy=json.dumps(mycountries) #json.dumps take a dictionary as input and returns a string as output.'''

with open('./data/obama_speech.txt', 'r') as f:
  lines = f.read().splitlines()
  total_wc =0
  tl = 0
  for line in lines:
    wc = line.split()
    total_wc += len(wc)
    tl += 1
  print(f'Total number of words {total_wc} and total lines {tl}')


def most_spoken_langugages(filename='./data/countries_data.json', n = 10):
  '''
    sort() -> returns a list 
  '''
  with open('./data/countries-data.json','r') as f:
    countries_dict = json.load(f)
    language_dict = dict()
    for country in countries_dict:
      language_list = country['languages']
      for lang in language_list:
        if lang not in language_dict:
          language_dict[lang] = 1
        else:
          language_dict[lang] +=1
  new_dict = dict(zip(language_dict.values(), language_dict.keys()))
  new_dict = sorted(new_dict.items() , reverse = True)
  print(new_dict[:n])
    
most_spoken_langugages('./data/countries_data.json',3)
  


