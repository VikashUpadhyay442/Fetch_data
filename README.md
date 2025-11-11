# Script for fetching User Data
This is a small program to fetch user data from API.

## Overview
This script fetches a json data from https://jsonplaceholder.typicode.com/users, and works with them.

1. It loops through the data and display-"name","username","email","city" from the data.

2. It then display the Optional Bonus, that was data from user whose city name starts with "S".

3. it uses sys.exit(1) for exiting the program with an error for API errors or empty list.

## Requirements

1. Python 3
2. "requests" library - can be installed via "pip install requests"

## How to run the Script

1. Go to the folder containing main.py file, manually or via cd.

2. Either run it directly or run using the command line with the command- "Python main.py".

3. Running the script will print the data to console itself.
