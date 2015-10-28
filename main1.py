#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)

import datamanip
import geomaps

#declare variables
count = 0

#file name to be extracted
file = ['TechNation_Part1.csv', 'TechNation_Part2.csv']

for x in range(0, len(file)):

    result1 = datamanip.cleandata(file[x], count)
    count = result1[0]
    count += 1
 
geomaps.getlatlong(result1[1])

#end of line


    




