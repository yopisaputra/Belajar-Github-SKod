name = "Yopi"

def printName():
    global name

    name = name + " saputra"
    print("Akses dari dalam " + name)

printName()

print("akses dari luar " + name)