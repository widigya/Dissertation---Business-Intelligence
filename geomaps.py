#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to do geocoding with Google Maps

def getlatlong(filename):

    import csv
    import time
    from pygeocoder import Geocoder
    from pygeolib import GeocoderError
    
    #declare variables
    lat = []
    lng = []
    numbers = []
    employs = []
    employ2 = []
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
    turn2 = []
    assets = []
    asset2 = []
    size = []
    x = 0
    n = 'N/A'
    a = 'N/A'
    newlatlngdata = 'master_data_transform.csv'

    #open location data csv
    geo = open(filename)
    csv_geo = csv.reader(geo)
    csv_geo.next()
    for row in csv_geo:
        
        number = row[0]
        name = row[1]
        employ = row[2]
        stat = row[3]
        addr1 = row[4]
        addr2 = row[5]
        addr3 = row[6]
        addr4 = row[7]
        city = row[8]
        pobox = row[9]
        web = row[10]
        turn = row[11]
        asset = row[12]
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

        try:
            results = Geocoder.geocode(row[9])
        except GeocoderError:
            lat.insert(x,n)
            lng.insert(x,a)
        else:    
            location = results[0].coordinates
            lat.insert(x,location[0])
            lng.insert(x,location[1])
        time.sleep(0.2)
        x = x+1
  
    geo.close()
    
    for j in range(len(employs)):
        try:
            employ1 = int(employs[j])
            turn1 = int(turns[j])
            asset1 = int(assets[j])
        except ValueError:
            employ1 = 0
            turn1 = 0
            asset1 = 0
            
        employ2.append(employ1)
        turn2.append(turn1)
        asset2.append(asset1)

        if (employ2[j] > 250 and turn2[j] > 41000000):
            size.append("Large")
        elif (employ2[j] > 250 and asset2[j] > 35200000):
            size.append("Large")
        elif (employ2[j] > 250 and turn2[j] > 41000000 and asset2[j] > 35200000):
            size.append("Large")
            
        elif ((employ2[j] <= 250 and employ2[j] > 50) and (turn2[j] <=  41000000 and turn2[j] > 8200000)):
            size.append("Medium")
        elif ((employ2[j] <= 250 and employ2[j] > 50) and (asset2[j] <=  35200000 and asset2[j] > 8200000)):
            size.append("Medium")
        elif ((employ2[j] <= 250 and employ2[j] > 50) and (turn2[j] <=  41000000 and turn2[j] > 8200000) and (asset2[j] <=  35200000 and asset2[j] > 8200000)):
            size.append("Medium")
            
        elif ((employ2[j] <= 50 and employ2[j] > 10) and (turn2[j] <=  8200000 and turn2[j] > 1700000)):
            size.append("Small")
        elif ((employ2[j] <= 50 and employ2[j] > 10) and (asset2[j] <=  8200000 and asset2[j] > 1700000)):
            size.append("Small")
        elif ((employ2[j] <= 50 and employ2[j] > 10) and (turn2[j] <=  8200000 and turn2[j] > 1700000) and (asset2[j] <=  8200000 and asset2[j] > 1700000)):
            size.append("Small")
            
        elif ((employ2[j] <= 10 and employ2[j] > 0) and (turn2[j] <=  1700000 and turn2[j] > 0)):
            size.append("Micro")
        elif ((employ2[j] <= 10 and employ2[j] > 0) and (asset2[j] <=  1700000 and asset2[j] > 0)):
            size.append("Micro")
        elif ((employ2[j] <= 10 and employ2[j] > 0) and (turn2[j] <=  1700000 and turn2[j] > 0) and (asset2[j] <=  1700000 and asset2[j] > 0)):
            size.append("Micro")
            
        else:
            size.append("N/A")

    #mdata_r = ([numbers, employs, names, stats, addrs1, addrs2, addrs3,
    #            cities, counties, regs, countries, poboxes, webs,
    #            type1sics, type1s, turns, assets, size])

    mdata_r = ([names, numbers, employs, stats, addrs1, addrs2, addrs3, addrs4, cities, poboxes, webs, turns, assets, size, lat, lng])
            
    mdata = [[mdata_r[j][i] for j in range(len(mdata_r))] for i in range(len(mdata_r[0]))]
            
    #write to new csv documents the latitude and longitude data
    header = (["Name", "Companies House ID", "No. of Employee", "Status", "Address1", "Address2", "Address3", "Address4", "City", "Postcode", "Web Address", "Turnover", "Total Assets", "Company Size", "Latitude", "Longitude"])

    gmas = open(newlatlngdata,'wb')
    csv_gmas = csv.writer(gmas)
    csv_gmas.writerow(header)
    for row in mdata:
        csv_gmas.writerow(row)
    gmas.close()

#end of line
    

    
