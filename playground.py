from trigRule import trigRule
from powerRule import powerRule

class myfunction():
    def __init__(self,f):
        function = f

def typecheck(term):
    if term[0].find("sin") >-1 or term.find("cos") >-1 or term.find("tan")>-1:
        return "trig"
    return "nontrig"


myfun = "60x^2-50x"
if typecheck(myfun) == "trig": print(trigRule(myfun))
else: print(powerRule(myfun))
