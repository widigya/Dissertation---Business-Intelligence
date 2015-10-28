#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to sort and cleanse keywords

def sortandcleansekeywords(filename, filename2):

    import csv
    import link
    import remove

    btypes = []
    btypes2 = []
    headers = []
    keys = []
    companies = []
    rows = []
    counter = 0
    counter2 = 0
    filename3 = "industry_type_sorted.csv"
    filename4 = "industry_type_sorted_&_cleaned.csv"

    #open csv files, get url into array
    geo = open(filename2, 'rU')
    csv_geo = csv.reader(geo)
    layers = csv_geo.next()

    for k in range(len(layers)):
        header = "Business Type" + str(k)
        headers.append(header)
    headers.insert(0, "Company Name")

    #part one
    #create tags csv file
    f = open(filename, 'wb')
    csv_f = csv.writer(f)
    csv_f.writerow(headers)
    f.close()
    
    for row in csv_geo:
        
        tags = row
        for i, col in enumerate(row):
            if col.isdigit() == True:
                btype = layers[i]
            else:
                continue
            btypes.append(btype)
        btypes.insert(0, row[0])

        if len(tags) == len(btypes):
            for j in range(len(tags)):
                if tags[j] == "1":
                    btype = btypes[j]
                else:
                    continue
                btypes2.append(btype)
        else:
            btype = "N/A"
            btypes2.append(btype)

        btypes2.insert(0, row[0])
        link.writelink(btypes2, filename)
        btypes = []
        btypes2 = []
        
    geo.close()

    f = open(filename3, 'wb')
    csv_f = csv.writer(f)
    csv_f.writerow(headers)
    f.close()

    #part two
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
                        link.writelink(temp2, filename3)
                    else:
                        pass
                counter2 = 0
            elif temp2[0] != temp[0]:
                link.writelink(temp, filename3)
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
                        link.writelink(temp2, filename3)
                    else:
                        pass
                counter2 = 0
            elif temp2[0] != temp[0]:
                link.writelink(temp, filename3)
    geo2.close()

    #part three
    crm = "customer relationship management"
    erp = "entreprise resource planning"
    ba = "business analytics"

    f = open(filename4, 'wb')
    csv_f = csv.writer(f)
    csv_f.writerow(headers)
    f.close()
    
    #third editing
    geo2 = open(filename3, 'rU')
    csv_geo2 = csv.reader(geo2)
    csv_geo2.next()
    for row in csv_geo2:

        temp = row
        for m in range(len(temp)):
            if temp[m] == crm :
                temp[m] = "crm"
            elif temp[m] == erp :
                temp[m] = "erp"
            elif temp[m] == ba :
                temp[m] = "analytics"
            else:
                pass
        temp = remove.removeduplicates(temp)
        link.writelink(temp, filename4)
        
    geo2.close()

    return filename4

#end of line
    
