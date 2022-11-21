from trigRule import trigRule
from powerRule import powerRule

def typecheck(term):
    if term.find("sin") >-1 or term.find("cos") >-1 or term.find("tan")>-1:
        return "trig"
    return "nontrig"


myfun = "-sinx"
if typecheck(myfun) == "trig": print(trigRule(myfun))
else: print(powerRule(myfun))
