from splitTerms import splitTerms
from  combineTerms import combineTerms
# given function in form ax^n+bx^o..., differentiate separated terms. 

def powerRule(function):
    #split terms
    function = splitTerms(function)
    
    #create iterator to change values of function list
    x=0

    #loop through terms in function
    for i in function:
        indexOfCarrot = i.find("^")
        #If carrot exists, make exponent the numbers after the carrot
        if indexOfCarrot>-1:
            exponent = int(i[indexOfCarrot+1:len(i)])
        #If carrot does not exist, term is either ax or a, if term contains x then exponent is 1, 
        # if term doesnt contain x it is a constant so 0
        elif i.__contains__("x"): exponent = 1
        else: exponent = 0
        #f' of a constant is 0, so term is empty
        if exponent == 0: del function[x] 
        #f' of linear function is coefficient, so term = everything before the last char, or x
        elif exponent == 1: function[x] = i[:len(i)-1]
        #f' of x^n is nx^(n-1)
        else:
            #x^n value of f'(x^2) is x^1 or x 
            if exponent == 2:
                newExponent = "x"
            #x^n value of f'(x^n) is x^(n-1)
            else: newExponent = "x^"+str(exponent-1)

            #concatenate coefficient of f'(ax^n), and new x^n value 
            indexOfX = i.find("x")
            function[x] = str(int(i[:indexOfX])*exponent)+ newExponent

        #increment iterator
        x+=1

    return combineTerms(function)
