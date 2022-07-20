# foreign.py

import usecsv, os, re

total = usecsv.opencsv('popSeoul.csv')
newpop = usecsv.switch(total)

i = newpop[1]



#print(newpop[:4])
