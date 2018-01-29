# This script creates in a single directory a same level suite of ##### subdirectories of the following form :
# pre##### where pre is an invariable prefix and ##### is a five digits number progressing by unity from 00001
# to (here) 25000.
# Run it with the command : >>>python3 plha.py

i, j = 25000, 25000
#pre = "/home/ladmin/Téléchargements/PLHA"    # Change the path and cancel the quote 

import os

while i:
    if i > 9999:
        suf = str(i)
    elif i > 999 and i < 10000:
        suf = '0' + str(i)
    elif i > 99 and i < 1000:
        suf = '00' + str(i)
    elif i > 9 and i < 100:
        suf = '000' + str(i)
    elif i < 10:
        suf = '0000' + str(i)
    path = pre + suf
    os.mkdir(path)
    i -=1

print(j, ' directories created')
