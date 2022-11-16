from splitTerms import splitTerms
from  combineTerms import combineTerms
#given trigonemetric function, derive
def trigRule(function):
    #split into terms
    function = splitTerms(function)
    for i in range(0,len(function)):
        #differentiate sin functions
        if function[i].find("sin") > -1:
            function[i]=function[i].replace("sin","cos")
        #differentiate cos functions
        elif function[i].find("cos") > -1:
            function[i] = function[i].replace("cosx","(-sinx)")
        #differentiate tan functions
        elif function[i].find("tan") > -1:
            function[i] = function[i].replace("tan","sec^2")
    return combineTerms(function)

