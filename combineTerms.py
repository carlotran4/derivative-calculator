#given a function split into terms, combine the terms
def combineTerms(function):
    #combine all terms, with plus mark
    combined = ""
    for i in function:
        combined+=i
        combined+="+"
    #remove extraneous plus sign
    combined = combined[:len(combined)-1]

    #remove +- 
    for i in range(1,len(combined)-2):
        if combined[i] == "-":
            combined = combined[:i-1]+combined[i:]
    return combined
