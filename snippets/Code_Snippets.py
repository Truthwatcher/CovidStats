'''
Prototyping block


data = acquireData(DATA_URL)

test = printStats('Canada',data)


#Get Transpose (To have statistics per Province)
test2 = test.transpose()
test2.columns = list(test2.values[0])
test3 = test2.drop(test2.index[0:3])
'''