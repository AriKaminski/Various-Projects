import csv
import datetime as dt

# Get first name from full name


def fname(any):
    try:
        nm = any.split(',')
        return nm[1]

    except IndexError:
        return ''

# Get last name from full name


def lname(any):
    try:
        nm = any.split(',')
        return nm[0]
    except IndexError:
        return ''

# Convert string to 0 if no value


def integer(any):
    return int(any or 0)

# Convert mm/dd/yyyy date to date or None if no valid date


def date(any):
    try:
        return dt.datetime.strptime(any, "%m/%d/%Y").date()
    except ValueError:
        return None

# Convert any string to boolean, False if no value


def boolean(any):
    return bool(any)


def floatnum(any):
    s_balance = (any.replace('$', '').replace(',', ''))
    return float(s_balance or 0)


# Create an empty list of people
people = []

# Define a class where each person is an object


class Person:
    def __init__(self, id, first_name, last_name, birth_year, date_joined, is_active, balance):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.date_joined = date_joined
        self.is_active = is_active
        self.balance = balance


# Open CSV file with UTF-8 encoding, dont read in newline characters
with open('Python For Dummies/sample.csv', encoding='utf-8', newline='') as f:
    reader = enumerate(csv.reader(f))
    # Skip the first row, which is the column headers
    f.readline()
    # Loop through remaining rows one at a time, i is counter, row is entire row
    for i, row in reader:
        # Create a person object using each unique data rows and columns
        people.append(Person(i, fname(row[0]), lname(row[0]), integer(
            row[1]), date(row[2]), boolean(row[3]), floatnum(row[4])))
# Iterate through all objects in people list
for p in people:
    print(p.id, p.first_name, p.last_name,
          p.birth_year, p.is_active, p.balance)


"""

with open('Python For Dummies/sample.csv', encoding='utf-8', newline='') as f:
    reader = enumerate(csv.reader(f))

    for i, row in reader:
        if i > 0:
            try:
                full_name = row[0].split(',')
                last_name = full_name[0].strip()
                first_name = full_name[1].strip()
            except IndexError:
                full_name = last_name = first_name = ""

            birth_year = int(row[1] or 0)

            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
            except ValueError:
                date_joined = None
            print(first_name, last_name, birth_year, date_joined)

print('Done!')
"""
