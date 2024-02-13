from .rule import Rule
from .predicate import Predicate

class Datalog:
    """ Datalog Program Class"""
    def __init__(self):
        self.schemesPredicates: list[Predicate] = []             # list of schemes
        self.factsPredicates: list[Predicate] = []               # list of facts
        self.queriesPredicates: list[Predicate] = []             # list of predicates
        self.rulesList: list[Rule] = []                          # list of rules

    def clear(self):
        self.schemesPredicates.clear()        
        self.factsPredicates.clear()          
        self.queriesPredicates.clear()         
        self.rulesList.clear()

    def addSchemePredicate(self, pred: Predicate) -> None: 
        self.schemesPredicates.append(pred)
    def addFactPredicate(self, pred: Predicate) -> None: 
        self.factsPredicates.append(pred)
    def addQueryPredicate(self, pred: Predicate) -> None: 
        self.queriesPredicates.append(pred)
    def addRuletoDP(self, rule: Rule) -> None: 
        self.rulesList.append(rule)
    def datalogToString(self) -> str:
        returnString:str = ''
        returnString += ("Schemes(" + str(len(self.schemesPredicates)) + "):\n")
        for each in self.schemesPredicates:
            returnString += ("  " + each.toString() + "\n")
        returnString += ("Facts(" + str(len(self.factsPredicates)) + "):\n")
        for each in self.factsPredicates:
            returnString += ("  " + each.toString() + ".\n")
        returnString += ("Rules(" + str(len(self.rulesList)) + "):\n")
        for each in self.rulesList:
            returnString += ("  " + each.toString() + "\n")
        returnString += ("Queries(" + str(len(self.queriesPredicates)) + "):\n")
        for each in self.queriesPredicates:
            returnString += ("  " + each.toString() + "?\n")
        return returnString