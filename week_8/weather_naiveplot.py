import matplotlib.pyplot as plt
import scipy.stats as stats


def get_temperature_data():
    infile = open('saskatoon-airport-1892-2007.csv', 'r')
    # read but ignore the column headers
    # header_row = infile.readline()
    # split each row into a list of data items using commas a delimiters and
    # add the list of data items to the temperature_data list, giving us a
    # list of lists.
    # [ [],[],...,[] ]

    temperature_data = []
    count = 0
    for line in infile: # starts from the second line
        if count>0:
            temperature_data.append(line.rstrip().split(','))
        count += 1

    infile.close()
    # Some columns of data need to be converted to floats.
    # in particular columns 3, 5, 7, 9, 11, 13, and 15.
    # Also, columns 1 and 2 need to be converted to integer data.
    for record in temperature_data:
        # do float conversions on required columns
        for i in range(3, 16, 2):
            # we can't attempt to convert if the data is missing
            if record[i + 1] != 'M':
                record[i] = float(record[i])

        # do int conversions on required columns
        for i in [1, 2]:
            record[i] = int(record[i])

    return temperature_data


def avg_monthly_temp(temperature_data, start_year,
                     end_year, temp_column_index):
    """
    Calculate the mean of the temperatures in column temp_column_index for the given range of years.

    :param temperature_data: a list in which each item is a temperature data record as a list
    :param start_year: earliest year to consider
    :param end_year: latest year to consider
    :param temp_column_index: index of the column where the temperature data resides.  
           Index 3 is max temp,
           index 5 is min temp, 
           index 8 is mean temp for the month.
    :return: array of 12 values with the
    averages of column temp_column_index for each month.
    """

    # create some lists of zeros.
    month_avg = [0.0] * 12  # running sum of yearly values for each month
    counts = [0] * 12  # running count of values added to each sum

    for row in temperature_data: # row is sublist
        row_year = row[1]
        row_month = row[2]
        # if the data is not missing, and is within the right year range
        if row[temp_column_index + 1] != 'M' and row_year >= start_year and row_year <= end_year:
            # accumulate it in the running sum for that month
            # Note: record[1] is the year, record[2] is the month (as an integer).
            month_avg[row_month - 1] = month_avg[row_month - 1] + row[temp_column_index]
            counts[row_month - 1] = counts[row_month - 1] + 1

    # compute the averages by dividing each month's running sum by the number of data points.
    # we have to use a different count for each month because of missing data items.
    for i in range(12):
        month_avg[i] = month_avg[i] / counts[i]

    return month_avg


####### The Main Program #######


data = get_temperature_data()

valid_dates = [data[r][0] for r in range(len(data)) if data[r][8] != 'M']
valid_means = [data[r][7] for r in range(len(data)) if data[r][8] != 'M']
xs = [x for x in range(0, len(valid_dates), 200)]
# print(valid_dates)
# print(valid_means)

plt.plot(valid_dates, valid_means, "bo", linestyle='')  # average
plt.xticks(xs)

plt.title('Mean temperature for each month in Saskatoon from 1892-2007')
plt.xlabel('Month')
plt.ylabel('Deg. Celcius')
plt.legend(['Average'])
plt.draw()

plt.show()
