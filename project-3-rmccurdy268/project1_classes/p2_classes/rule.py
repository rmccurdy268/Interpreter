from .predicate import Predicate
class Rule:
    """ Rule Class """
    def __init__(self):
        self.reset()
        headPredicate:Predicate = Predicate("")
        body_predicates:list[Predicate] = []
    
    def setHeadPredicate(self, headPred:Predicate) -> None:
        self.headPredicate = headPred
    def addBodyPredicate(self, pred: Predicate) -> None: 
        self.body_predicates.append(pred)
    def getHeadPredicate(self)-> Predicate:
        return self.headPredicate
    def getBodyPredicates(self) -> list:
        return self.body_predicates

    def toString(self) -> str:
        returnString:str = ""
        count = 0
        returnString = self.headPredicate.toString() + " :- "
        for each in self.body_predicates:
            count += 1
            returnString = returnString + each.toString()
            if count != len(self.body_predicates):
                returnString += ","
        returnString = returnString + "."
        return returnString
    

    def reset(self)->None:
        self.head_predicate = Predicate("")
        self.body_predicates = []
