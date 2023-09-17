"""

"""

# def printNama(*args):
#     for name in args:
#         print(name)


# printNama('Yopi', 'Saputra')


def printNama(**kwargs):
    for key, value in kwargs.items():
        print(key + "-" + value)


printNama(name = 'Yopi', age = '21', hoby = 'membaca')