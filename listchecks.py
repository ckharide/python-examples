numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
x = [i for i in numbers if i <=0]
print(x)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8]]]
x = [num for row in list_of_lists   for num in row]
print(x)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

concataned = [ y[0] + y[1] for x in names for y in x]
print(concataned)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland' ,'England']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def uppercase_country(country_name):
    return country_name.upper()

uppercasecountrynames = map(uppercase_country,countries)
print(list(uppercasecountrynames))

def filter_land(name):
    if "land" in name:
        return True
    return False

filter_names = filter(filter_land,countries)
print(list(filter_names))

def concate(x,y):
    return x + y

def first_3(countries,k):
    return countries[0:k]

def last_3(countries , k):
    return countries[-k:]

print(first_3(countries,3))
print("First three")
print(last_3(countries,3))
print("last three")


def dict_function(countries):
    mydict = {}
    for x in countries:
       key_name = x[0]
       value = containsfunct(key_name,countries)
       mydict[key_name] = value
    return mydict


def containsfunct(input, country_list):
    list = [ x for x in country_list if x[0] == input]
    return len(list)


myvalues = dict_function(countries)
print(myvalues)

