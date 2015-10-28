#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to join csv

def joincsv(csvjoin1, csvjoin2):

    import csv
    from collections import OrderedDict

    with open(csvjoin2, 'rb') as f:
        r = csv.reader(f)
        header2 = r.next()
        header2 = header2[1:]
        dict2 = {row[0]: row[1:] for row in r}
        
    with open(csvjoin1, 'rb') as f:
        r = csv.reader(f)
        header1 = r.next()
        dict1 = OrderedDict((row[0], row[1:]) for row in r)

    header = header1 + header2

    result = OrderedDict()
    for d in (dict1, dict2):
        for key, value in d.iteritems():
            result.setdefault(key, []).extend(value)

    with open('master_data_transform_final.csv', 'wb') as f:
        w = csv.writer(f)
        w.writerow(header)
        for key, value in result.iteritems():
            w.writerow([key] + value)
