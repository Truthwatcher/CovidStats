#!/usr/bin/env python

###   Constants

FILE_LOCATION = 'Data/heart.csv'
DATA_URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

###   Imports

import pandas
import matplotlib.pyplot as plt

def acquireData(dataSource):
    #data = pandas.read_csv(DATA_URL, index_col = "Country/Region")
    data = pandas.read_csv(DATA_URL)
    return data

def parseData():
    f = open(FILE_LOCATION, "r")
    data = list(csv.reader(f, delimiter=';'))
    return data

    
    #with open(FILE_LOCATION, 'r') as f:
    #    print(f.read()) 
    #    print ('Hi')


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
    print(command)
    if command[0] == 'help':
        print ("The currently implemented commands are:")
        print ("exit: exit the program")
        print ("plot <country>: plot the cases in a country up to a specifc date")
    
    elif command[0] == 'exit':
        return False

    elif command[0] == 'list':
        print (list(data.columns.values))
    
    elif command[0] == 'plot':

        if command[1].capitalize() not in list(data['Country/Region']):
            print ("invalid argument for 'plot' command")

        else:
            plotCountry(command[1].capitalize(),data)
    
    elif command[0] == 'stats':

        if command[1].capitalize() not in list(data['Country/Region']):
            print ("invalid argument for 'stats' command")

        else:
            printStats(command[1].capitalize(),data)



    else:
        print ("ERROR: command not recognized")



'''
Prototyping block
'''


data = acquireData(DATA_URL)

test = printStats('Canada',data)


#Get Transpose (To have statistics per Province)
test2 = test.transpose()
test2.columns = list(test2.values[0])
test3 = test2.drop(test2.index[0:3])


'''

def main():
    """ Main program """
    # Code goes over here.

    covidData = acquireData(DATA_URL)

    while(True):

        print('Please enter a command:')
        command = input()
        if executeCommand(command,covidData) == False:
            break


    return covidData



if __name__ == "__main__":
    main()

#Useful notes:

How to access a  list of countries in the dataset:
    data['Country/Region']

How to access a  list of countries in the dataset:
    data['Country/Region']

Get all rows that have items of the specific name: data[data["Country/Region"]=="France"]

Get all the headers of the columns:
list(test.columns.values)

'''