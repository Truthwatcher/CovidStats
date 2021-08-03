# Everything in this file could probably be replaced by numpy or other functions
# I've made this just to make sure I understand the math involved.

sampledata = [1, 2, 3, 4, 5]


def standard_deviation(data):
    """

    Parameters
    ----------
    data

    Returns
    -------

    """
    # input: list of numbers
    # Returns the population standard deviation of a list of numbers
    # Formula: https://www.k2analytics.co.in/wp-content/uploads/2020/05/standard-deviation.png

    n = len(data)
    mean = (sum(data) / n)
    summation = 0

    for value in data:
        summation += (value - mean) ** 2

    return (summation / n) ** (1 / 2)


def zscore(data):
    # Returns the zscores of all samples in a dataset
    # Formula: https://www.statisticshowto.com/probability-and-statistics/z-score/

    stddev = standard_deviation(data)
    mean = (sum(data) / len(data))
    zscores = []

    for value in data:
        zscores.append((value - mean) / stddev)

    return zscores


def correlation_coeffecient(xdata: list(), ydata: list()) -> float:
    """
    Calculates the population correlation coefficient.
    Based on this formula (which is another way of writing the Pearson Correlation coefficient:
    https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/correlation-coefficient-r/v/calculating-correlation-coefficient-r

    Parameters
    ----------
    xdata
    ydata

    Returns
    -------

    """
    # Returns the correlation coeffecient of the x and y data.
    # https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/correlation-coefficient-r/v/calculating-correlation-coefficient-r
    # https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/correlation-coefficient-r/v/calculating-correlation-coefficient-r
    #
    #

    if len(xdata) != len(ydata):
        print("unequal number of x and y values. Sanitize your data inputs")

    result = 0
    stdx = standard_deviation(xdata)
    stdy = standard_deviation(ydata)
    meanx = sum(xdata)/len(xdata)
    meany = sum(ydata)/len(ydata)

    for i in range(len(xdata)):
        result += ((xdata[i]-meanx)/stdx)*((ydata[i]-meany)/stdy)

    return(result/len(xdata))

if __name__ == "__main__":
    samplexdata = [1,2,2,3]
    sampleydata = [1,2,3,6]
    print(correlation_coeffecient(samplexdata,sampleydata))
