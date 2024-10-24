import csv
import sys
import doctest

#==================================================================================================


#Define function
def is_an_oak(name):
    """
    For a given string, checks whether or not it starts with 'quercus'

    Args:
        name (str): The genus name to check 

    Returns: 
        bool: True if starts with 'quercus', false otherwise.
    """

    """
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
    name = name.lower()
    return name.startswith('quercus') and (len(name) == len('quercus') or name[len('quercus')] == ' ')
    #checks name starts with 'quercus'
    #also checks if the name is 'quercus' exactly or the character after 'quercus' is a space
    
 #==================================================================================================


def main(argv): 
    """
    Runs is_an_oak on each of the non-header rows.

    Returns:
        int: 0 on success, non-0 on failure
    """


    f = open('../data/TestOaksData.csv','r')
    g = open('../results/oaks_debugme_results.csv','w')
    taxa = csv.reader(f)    
    csvwrite = csv.writer(g)
    oaks = set() #oaks will be a set of unique species


#skip the first row if it is 'genus' and 'species'
#if this is true, then write the first row to the results file
#if it is false, then still write 'genus' and 'species' to the results file 
    header = next(taxa)
    if header[0].strip().lower() == 'genus' and header[1].strip().lower() == 'species':
        print("Skipping header row...")
        csvwrite.writerow(header)
    else:
        taxa = [header] + list(taxa)
        header = ["Genus", " species"]
        csvwrite.writerow(header)
    
#goes through each (remaining) row and runs is_an_oak on it; if it returns true, then write the row to the results file
    for row in taxa:
        print(row)
        print ("The genus is: ", row[0]) 

        if is_an_oak(row[0]):
            rowfullname = row[0] + " " + row[1]
            if rowfullname not in oaks: #prevents duplicate oak species from showing up
                print(rowfullname, " is an oak! \n")
                csvwrite.writerow([row[0], row[1]])
                oaks.add(rowfullname) 
        else:
            rowfullname = row[0] + " " + row[1]
            print(rowfullname, "is not an oak! \n")    

    return 0

#==================================================================================================
    
if __name__ == "__main__":
    """Makes sure the "main" function is called from the command line"""
    import doctest
    doctest.testmod()
    status = main(sys.argv)
    sys.exit(status)






