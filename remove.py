#!/usr/bin/env python
#Author: Alam Widigya (alam.widigya@kcl.ac.uk)
#Description: Python script to remove duplicates

def removeduplicates(values):

    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    
    return output

#end of line
