#!/usr/bin/env python

###   Constants

FILE_LOCATION = 'Data/heart.csv'

###   Imports
import csv

def parseData():
    f = open(FILE_LOCATION, "r")
    data = list(csv.reader(f, delimiter=';'))
    return data

    
    #with open(FILE_LOCATION, 'r') as f:
    #    print(f.read()) 
    #    print ('Hi')


def main():
    """ Main program """
    # Code goes over here.

    heartData = parseData()
    return heartData

if __name__ == "__main__":
    main()