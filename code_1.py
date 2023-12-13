import getpass

#inputing the database in the form of dictonary { username : password}
database={"sanjay.kumar": "sanju@11122","shreya.pothapur":"shreya@gmail","uday.kumar":"udaya19011977"}
username= input("Enter your username:")
password=input("Enter your password:")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = input("Enter the password again:")
        break
print("Verified")
