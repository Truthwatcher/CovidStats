## covidstats

## Introduction:

This is a project I created to help teach myself how to analyze statistics using Python using a worldwide covid infections dataset.

-------
## Installation:
covidstats a pip installable python package.

To install covidstats dynamically, navigate to the /covidstats directory run 'pip install -e .'

-------
## Outline:

/covidstats
 * /main.py : allows a user to generate a plot from a specific subset of data.
 * /mathfunctions.py : contains functions related to calculating statistics.

-------
## Data:

Source: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series?fbclid=IwAR0cH8QXrAjDyfOkYrpSCz68ZO4b8Y7_kBTO7DMaq9DEKTYeZ1rnm1EVdyw

I do not claim any ownership of the data used by this project. All rights reserved by their respective owners.

-------

# Tools:
Visual Studio Code:
https://code.visualstudio.com/

Pylint: 
Installed with:
python -m pip install -U pylint --user

Git:
https://git-scm.com/download/win

Tortoise Git:
https://tortoisegit.org/download/

-------

# Useful Links:

Data Processing:
https://www.dataquest.io/blog/numpy-tutorial-python/

How to use DataFrames in Pandas library:
https://www.geeksforgeeks.org/python-pandas-dataframe/

Pandas Tutorial
https://pandas.pydata.org/docs/getting_started/index.html

Library for Plotting:
https://matplotlib.org/tutorials/introductory/pyplot.html

-------
### Notes from peer Review 2021-03-16:
- could use pandas cumsum to make returnXYSelection look nicer
- To reduce bloat on arguments that are getting passed around, could pass the 'args' around instead. Tradeoff is code reusability
- Learn Linear Regression and Use it. libraries to use are either https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.linregress.html or https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html?fbclid=IwAR1XeOhq_Js22DFbRhJZwpcpBnS_HZ4Nio-x70ddIAH3T0JGQm6uBTxIwwM