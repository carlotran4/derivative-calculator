def splitTerms():
    myFun = input("please input your formula. Refer to readme for proper styling:\n")

    splitLocations = []

    myFunSplit = []

    for i in range(0,len(myFun)):
        if myFun[i] == "+":
            splitLocations.append(i)


    myFunSplit.append(myFun[0:splitLocations[0]])
    for i in range(0,len(splitLocations)-1):
        myFunSplit.append(myFun[splitLocations[i]+1:splitLocations[i+1]])
    myFunSplit.append(myFun[splitLocations[len(splitLocations)-1]+1:])

    print(myFunSplit)
splitTerms()