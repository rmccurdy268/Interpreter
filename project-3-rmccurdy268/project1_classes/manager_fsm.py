class ManagerFSM:
    def __init__(self) -> None:
        self.output:str = "EOF"
    def run(self, status_dict: dict[str, bool]):
    
        if status_dict["COLON_DASH"] == True and status_dict["COLON"] == True:
            self.output = "COLON-DASH"
        elif status_dict["COLON"] == True and status_dict["COLON_DASH"] == False:
            self.output = "COLON"
        elif status_dict["LEFT_PAREN"] == True:
            self.output = "LPAREN"
        elif status_dict["MULTIPLY"] == True:
            self.output = "MULTIPLY"
        elif status_dict["RIGHT_PAREN"] == True:
            self.output = "RPAREN"
        elif status_dict["COMMA"] == True:
            self.output = "COMMA"
        elif status_dict["PERIOD"] == True:
            self.output = "PERIOD"
        elif status_dict["ADD"] == True:
            self.output = "ADD"
        elif status_dict["Q_MARK"] == True:
            self.output = "QMARK"
        elif status_dict["SCHEMES"] == True:
            self.output = "SCHEMES"
        elif status_dict["FACTS"] == True:
            self.output = "FACTS"
        elif status_dict["RULES"] == True:
            self.output = "RULES"
        elif status_dict["QUERIES"] == True:
            self.output = "QUERIES"
        elif status_dict["STRING"] == True:
            self.output = "STRING"
        elif status_dict["ID"] == True and status_dict["QUERIES"] == False and status_dict["Schemes"] == False and status_dict["RULES"] == False and status_dict["FACTS"] == False:
            self.output = "ID"
        elif status_dict["COMMENT"] == True:
            self.output = "BLOCK COMMENT"
        elif status_dict["COMMENT"] == True:
            self.output = "LINE COMMENT"
        else:
            self.output = "UNDEFINED"
        return self.output