#!/usr/bin/env python

###   Constants

DATA_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

###   Imports

import pandas
import matplotlib.pyplot as plt
import csv
import argparse

###   Functions


def acquireData(dataSource):
    data = pandas.read_csv(DATA_URL)
    return data

def returnCountries(data):
    return data['Country/Region']

def plotCountry(country,data):

    countryFrame = data[data["Country/Region"] == country]

    plotDataX = []
    plotDataY = []
    
    #The first four columns in the dataframe are ['Province/State', 'Country/Region', 'Lat', 'Long']
    for date in list(data.columns.values)[4:]:
        plotDataX.append(date[:-3])
        plotDataY.append(sum(countryFrame[date]))
    
    plt.plot(plotDataX,plotDataY)
    plt.show()

def printStats(country,data):

    countryFrame = data[data["Country/Region"] == country]

    return countryFrame
    

def executeCommand(command,data):
    command = command.lower()
    command = command.split()
    if len(command) != 0:
        print(command)

        if command[0] == 'help':
            print ("The currently implemented commands are:")
            print ("exit: exit the program")
            print ("plot <country>: plot the cases in a country up to a specifc date")
            print ("countries: list all countries that are in the database")
        
        elif command[0] == 'exit':
            return False

        elif command[0] == 'list':
            print (list(data.columns.values))
        
        elif command[0] == 'plot':

            if command[1].capitalize() not in list(data['Country/Region']):
                print ("invalid argument for 'plot' command")
            else:
                plotCountry(command[1].capitalize(),data)

        elif command[0] == 'countries':
            print(returnCountries(data))
        
        elif command[0] == 'stats':

            if command[1].capitalize() not in list(data['Country/Region']):
                print ("invalid argument for 'stats' command")

            else:
                printStats(command[1].capitalize(),data)
        else:
            print ("ERROR: command not recognized.")
            print ("Type 'help' to get a list of commands")
    else:
        print("No command was entered")

###     Main

def main():
    """ Main program """
    # Code goes over here.

    covidData = acquireData(DATA_URL)

    while(True):

        print('Please enter a command:')
        command = input()
        if executeCommand(command,covidData) == False:
            break

    test = 1
    return main

#test commits:

main()

#if __name__ == "__main__":
#   return main()

#Useful notes:

#How to access a  list of countries in the dataset:
#    data['Country/Region']

#Get all rows that have items of the specific name: data[data["Country/Region"]=="France"]

#Get all the headers of the columns:
#list(test.columns.values)