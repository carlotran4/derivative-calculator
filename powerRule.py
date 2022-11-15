from splitTerms import splitTerms
# given a list of separated terms in form ax^n, differentiate. 

def powerRule(function):
    x=0
    for i in function:
        indexOfCarrot = i.find("^")
        if indexOfCarrot>-1:
            exponent = int(i[indexOfCarrot+1:len(i)])
        elif i.__contains__("x"): exponent = 1
        else: exponent = 0
        if exponent == 0: function[x] = ""
        if exponent == 1: function[x] = i[:len(i)-1]
        x+=1
    print(function)

powerRule(splitTerms("5x^2+5x+5"))