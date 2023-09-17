

player1 = {"name": "Yopi",
           "power": 4000}
player2 = {"name": "Putra",
           "power": 3500}

def trainPlayer(player):
    # player["power"] = player["power"] + 500
    player["power"] += 1000


def attackPlayer(attacker, defender):
    if(attacker["power"] > defender["power"]):
        print("Serangan berhasil! selamat untuk ", attacker["name"])
    else:
        print("serangan gagal! kamu lemah", attacker["name"])


trainPlayer(player2)
attackPlayer(player1, player2)