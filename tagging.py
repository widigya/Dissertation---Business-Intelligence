#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to search keywords inside websites

def search(filename, filename2, newmdata):
    
    import csv
    import crawl
    import remove
    import numpy as np

    counter = 0
    companies = []
    webs = []
    words = []
    url = []
    url2 = []
    urls = []
    urls2 = []

    #open csv files, get url into array
    geo = open(filename, 'rU')
    csv_geo = csv.reader(geo)
    csv_geo.next()
    for row in csv_geo:
        company = row[0]
        web = row[10]
        companies.append(company)
        webs.append(web)
    geo.close()
    
    #open a csv file with keywords
    geo2 = open(filename2, 'rU')
    csv_geo2 = csv.reader(geo2)
    csv_geo2.next()
    for row in csv_geo2:
        word = row[0]
        words.append(word)
    geo2.close()

    header = ["Company Name", "URLs"]
        
    #write to new csv document
    gmas = open(newmdata,'wb')
    csv_gmas = csv.writer(gmas)
    csv_gmas.writerow(header)

    for i in range(len(webs)):
        try:
            url = np.array(crawl.scraping(webs[i]))
        except AttributeError:
            pass

        url2 = np.array(remove.removeduplicates(url))
        
        for j in range(len(words)):
            for k in range(len(url2)):
                if words[j] in url2[k]:
                    counter = counter + 1
                    if counter > 1:
                        continue
                    else:
                        urls.append(url2[k])
                else:
                    continue
            counter = 0
        urls.insert(0, companies[i])
        urls2 = remove.removeduplicates(urls)

        #only take the first four entry (for prototyping)
        urls2 = urls2[:4]
                 
        csv_gmas.writerow(urls2)
        url = []
        urls = []
        urls2 = []
    
    gmas.close()

#end of line
