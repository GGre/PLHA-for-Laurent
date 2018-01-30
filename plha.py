# This script creates in a single directory (here : /home/ladmin/Téléchargements/) a same level suite of ##### subdirectories
# of the following form : pref##### where pref is an invariable prefix and ##### is a five digits number progressing by unity
# from 00001 to (here) 25000.
# Run it with the command : >>>python3 plha.py

i, j = 25000, 25000
#way = "/home/ladmin/Téléchargements/PLHA"    # Change the path to the wished one (see below N.B. 1 & 2)
                                              # Cancel the quote
                                              # N.B. 1: PLHA will be the prefix pref
                                              # N.B. 2: Directories PLHA##### will be created here in
                                              # /home/ladmin/Téléchargements/

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
    path = way + suf
    os.mkdir(path)
    i -=1

print(j, ' directories created')
