import matplotlib.pyplot as plt
import scipy.stats as stats

def get_temperature_data():
    """
    Read a CSV file containing weather station data from Environment Canada.

    :return: A list of lists where each sublist contains data items
             for one month with numeric data properly converted.
    """
    infile = open('saskatoon-airport-1892-2007.csv', 'r')

    temperature_data = []

    # read but ignore the column headers
    header_row = infile.readline()

    # split each row into a list of data items using commas a delimiters and
    # add the list of data items to the temperature_data list, giving us a
    # list of lists.
    for line in infile:
        temperature_data.append(line.rstrip().split(sep=','))

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
    :return: array of 12 values with the averages of column temp_column_index for each month.
    """

    # create some lists of zeros.
    month_avg = [0.0] * 12  # running sum of yearly values for each month
    counts = [0] * 12       # running count of values added to each sum

    for row in temperature_data:
        row_year = row[1]
        row_month = row[2]
        # if the data is not missing, and is within the right year range
        if row[temp_column_index+1] != 'M' and row_year >= start_year and row_year <= end_year:
            # accumulate it in the running sum for that month Note: record[1] is the
            # year, record[2] is the month (as an integer).
            month_avg[row_month - 1] = month_avg[row_month - 1] + row[temp_column_index]
            counts[row_month - 1] = counts[row_month - 1] + 1

    # compute the averages by dividing each month's running sum by the number of data points.
    # we have to use a different count for each month because of missing data items.
    for i in range(12):
        month_avg[i] = month_avg[i] / counts[i]

    return month_avg


####### The Main Program #######


data = get_temperature_data()

# Plot average mean, min and max monthly temperatures for all years.
plt.plot(range(12), avg_monthly_temp(data, 1892, 2007, 7))  # average 
plt.plot(range(12), avg_monthly_temp(data, 1892, 2007, 3))  # max
plt.plot(range(12), avg_monthly_temp(data, 1892, 2007, 5))  # min
plt.title('Average min, max, and overall avg. monthly temperature for Saskatoon, 1892-2007')
plt.xlabel('Month')
plt.ylabel('Deg. Celcius')
plt.legend(['Average', 'Max', 'Min'])
plt.draw()

# We want to look at temps before and after cutoff_year.
# give the year a name so we can more easily experiment with different years
cutoff_year = 1970


# On a separate figure, plot average monthly mean temp for two different
# year ranges.
plt.figure()
plt.plot(range(12), avg_monthly_temp(data, 1892, cutoff_year, 7))
plt.plot(range(12), avg_monthly_temp(data, cutoff_year+1, 2007, 7))
plt.title('Average Monthly Temp in Saskatoon')
plt.xlabel('Month')
plt.ylabel('Deg. Celcius')
plt.legend(['1892-'+str(cutoff_year), str(cutoff_year+1)+'-2007'])
plt.draw()


# At this point we hypothesize that there winters may have been a little warmer
# after cutoff_year, so we set up the data for a statistical test.

# Get all records for January -- r[2] is the month as an integer.
january_data = [ r for r in data if r[2] == 1]

# Get avg January temp from 1892 to cutoff_year.  r[1] is the year, r[7] is the mean temp, and r[8]
# is an 'M' if the data is missing.
january_data_to_cutoff = [ r[7] for r in january_data if r[1] <= cutoff_year and r[8] != 'M']


# Get avg January temp from cutoff_year to 2007.  r[1] is the year, r[7] is the mean temp, and r[8]
# is an 'M' if the data is missing.
january_data_after_cutoff = [ r[7] for r in january_data if r[1] >= cutoff_year+1 and r[8] != 'M']


# Perform a statistical test to see if there is a difference in the average January temperature before and
# after cutoff_year.
[t, p] = stats.ttest_ind(january_data_to_cutoff, january_data_after_cutoff)
print('The p-value is:', p)

plt.show()