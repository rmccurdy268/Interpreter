class Parameter:
    """ Parameter Class """
    def __init__(self, name: str, is_id: bool):

        self.name:str = name        # name of parameter (inside of parenthesis)
        self.is_id: bool = is_id # bool of whether it is ID (TRUE) or STRING (FALSE)

    def toString(self) -> str:
        if self.is_id == True:
            return str(self.name)
        else:
            return self.name