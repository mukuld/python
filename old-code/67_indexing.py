# Python Programme Number 67
# Indexing example for Python
# Programmer: Mukul Dharwadkar
# Date: 6th December 2006

# This programme will print out a date given a day, month and year as numbers

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

# Create a list with one ending for each number from 1 to 31
endings = ["st", "nd", "rd"] + 17 * ["th"] \
          + ["st", "nd", "rd"] + 7 * ["th"] \
          + ["st"]

# Get input

year = raw_input("Year: ")
month = raw_input("Month (1 - 12): ")
day = raw_input("Day (1 - 31): ")

month_num = int(month)
day_num = int(day)

# 1 is subtracted from the number entered by user to get the correct index
month_name = months[month_num - 1]
ordinal = day + endings[day_num - 1]

print month_name + " " + ordinal + ", " + year
