class Header:
    def __init__(self, values: list[str]) -> None:
        self.headerItems:list = values
    
    def toString(self) -> str:
        returnstring:str = ''
        for each in self.headerItems:
            returnstring = returnstring + each
        return returnstring
    