import requests
import sys

URL="https://jsonplaceholder.typicode.com/users"

#Optional Bonus- Handle API errors
try:
    response=requests.get(URL)
    response.raise_for_status() #raises the status of the file
    data=response.json()
except requests.exceptions.RequestException as e:#takes output from raised status and uses it
    print(f"ERROR: Could not get data from API. {e}")
    sys.exit(1)#exits with an error

#using function to save from being used two times with city starts with s.
def details(user):
    print(f"User {user['id']}:")
    print(f" Name: {user['name']}")
    print(f" Username: {user['username']}")
    print(f" Email: {user['email']}")
    print(f" City: {user['address']['city']}")
    print("---------------------- \n")#creating gap from next user


#Optional Bonus- empty list
if not data:#if data is empty this will run and exit the code
    print("No user data found.")
    sys.exit(1)
    
for user in data:
    details(user)


#Optional Bonus
print("--------------------------------------------")
print("Users whose city name starts with the letter 'S")

for user in data:
    if user["address"]["city"].startswith("S"):
        details(user)