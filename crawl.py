#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to crawl through websites

def scraping(curl):

    import urlparse
    import urllib
    import requests
    from bs4 import BeautifulSoup

    url = curl
    urls = [url]
    visited = [url]
    htmltext = 0

    while len(urls) > 0:

        try:
            htmltext = requests.get(urls[0])
        except:
            pass

        soup = BeautifulSoup(htmltext.text, "lxml")

        urls.pop(0)

        for tag in soup.findAll('a', href = True):
            tag['href'] = urlparse.urljoin(url, tag['href'])
            if url in tag['href']:
                visited.append(tag['href'])

    return visited

#end of line


