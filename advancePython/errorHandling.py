"""
    Exceptions
"""
import sys

name = "Yopi"

# raise Exception("Stop ada kesalahan")

# try:
#     print(i + name)
# except:
#     print("Ada kesalahan dari i + name")

def is_it_linux():
    assert('linux' in sys.platform), "fungsi ini hanya untuk linux"

is_it_linux()
print("finish")