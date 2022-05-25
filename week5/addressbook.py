import requests

        
class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
    
class Contact():
    def __init__(self, first, last, email, phone, photo):
        self.fname = first
        self.lname = last
        self.email = email
        self.phone = phone
        self.photo = photo

    def __str__(self):
            return f'{self.fname} {self.lname} ({self.email})'

    def __repr__(self):
        rep = 'Person(' + self.fname + ',' + str(self.lname) + ')'
        return rep

    def getFirstName(self):
        return self.fname

    def getLastName(self):
        return self.lname

    def getEmail(self):
        return self.email

    def getPhone(self):
        return self.phone

    def getPhoto(self):
        return self.photo