uang = int(input("Berapa uang kamu?"))
utang = 100000

if uang < utang:
    print("Belum bisa bayar hutang")
elif uang == utang:
    print("Pas-pasan bayar hutang")
else:
    print("Bisa bayar hutang")