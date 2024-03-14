import hashlib

#Number of iterations, since this is given to us in the question I set it to the maximum possible value.
iterations = 2000

#Possible combinations of key stretching
combinations = ["a", "b", "c", "d", "e", "f"]

#Hash function to have deterministic hashing
def hashFunc(password):
    hash=hashlib.sha512(password.encode()).hexdigest()
    return hash

#Return a list with prepended and apended salt + password
def saltHash(password, salt, prevHash, combination):
    a = hashFunc(password + prevHash + salt)
    b = hashFunc(password + salt + prevHash)
    c = hashFunc(salt + password + prevHash)
    d = hashFunc(salt + prevHash + password)
    e = hashFunc(prevHash + password + salt)
    f = hashFunc(prevHash + salt + password)
    
    if(combination == "a"):
        return a
    elif(combination == "b"):
        return b
    elif(combination == "c"):
        return c
    elif(combination == "d"):
        return d
    elif(combination == "e"):
        return e
    elif(combination == "f"):
        return f

#Import the to-be-hacked passwords into a double array with each element: ["name", "hashed-password"]
with open("Q1/keystreching-digitalcorp.txt", 'r') as file:
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

for line in lines:
    for c in combinations:
        k = 0
        for salt in saltList:
            prevHash = ""
            j = 0
            while j < iterations:
                cand = saltHash(line, salt, prevHash, c)
                if(cand == digitalList[k][1]):
                    print(digitalList[k][0] + "'s password is " + line)
                    #print(c)
                    digitalList.pop(k)
                    saltList.pop(k)
                    break
                prevHash = cand
                j+=1
            k+=1