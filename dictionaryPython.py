data = {'name' : 'Yopi',
        'age' : 23,
        'hobby' : 'reading'}


data['name'] = 'Jackson'
data['dream'] = 'singer'

# del data['age']

# print(data['dream'])
# print(data)


for key, value in data.items():
    print(key + ":" + str(value) + "\n")