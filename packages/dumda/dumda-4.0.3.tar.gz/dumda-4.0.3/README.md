# Dumda 4.0.3

Python Library to get fast extensive Dummy Data for testing https://pypi.org/project/dumda/

## Installation

```
pip install dumda
```

or update from previous version:

```
pip install --update dumda
```

## Usage

This section will cover the functionality of Dumda and how you can power your applicaiton \
with fast customizable randomly generated data.

```python
import dumda
```

### Names

You can generate random names with a handful of specifiers such as the associated \
sex of the name and the format of the name string.

```python
from dumda import random_name, random_names, names_by_prefix

# Basic call with default arguments, returns a full name
n1 = random_name()
print("Hello, world. My name is %s" % n1)

# You can specify the sex of the name generated (1 for female and 0 for male)
# the default is None, so any name of any sex is chosen
male_name = random_name(sex=0)
female_name = random_name(sex=1)
print("Hi, %s. My name is %s" % (male_name, female_name))

# finally you can specify the format of the string
# the default is First Last, but if you mark 'reversed' parameter as True
# it will return the name in Last, First format
formal_name = random_name(reversed=True)
print("Student: %s" % formal_name)

# Most relevantly you can generated n number of names and the parameter list
# stays the same
name_list = random_names(n=7, sex=0, reversed=False)  # returns an iterator
print(list(name_list))

# you can also retrieve names with just a given prefix
BEST_PREFIX = "oliv"
print(names_by_prefix(BEST_PREFIX, n=1, sex=0, full=False))
```

#### Output:

```
Hello, world. My name is Tracie Bradley
Hi, Hugo Flores. My name is Rosario Romero
Student: Benton, Audrea
['Kris Gould', 'Wes Heath', 'Arthur Larsen', 'Lucien Christian', 'Lincoln Moody', 'Cortez Jimenez', 'Giuseppe Meadows']
Oliver
```

### Countries/Cities

You can generate random countries with a handful of specifiers as well.

```python
from dumda import random_country, random_countries, random_city, random_cities, NAMEKEY, POPULATIONKEY, LNGKEY, \
    LATKEY

# Countries
c1 = random_country()  # you can generate a random country like names
print("I'm from %s" % c1)
c2 = random_country(iso=True)  # you can specify whether you want the country string to be in iso3 format
print("COUNTRY: %s" % c2)

# as with names, you can get an iterator of a specified amount of countries
country_codes = random_countries(10, iso=True)
print(list(country_codes))

# Cities
# you can generate random cities. There are 3 optional parameters
# 1. country - there are valid countries to get cities from
#               check COUNTRIES_WITH_CITIES_DATA to see, will raise Exception if not valid
# 2.populus - if marked, it will only return cities that have a population higher than
#               the average population of the dataset
# 3. returnobj - if marked, will return a dictionary object rather than just a city name str
#               - with data related to the city
city1 = random_city()
print("Random city: %s" % city1)
norwegian_city = random_city(country="norway")  # country string can be in any casing
print("I wonder how cold it is in %s, Norway" % norwegian_city)
city2 = random_city(country="United States", populus=True)
print("%s is a pretty sizable place" % city2)
obj = random_city(country="Colombia", populus=True, returnobj=True)
# Keys are in the __init__ file
lng = obj[LNGKEY]
lat = obj[LATKEY]
print(f"{obj[NAMEKEY]} has a population of {obj[POPULATIONKEY]} and is located at: {lat, lng}")

# and of course, you can get numerous
print(list(random_cities(n=3, country="United States", populus=False, returnobj=True)))

```
#### Output:
```
I'm from Montenegro
COUNTRY: CIV
['ZAF', 'ALB', 'ARG', 'SWZ', 'MOZ', 'GBR', 'SWE', 'BGR', 'CZE', 'POL']
Random city: Presidente Medici
I wonder how cold it is in Haugesund, Norway
Chicago is a pretty sizable place
Pasto has a population of 382236 and is located at: (1.2136, -77.2811)
[{'name': 'Wescosville', 'latitude': 40.5617, 'longitude': -75.5489, 'country': 'United States', 'iso3': 'USA', 'population': 6694}, {'name': 'Moundsville', 'latitude': 39.9221, 'longitude': -80.7422, 'country': 'United States', 'iso3': 'USA', 'population': 8252}, {'name': 'Nampa', 'latitude': 43.5845, 'longitude': -116.5631, 'country': 'United States', 'iso3': 'USA', 'population': 184428}]
```

### Misc.
There is also some other functions for full person recreation, (and then more on that)
```python
from dumda import generate_email, generate_number, Person, names_by_prefix
import json

# generate an email address
email_list = []
names = list(names_by_prefix("oli", n=3, full=True))
for i in range(3):
    # name passed to email generator *must* be a full name of style; First Last
    e = generate_email(names[i])
    email_list.append(e)
    
print(email_list)

# generate a phone number
print("Call me: %s" % generate_number())

# possible parameters
# - area_code (defaults to randomly generated) and country_code (defaults to +1)

DC_AREA_CODE = 202
print("for store hours call: %s" % generate_number(area_code=DC_AREA_CODE))




p = Person() # generate a person object that uses all of the functions in Dumda
print(json.dumps(p.json(), indent=4))
```
#### Output:
```
['ohuffman@baz.net', 'olivesloan@qux.org', 'olivalin@bar.org']
Call me: +1 (743)-792-9493
for store hours call: +1 (202)-293-2130
{
    "name": "Katelynn Brown",
    "location": {
        "name": "Atlantic",
        "latitude": 41.3957,
        "longitude": -95.0138,
        "country": "United States",
        "iso3": "USA",
        "population": 6526
    },
    "email": "katelynnbrown@foo.org",
    "phone": "+1 (793)-759-380"
}
```
