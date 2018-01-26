# This script creates in a single directory a a same level suite suite of ##### subdirectories of the following form :
# pre##### where pre is an invariable prefix and ##### is a five digits number progressing
# by unity from 00001 to (here) 25000.
# Run it with the command : >>>python3 plha.py

pre, i, j, k = PLHA, 25001, 0, 25000                                # Prefix, increment, except count, nbr of waited directories

from os import chdir, mkdir

chdir("/home/bidon/bidon")                                          # Change with the wishing path

while i:
    i -= 1
    try:
        if i < 10000:
            name = pre + '0' + str(i)
        elif i < 1000:
            name = pre + '00' + str(i)
        elif i < 100:
            name = pre + '000' + str(i)
        elif i < 10:
            name = pre + '0000' + str(i)
        mkdir name
    except Exception as err:
        print(err)
        j += 1
        continue

print(k-j, ' directories created (', j, ' exception(s) occured)')   # Final report edition
