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

def plotCountry(data,country,range):

    countryFrame = data[data["Country/Region"] == country]

    plotDataX = []
    plotDataY = []
    
    #The first four columns in the dataframe are ['Province/State', 'Country/Region', 'Lat', 'Long']
    for date in list(data.columns.values)[(4+(len(list(data.columns.values))-range)):]:
        plotDataX.append(date)
        plotDataY.append(sum(countryFrame[date]))
    
    #fig, ax = plt.subplots()
    #ax.plot(plotDataX,plotDataY)
    #ax.xaxis_date()
    #fig.autofmt_xdate()
    plt.plot(plotDataX,plotDataY)
    plt.xticks(plotDataX[::30])
    plt.show()

def printStats(country,data):

    countryFrame = data[data["Country/Region"] == country]

    return countryFrame
    

def executeCommand(data,command,country,range):

    if command == 'list countries':
        print(list(data["Country/Region"]))

    elif command == 'plot':
        if country.capitalize() not in list(data['Country/Region']):
            print ("invalid argument for 'plot' command '" + country + "' is not a country")
        else:
            plotCountry(data,country,range)

    else:
        print("Command not recognised. The available commands are:")
        print("list: return a list of countries that are in the database")





    '''
    if len(command) != 0:
        print(command)

        if command[0] == 'help':
            print ("The currently implemented commands are:")
            print ("plot <country>: plot the cases in a country up to a specifc date")
            print ("countries: list all countries that are in the database")
        

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
'''
###     Main

def main(args):
    """ Main program """
    # Code goes over here.

    covidData = acquireData(DATA_URL)

    print(args.command)

    ### Main Logic for executing commands:

    if args.command == 'list countries':
        print(list(covidData["Country/Region"]))

    elif args.command == 'plot':
        if args.country.capitalize() not in list(covidData['Country/Region']):
            print ("invalid argument for 'plot' command '" + args.country + "' is not a country")
        else:
            plotCountry(covidData,args.country,range)

    else:
        print("Command not recognised. The available commands are:")
        print("list: return a list of countries that are in the database")

    return None

#test commits:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool for examining Covid statistics')

    parser.add_argument(dest    = 'command',
                        type    = str,
                        help    = 'The command sent to the program')


    parser.add_argument('--country',
                        type    = str,
                        help    = 'the country that the specific command will work with')

    parser.add_argument('--range',
                        type    = int,
                        help    = 'The number of datapoints that you want to use. The operation will be done on the most recent day, and up to range number of days before the most recent day',
                        default = 0)     

    main(parser.parse_args())

    

#if __name__ == "__main__":
#   return main()

#Useful notes:

#How to access a  list of countries in the dataset:
#    data['Country/Region']

#Get all rows that have items of the specific name: data[data["Country/Region"]=="France"]

#Get all the headers of the columns:
#list(test.columns.values)