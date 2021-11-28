#!/bin/python3

# import pandas as pd
# 
# df = pd.read_csv("./species.csv", error_bad_lines=False, delimiter='\t', encoding='iso-8859-1')
# 
# print(df.keys())


fd = open("./toto", "r")

file = fd.read()

a = file.split()

for elem in a:
    if "-" in elem:
        print()
        continue
    print(elem + ", " , end = '')

fd.close()