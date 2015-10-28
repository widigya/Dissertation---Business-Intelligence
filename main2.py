#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script for finding industry type

import tagging
import words

filename = "master_data_transform.csv"
filename2 = "keywords_urls.csv"
filename3 = "keywords_tags.csv"
newmdata = "sample_urls.csv"

tagging.search(filename, filename2, newmdata)
words.keywords(filename, filename3, newmdata)

#end of line


