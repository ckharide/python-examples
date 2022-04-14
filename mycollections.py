dog = {}
print(dict)
dog = {'name' : 'x', 'color' : 'white' , 'breed' : 'alseacian'  }

student  = {
    'name' :'Chandra',
    'age' : 40,
    'gender' : 'm',
    'martialstatus' : 'married',
    'skills' :['Technogoyc , Management']
}

print("Clas name of skills")
print(type(student['skills']))

print(student.keys())
print("post deletion")
student.pop('age')

print(student.keys())

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Denmark' in nordic_countries)

veg_tp = ('carrot' , 'brinjal' , 'cauli')
fruits = ('apple' , 'mango')
animals = ('milk' , 'butter' ,'cheese')
food_tp = animals + veg_tp + fruits
print(food_tp)