import csv
import numpy as np
np.set_printoptions(suppress=True)

with open('./huizong/hebing2.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)
temp_li = []
for item in result:
    if item[5] != '':
        # temp_li.extend(item[5].split(' '))
        # temp_li = list(set(temp_li))
        temp_li = list(set(temp_li+item[5].split(' ')))



print(temp_li)
print(len(temp_li))