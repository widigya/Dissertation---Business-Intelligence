#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to gather keywords and search into urls

def keywords(filename, filename2, newmdata):

    import csv
    import link
    
    companies = []
    counts = []
    counter = 0
    layers = []
    clayer = []
    urls2 = []
    filename3 = "tags.csv"

    #open csv files, get company into array
    geo = open(filename, 'rU')
    csv_geo = csv.reader(geo)
    csv_geo.next()
    for row in csv_geo:
        company = row[0]
        companies.append(company)
    geo.close()

    #open a csv file with keywords
    geo2 = open(filename2, 'rU')
    csv_geo2 = csv.reader(geo2)
    csv_geo2.next()
    for row in csv_geo2:
        layer = row[0]
        layers.append(layer)
    geo2.close()

    headers = layers
    headers.insert(0, "Company Name")
    
    #print headers
    f = open(filename3, 'wb')
    csv_f = csv.writer(f)
    csv_f.writerow(str(headers))
    f.close()

    #create tags csv file
    f = open(filename3, 'wb')
    csv_f = csv.writer(f)
    csv_f.writerow(headers)
    f.close()

    #open a csv file with keywords
    geo3 = open(newmdata, 'rU')
    csv_geo3 = csv.reader(geo3)
    csv_geo3.next()
    for row in csv_geo3:
        url = row

        if len(url) > 1:
            for j in range(len(url)):
                if j == 0:
                    continue
                for k in range(len(layers)):
                    if counter < 1:
                        count = link.searchlink(url[j], layers[k])
                        clayer2 = count
                        clayer.append(clayer2)
                    elif counter > 0:
                        if clayer[k] == 1:
                            count = 1
                        elif clayer[k] == 0:
                            count = link.searchlink(url[j], layers[k])
                    counts.append(count)
                counts[0] = url[0]                 
                link.writelink(counts, filename3)
                counts = []
                counter = counter + 1
        else:
            for l in range(len(layers)):
                count = "Website not available"
                counts.append(count)

            counts[0] = url[0]                           
            link.writelink(counts, filename3)
            counts = []

        counter = 0
            
    geo3.close()

 #end of line


    
