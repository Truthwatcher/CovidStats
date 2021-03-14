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

def provincesInCountry(data,country):
    return list((data[data["Country/Region"] == country])["Province/State"])

def returnXYSelection(data,country,province ='',range = 0 , daily = False):
    #Function that returns list containing a selection of [X,Y] values from the dataframe
    #
    #
    #Arguments:
    #data: [pandas dataframe] The dataset that is being operated on. Expc
    #country: [string] The country that the operation is done on. Expected to be a string
    #province: [string] The province that the operation is done on. if no probince is supplied 
    #daily: [boolean] Specify if the data should be
    xdata = []
    ydata = []

    #Creating a subset of the dataframe to ensure their are no duplicate provinces
    countryFrame = data[data["Country/Region"] == country]

    for date in list(data.columns.values)[(4+(len(list(data.columns.values))-range)):]:
        xdata.append(date)
        if province == '':
            ydata.append(sum(countryFrame[date]))
        else: 
            ydata.append(int(countryFrame[countryFrame['Province/State']==province][date]))

    return xdata,ydata





def plotCountry(data,country,province,range):
    ##To do: implement plotting + checking province

    countryFrame = data[data["Country/Region"] == country]

    plotDataX = []
    plotDataY = []
    
    #initialize the plot so other operations can be done
    plt.plot(plotDataX,plotDataY)

    
    #The first four columns in the dataframe are ['Province/State', 'Country/Region', 'Lat', 'Long']
    if province == "all":
        plotcount = 0
        plt.title("Total Covid Cases by Data in " + country)
        for entry in provincesInCountry(data,country):
                plotcount += 1

                plotDataX, plotDataY = returnXYSelection(data,country,entry,range)
                #plotDataX =[]
                #plotDataY =[]
                #for date in list(data.columns.values)[(4+(len(list(data.columns.values))-range)):]:
                #    plotDataX.append(date)
                #    plotDataY.append(int(countryFrame[countryFrame['Province/State']==entry][date]))

                #To make sure that the lines representing the data on the plot are unique, different line styles are used 
                if plotcount <=10:
                    templinestyle = '-'
                elif plotcount <=20:
                    templinestyle = '--' 
                elif plotcount <=30:
                    templinestyle = ':'
                elif plotcount <= 40:
                    templinestyle = '-.'

                plt.plot(plotDataX,plotDataY,label = entry,linestyle = templinestyle)

    elif province != '':
        plt.title("Number of total covid cases by Day in " + province + " " + country)

        for date in list(data.columns.values)[(4+(len(list(data.columns.values))-range)):]:
            plotDataX.append(date)
            plotDataY.append(int(countryFrame[countryFrame['Province/State']==province][date]))
        plt.plot(plotDataX,plotDataY,label = province)
        #sum all provinces/states 

    else:
        plt.title("Number of total covid cases by Day in " + country)

        for date in list(data.columns.values)[(4+(len(list(data.columns.values))-range)):]:
            plotDataX.append(date)
            plotDataY.append(sum(countryFrame[date]))
        plt.plot(plotDataX,plotDataY,label = country)

   
    #Do all operations that need to be done on all possible plots
    plt.xticks(plotDataX[::30])
    plt.legend()
    plt.show()

def printStats(country,data):

    countryFrame = data[data["Country/Region"] == country]

    return countryFrame
    
###     Main

def main(args):
    """ Main program """
    # Code goes over here.

    covidData = pandas.read_csv(DATA_URL)

    #If the user chooses to exclude travellers, delete them from the data
    if args.include_travellers == False:
        #covidData = covidData[covidData.province/state ]

        #I need to remove the entries when at a time. Trying to use an 'or' statement in the index causes an error
        covidData = covidData[covidData['Province/State']!= 'Repatriated Travellers'] #or (countryFrame['Province/State']!= 'Diamond Princess') ] 
        covidData = covidData[covidData['Province/State']!= 'Grand Princess']
        covidData = covidData[covidData['Province/State']!= 'Diamond Princess']


    ### Validate arguments before doing further operation
    if (args.country != '') and (args.country.capitalize() not in list(covidData['Country/Region'])):
        sys.exit("invalid --country argument "+ args.country + " is not a country/region in the dataset")

    if  (args.province != '' and args.province != 'all'):
        if args.province not in list((covidData[covidData["Country/Region"] == args.country])["Province/State"]):
            sys.exit(args.province + ' is not a valid province/state in ' + args.country)        

    if (args.province != '' and args.province != 'all') and (args.province.capitalize() not in list(covidData['Province/State'])):
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
                        help    = 'The command sent to the program,')

    parser.add_argument('--country',
                        type    = str,
                        help    = 'the country that the specific command will work with',
                        default= '')

    parser.add_argument('--province',
                        type    = str,
                        help    = 'the province/state that the specific command will work with. "all" will cause operations to be done on all province/state',
                        default = '')

    parser.add_argument('--range',
                        type    = int,
                        help    = 'The number of datapoints that you want to use. The operation will be done on the most recent day, and up to range number of days before the most recent day',
                        default = 0)  

    parser.add_argument('--include_travellers',
                        type = bool,
                        help = 'Flag to either include repatriated travellers and cruise ships or exclude them from the database',
                        default = False)

    main(parser.parse_args())

    

#if __name__ == "__main__":
#   return main()

#Useful notes:

#How to access a  list of countries in the dataset:
#    data['Country/Region']

#Get all rows that have items of the specific name: data[data["Country/Region"]=="France"]

#Get all the headers of the columns:
#list(test.columns.values)