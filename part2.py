import hashlib

#Hash function to have deterministic hashing
def hashFunc(password):
    hash=hashlib.sha512(password.encode()).hexdigest()
    return hash

#Return a list with prepended and apended salt + password
def saltHash(password, salt):
    saltPrepApen = []
    saltPrepApen.append(hashFunc(password + "" + salt))
    saltPrepApen.append(hashFunc(salt + "" + password))
    return saltPrepApen
    
#Import the to-be-hacked passwords into a double array with each element: ["name", "hashed-password"]
with open("Q1/salty-digitalcorp.txt", 'r') as file:
    digitalList = []
    saltList = []
    for line in file:
        tokenized = line.strip().split(",")
        saltList.append(tokenized.pop(1))   #Add the salt to the salt list
        digitalList.append(tokenized)       #Append now that the salt has been removed

#Remove tags at the top
saltList.pop(0)
digitalList.pop(0)
      
with open("Q1/rockyou.txt", 'r') as file:
    lines = []
    for line in file:
        lines.append(line.strip())
        
#To hold hashed rockyou passwords
hashedLines = []


#Populating "hashedLines" with hashed rockyou passwords
for line in lines:
    salted = []
    for salt in saltList:
        salted.append(saltHash(line, salt))
    hashedLines.append(salted)

#I thought each person's password could be prepended or appended independently from one another so that information is also displayed
for j, hashed in enumerate(hashedLines):
    for i, salted in enumerate(hashed):
        if(digitalList[i][1] == salted[0]):
            print(digitalList[i][0] + "'s password is " + lines[j] + ". The salt is appended")
        if(digitalList[i][1] == salted[1]):
            print(digitalList[i][0] + "'s password is " + lines[j] + ". The salt is prepended")
