#!/usr/bin/env python3

"""
A Python script that finds oak in a given .csv file.

It contains two functions, one that returns `True` if the genus is exactly 'quercus'.
Another function that finds oaks and prints them into a new csv file.
"""

__author__ = 'Yibin.Li Yibin.Li24@imperial.ac.uk'
__version__ = '0.0.1'

import csv
import sys
import doctest



#Define function that identify whether the oaks in the dataset
def is_an_oak(name):
    """ 
    Returns True if name starts with 'quercus' 
    >>> is_an_oak('Fagus sylvatica')
    False
    >>> is_an_oak('Quercus robur')
    True
    >>> is_an_oak('quercus ROBUR')
    True
    >>> is_an_oak('Quercuss robur')
    False
    >>> is_an_oak('Quercus')
    True
    >>> is_an_oak(' Quercus robur')
    False
    """

    # Extract the genus name (first word)
    name = name.lower()

    # Handle minor typos in genus name
    return name.startswith('quercus') and (len(name) == len('quercus') or name[len('quercus')] == ' ')



def main(argv): 
    """
    Find oaks and prints them into a new csv file.
    """
# open csv files to read and save the results
    f = open('../data/TestOaksData.csv','r')
    g = open('../results/oaks_debugme_results.csv','w')
    taxa = csv.reader(f)    
    csvwrite = csv.writer(g)
    oaks = set() #oaks will be a set of unique species


#skip the first row if it is 'genus' and 'species'
    header = next(taxa)
    if header[0].strip().lower() == 'genus' and header[1].strip().lower() == 'species':
        print("Skipping header row...")
        csvwrite.writerow(header)

# add header to new csv file    
    else:
        taxa = [header] + list(taxa)
        header = ["Genus", " species"]
        csvwrite.writerow(header)
    
#goes through each (remaining) row and runs function on it
    for row in taxa:
        print(row)
        print ("The genus is: ", row[0])

# adds oaks to result file
        if is_an_oak(row[0]):
            rowfullname = row[0] + " " + row[1]
            if rowfullname not in oaks: 
                print(rowfullname, " is an oak! \n")
                csvwrite.writerow([row[0], row[1]])
                oaks.add(rowfullname) 
        else:
            rowfullname = row[0] + " " + row[1]
            print(rowfullname, "is not an oak! \n")    

    return 0

if __name__ == "__main__":
    """
    Makes sure the "main" function is called from the command line
    """
    import doctest
    doctest.testmod()
    status = main(sys.argv)
    sys.exit(status)