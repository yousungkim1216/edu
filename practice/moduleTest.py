# moduleTest.py

import usecsv, os

os.chdir(r'C:\doit\practice')
a = [['국어', '영어', '수학'], [99, 88, 77]]
usecsv.writecsv('test.csv', a)


