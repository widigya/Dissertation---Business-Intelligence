#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to create core ETL process

def cleandata(filename, count):
    
    import csv
    import geomaps

    #declare variables
    numbers = []
    employs = []
    names = []
    stats = []
    addrs1 = []
    addrs2 = []
    addrs3 = []
    addrs4 = []
    cities = []
    poboxes = []
    webs = []
    turns = []
    assets = []
    newmdata = 'master_data_extract.csv'

    #open sample csv document and assign variables
    f = open(filename,'rU')
    csv_f = csv.reader(f)
    csv_f.next()
    for row in csv_f:

        number = row[0]
        name = row[2]

        if isinstance(row[17], str):
            employ = row[17]
        else:
            employ = int(row[17])

        stat = row[19]
        addr1 = row[21]
        addr2 = row[22]
        addr3 = row[23]
        addr4 = row[24]

        if row[24]:
            city = row[23]
            addr1 = row[21]
            addr2 = row[22]
            addr3 = row[23]
            addr4 = row[24]
        elif row[23]:
            city = row[22]
            addr1 = row[21]
            addr2 = row[22]
            addr3 = row[23]
            addr4 = None
        elif row[22]:
            city = row[21]
            addr1 = row[21]
            addr2 = row[22]
            addr3 = None
            addr4 = None
    
        pobox = row[25]
        web = row[33]

        if isinstance(row[43], str) and isinstance(row[44], str):
            turn = row[43]
            asset = row[44]
        else:
            turn = int(row[43])
            asset = int(row[44])

        #selecting companies with complete attributes
        if employ and web :
            if isinstance(turn, str) and isinstance(asset, str) :
                if turn != '0' or asset != '0' :
                
                    numbers.append(number)
                    names.append(name)
                    employs.append(employ)
                    stats.append(stat)
                    addrs1.append(addr1)
                    addrs2.append(addr2)
                    addrs3.append(addr3)
                    addrs4.append(addr4)
                    cities.append(city)
                    poboxes.append(pobox)
                    webs.append(web)
                    turns.append(turn)
                    assets.append(asset)
        
    f.close()
          
    #transpose data
    mdata_r = ([numbers, names, employs, stats, addrs1, addrs2, addrs3, addrs4,
                 cities, poboxes, webs, turns, assets])
        
    mdata = [[mdata_r[j][i] for j in range(len(mdata_r))] for i in range(len(mdata_r[0]))]

    if count < 1:
        #write to new csv documents
        #master data (company, city, postcode, status)
        gmas = open(newmdata,'wb')
        csv_gmas = csv.writer(gmas)
        for row in mdata:
            csv_gmas.writerow(row)
        gmas.close()

        #remove duplicate entry
        rows = open(newmdata).read().split('\n')
        newrows = []
        for row in rows:
            if row not in newrows:
                newrows.append(row)
        f = open(newmdata, 'w')
        f.write('\n'.join(newrows))
        f.close()

    else:
        #write to new csv documents
        #master data (company, city, postcode, status)
        gmas = open(newmdata,'a')
        csv_gmas = csv.writer(gmas)
        for row in mdata:
            csv_gmas.writerow(row)
        gmas.close()

        #remove duplicate entry
        rows = open(newmdata).read().split('\n')
        newrows = []
        for row in rows:
            if row not in newrows:
                newrows.append(row)
        f = open(newmdata, 'w')
        f.write('\n'.join(newrows))
        f.close()
    
    return count, newmdata

#end of line
