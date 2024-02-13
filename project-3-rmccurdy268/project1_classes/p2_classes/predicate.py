from .parameter import Parameter
class Predicate:
    """ Predicate class"""
    def __init__(self, name:str):
        self.parameters: list[Parameter] = []     # a list of parameters
        self.name:str = name  # name of everything leading parenthesis
        
    def addParameter(self, parameter: Parameter) -> None: 
        self.parameters.append(parameter)

    def toString(self) -> str:
        returnString:str = ""
        count = 0
        returnString = (self.name + "(")
        for each in self.parameters:
            returnString = returnString + each.toString()
            count += 1
            if count != len(self.parameters):
                returnString += (",")
        returnString = returnString + ")"
        return returnString