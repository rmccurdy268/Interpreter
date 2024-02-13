class Toople:
    def __init__(self,items:list[str]):
        self.items:list[str] = items
    def __hash__(self) -> int:
        return hash(tuple(self.items))
    def __eq__(self, other: 'Toople') -> bool:
        if type(other) != 'Toople':
            return False
        else:
            if self.items == other.items:
                return True
            else:
                return False
        
    def __lt__(self, other: 'Toople') -> bool:
        pass

    def toString(self) -> str:
        returnstring:str = ''
        for each in self.items:
            returnstring = returnstring + each.name
        return returnstring