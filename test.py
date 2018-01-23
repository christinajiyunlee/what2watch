# import re
# # m = re.search('(?<=-)\w+', 'spam-egg')
# # m.group(0)
#
# test = "This is my test string \n"
# pls = re.search('is', test)
# print pls.group(0)

#trying to access element within array within array

"""
DOWNLOAD SQLITE3 TO RUN THIS DB FILE YOU CREATED
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(ID NUMBER, title TEXT, year NUMBER, genre TEXT)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234, 'Toystory', 1995, 'animation')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()"""

"""
#ZIP AND UNZIP (COMBINE) TWO ARRAYS INTO ONE
x = [['one', 'two', 'three'], 'four', 'five']
y = [1, 2, 3]
z = ['un', 'deux', 'trois']
combine = zip(x, y, z) #= zip so first element of x is combined with first element of y
prnt = list(combine) #= make into an array form instead of () form -> (,,) to [,,]
x2, y2, z2 = zip(*combine) #= unzip the zipped stuff zip(*zippedtings)

print prnt[0][0][0]
#print x == list(x2)
#print list(z2)
#print z
"""
