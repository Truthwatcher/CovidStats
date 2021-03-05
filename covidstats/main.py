#!/usr/bin/env python

###   Constants

DATA_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

###   Imports

import pandas
import matplotlib.pyplot as plt
import csv
import argparse
import sys

###   Functions


def acquireData(dataSource):
    data = pandas.read_csv(DATA_URL)
    return data

def plotCountry(data,country,province,range):
    ##To do: implement plotting + checking province

    countryFrame = data[data["Country/Region"] == country]

    plotDataX = []
    plotDataY = []
    
    #initialize the plot so other operations can be done
    plt.plot(plotDataX,plotDataY)

    #Check if a province was passed to the function
    if province !="":
        provinceFrame = countryFrame[countryFrame["Province/State"] == province]
        plotFrame = provinceFrame
        plt.title("Number of total covid cases by Day in " +province+" "+ country)
    else:
        plt.title("Number of total covid cases by Day in " + country)
        plotFrame = countryFrame


    
    #The first four columns in the dataframe are ['Province/State', 'Country/Region', 'Lat', 'Long']
    for date in list(data.columns.values)[(4+(len(list(data.columns.values))-range)):]:
        plotDataX.append(date)
        plotDataY.append(sum(plotFrame[date]))

    plt.plot(plotDataX,plotDataY)
   
    plt.xticks(plotDataX[::30])
    plt.show()

def printStats(country,data):

    countryFrame = data[data["Country/Region"] == country]

    return countryFrame
    
###     Main

def main(args):
    """ Main program """
    # Code goes over here.

    covidData = acquireData(DATA_URL)

    print(args.command)

    ### Validate arguments before doing further operation
    if (args.country != '') and (args.country.capitalize() not in list(covidData['Country/Region'])):
        sys.exit("invalid --country argument "+ args.country + " is not a country/region in the dataset")

    if (args.province != '') and (args.province.capitalize() not in list(covidData['Province/State'])):
        sys.exit("invalid --province argument "+ args.province + " is not a province/state in the dataset")
                
        

    ### Main Logic for executing commands:

    if args.command == 'list countries':
        print(list(covidData["Country/Region"]))
    
    elif args.command == 'list provinces':
        print(list((covidData[covidData["Country/Region"] == args.country])["Province/State"]))
        
    elif args.command == 'plot':
        plotCountry(covidData,args.country,args.province,args.range)

    else:
        print("Command not recognised. The available commands are:")
        print("list countries: return a list of countries that are in the database")
        print("list provinces <country>: return a list of all provinces/states that are in the country")
        print(" ")
        print("plot <country> <province> <range>: plot the <range> most recent datapoints in the province in the specified country.")
        print("If no <province> is specified, all <province> will be summed together and plotted.")

    return None

#test commits:
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool for examining Covid statistics')

    parser.add_argument(dest    = 'command',
                        type    = str,
                        help    = 'The command sent to the program')


    parser.add_argument('--country',
                        type    = str,
                        help    = 'the country that the specific command will work with',
                        default= '')

    parser.add_argument('--province',
                        type    = str,
                        help    = 'the province/state that the specific command will work with',
                        default = '')

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