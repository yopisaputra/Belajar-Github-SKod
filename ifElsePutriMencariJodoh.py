"""
Putri Raja Mencari Jodoh
"""

tamu = "biner"
baik = True
rajin = True

if baik & rajin & (tamu == "pria"):
    print("Cocok")
elif baik & rajin & (tamu != "pria"):
    print("Sodaraan Aja")
else:
    print("Tidak Cocok")