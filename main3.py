#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script for finding industry type (part2)

import sort
import join
import reverse

filename = "industry_type.csv"
filename2 = "tags.csv"
filename3 = "keywords.csv"
newmdata = "sample_urls.csv"
master = "master_data_transform.csv"

filename4 = sort.sortandcleansekeywords(filename, filename2)
join.joincsv(master, filename4)
reverse.reversedata(filename2)

#end of line


