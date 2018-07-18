# CSV literally stands for comma separated variable, where the comma is what is known as a "delimiter."
# While you can also just simply use Python's split() function, to separate lines and data within each line, the CSV module can also be used to make things easy.

import csv

with open('Examples/emp.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    salary = []
    for row in readCSV:
        sal = row[2]
#        print(row)
#        print(row[0])
#        print(row[0],row[1],row[2],)
        salary.append(sal)

    print(salary)
    print(max(salary[1:]))


# #How to pull out specific data from the spreadsheet and save it to a list variable:
# with open('Examples/example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     colors = []
#     for row in readCSV:
#         color = row[3]
#         date = row[0]
#
#         dates.append(date)
#         colors.append(color)
#
#     print(dates)
#     print(colors)



# # #Once we have this data, what can we do with it? Maybe we are curious about what color something was on a specific date.
# with open('Examples/example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     colors = []
#     for row in readCSV:
#         color = row[2]
#         date = row[0]
#
#         dates.append(date)
#         colors.append(color)
#
#     print(dates)
#     print(colors)
#
#     # now, remember our lists?
#
#     whatColor = input('What color do you wish to know the date of?:')
#     coldex = colors.index(whatColor.lower())
#     theDate = dates[coldex]
#     print('The date of',whatColor,'is:',theDate)
