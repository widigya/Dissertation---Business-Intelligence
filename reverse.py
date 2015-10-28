#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to reverse cleaned sorted data

def reversedata(filename):

    import csv
    import link

    counter = 0
    counter2 = 0
    filename2 = "tags_cleaned.csv"

    #open csv files, get url into array
    geo = open(filename, 'rU')
    csv_geo = csv.reader(geo)
    headers = csv_geo.next()
    
    f = open(filename2, 'wb')
    csv_f = csv.writer(f)
    csv_f.writerow(headers)
    f.close()
    
    #edit csv
    geo2 = open(filename, 'rU')
    csv_geo2 = csv.reader(geo2)
    csv_geo2.next()
    for row in csv_geo2:
        if counter > 0:
            counter = counter + 1
            temp2 = row
            if temp2[0] == temp[0]:
                counter2 = counter2 + 1
                if len(temp) == len(temp2):
                    for l in range(len(temp)):
                        if temp[l] in temp2:
                            continue
                        else:
                            temp2.append(temp[l])
                    if counter2 == 0:
                        link.writelink(temp2, filename2)
                    else:
                        pass
                counter2 = 0
            elif temp2[0] != temp[0]:
                link.writelink(temp, filename2)
            temp = temp2
        else:
            counter = counter + 1
            temp = row
    geo2.close()

    tcounter = counter
    counter = 0

    #second editing
    geo2 = open(filename, 'rU')
    csv_geo2 = csv.reader(geo2)
    csv_geo2.next()
    for row in csv_geo2:
        counter = counter + 1
        if counter == (tcounter - 1):
            temp2 = row
        elif counter == tcounter:
            temp = row
            if temp2[0] == temp[0]:
                counter2 = counter2 + 1
                if len(temp) == len(temp2):
                    for l in range(len(temp)):
                        if temp[l] in temp2:
                            continue
                        else:
                            temp2.append(temp[l])
                    if counter2 == 0:
                        link.writelink(temp2, filename2)
                    else:
                        pass
                counter2 = 0
            elif temp2[0] != temp[0]:
                link.writelink(temp, filename2)
    geo2.close()

#end of line

