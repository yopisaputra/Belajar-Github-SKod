data = {1:{'name': 'Yopi', 'age': 23, 'hobby':'singing'},
        2:{'name': 'Putra', 'age': 20, 'hobby':'sleeping'},
        3:{'name': 'Santi', 'age': 21, 'hobby':'eating'}}

# print(data[2]['name'])

for key, value in data.items():
    print("\nKey : ", key)

    for key2 in value:
        print(key2 + ":" + str(value[key2]))