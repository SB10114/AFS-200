from addressbook import AddressBook, Contact
from flask import Flask, render_template, request
import requests
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

class AllUsers():
    def __init__(self):
        self.authUsers = []
    
    def addUser(self, user):
        self.authUsers.append(user)
    def showUsers(self):
        for user in self.authUsers:
            print(user)


def getData(numUsers, nationality):
    URL = "https://randomuser.me/api/?results="+str(numUsers)+"&nat="+nationality
    try: 
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)



users = AddressBook()
numUsersRequesting = 25
data = getData(numUsersRequesting, "us")
response_API = requests.get('https://randomuser.me/api/?results=10&nat=us')

for user in data["results"]:
    newUser = Contact(user["name"]["first"],
                user['name']['last'],
                user['email'],
                user['phone'],
                user['picture']['medium'])
    users.addAddress(newUser)
    print(newUser)

@app.route("/")
def hello():
    print(users.addresses)
    return render_template('index.html', results = users.getAllAddresses())