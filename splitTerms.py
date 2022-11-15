def splitTerms(myFun):
    #initialize lists for the resulting formula split into terms, locations of plus signs
    splitLocations = []

    myFunSplit = []

    #Change - signs into +-
    for i in range(0,len(myFun)):
        if myFun[i] == "-" and myFun[i-1] != "+":
            myFun = myFun[:i] + "+" + myFun[i:]

    #add locations of plus signs to split locations
    for i in range(0,len(myFun)):
        if myFun[i] == "+":
            splitLocations.append(i)

    #split myFun into terms based on the split locations

    
    if len(splitLocations) > 0:
        #split first term
        myFunSplit.append(myFun[0:splitLocations[0]])

        #split middle terms
        for i in range(0,len(splitLocations)-1):
            myFunSplit.append(myFun[splitLocations[i]+1:splitLocations[i+1]])

        #split last location
        myFunSplit.append(myFun[splitLocations[len(splitLocations)-1]+1:])
    else: myFunSplit.append(myFun)

    return myFunSplit