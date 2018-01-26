# This script generate in a single directory a suite of subdirectories of the following form :
# {pre}{#####} where {pre} is an invariable prefix and {#####} is a five digits number progressing
# by unity from 00001 to (here) 25000.
# This script shall be ran with the command >>>python3 plha.py

python3

pre, i, j = PLHA, 25001, 0                                          # Prefix, increment, exceptions count

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
    except:
        print('An exception occurs')
        j += 1
        continue

print(i-1-j, ' directories created (', j, ' exception(s) occured)')
