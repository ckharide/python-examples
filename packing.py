def sum_numbers(*numlist):
    sum = 0
    try :
      for i in numlist:
        sum +=i
    except TypeError as e:
        print('Exception')
    return sum

print(sum_numbers(1,2,3,4,5))

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*first , fu , eng = names
print(first)
print(eng)

lang = ["Finnish" , 'Sweedish' , 'Nords'] 

country_lang = []
for c , l in zip(names, lang):
    country_lang.append({'country' : c , 'language' : l})

print(country_lang)

for i in country_lang:
    print(i)