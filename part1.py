import hashlib

#Hash function to have deterministic hashing
def hashFunc(password):
    hash=hashlib.sha512(password.encode()).hexdigest()
    return hash

#Import the to-be-hacked passwords into a double array with each element: ["name", "hashed-password"]
with open("Q1/digitalcorp.txt", 'r') as file:
    digitalList = []
    for line in file:
        digitalList.append(line.strip().split(","))

#Remove the tags at the top
digitalList.pop(0)

#Import the rockyou password list into a list    
with open("Q1/rockyou.txt", 'r') as file:
    lines = []
    for line in file:
        lines.append(line.strip())


#To hold hashed rockyou passwords
hashedLines = []

#Populating "hashedLines" with hashed rockyou passwords
for line in lines:
    hashedLines.append(hashFunc(line))

#Iterate through hashed rockyou passwords and digitalcorp. If there is a match, print the owner with the original password
for i, line in enumerate(hashedLines):
    for hPass in digitalList:
        if (line == hPass[1]):
            print(hPass[0] + "'s password is " + lines[i])
