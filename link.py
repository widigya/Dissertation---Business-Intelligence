#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to search keywords in a url

def searchlink(urls, words):

    import requests
    from socket import error as SocketError

    try:
        site = requests.get(urls)
        sitetext = site.text
        if words in sitetext:
            count = 1
        else:
            count = 0
    except requests.exceptions.ConnectionError:
        count = "This is not the domain we're looking for"
    except requests.exceptions.InvalidSchema:
        count = "No connection adapters were found"
    except requests.exceptions.MissingSchema:
        count = "Invalid URL"
    except requests.exceptions.ReadTimeout:
        count = "Connection timeout"
    except socket.error:
        count = "Connection reset by peer"

    return count

#end of line

def writelink(count, filename):

    import csv

    f = open(filename, 'a')
    csv_f = csv.writer(f)
    csv_f.writerow(count)
    f.close()

#end of line
