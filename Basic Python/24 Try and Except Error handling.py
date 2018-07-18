#Try and Except statements, which are used for error handling.
# These statements work similarly to the if-else, where if the Try runs, the except will not run.
# If the Try fails, then the exception will run with the error that was just generated in the try.
# Try and Except is mainly used to handle failures in code, which result in errors.
# With handling exceptions, you can keep your code running when it would otherwise grind to a catastrophic halt from an error.
# You can also use error handling to log problems in your code, or to even attempt to remedy the problem as a part of the program.



import csv

with open('Examples/example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    # we could put the try anywhere. The weak point, however, starts
    # in my opinion immediately when we accept user input... no longer
    # is this is a closed-program, so I would personally code this block
    # here, but you could put the try right about the print statement
    # of where we search for the color and we KNOW it will throw an error
    # if not in the list.
    try:
        whatColor = input('What color do you wish to know the date of?:')

        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of',whatColor,'is:',theDate)
        else:
            # now we can handle a specific scenario, instead
            # of handling it with a "catch-all" error.
            # now we have error handling and
            # proper logic. Yay.
            print('This color was not found.')

    # in python 2, this is read exception Exception, e. It's just helpful
    # to know this for porting old scripts if you need to.


    except Exception as e:
        print(e)
