name = input("Nama monter anda: ")

monster = {"name": name,
           "power": 100}

def startGame():
    choice = input("Pilih menu: 1.Makan 2.LihatStatus 3.Keluar ")
    if choice == "1":
        goEat()
    elif choice == "2":
        goStatus()
    else:
        goExit()

def goEat():
    monster["power"] += 100
    print("Nyam...nyam...")
    startGame()

def goStatus():
    print(monster)
    print("Check...check...")
    startGame()

def goExit():
    print("Bye...bye...")


startGame()