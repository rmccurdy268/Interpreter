class Token():
    def __init__(self, token_type: str, value: str, line_num: int):
        self.token_type = token_type
        self.value = value
        self.line = line_num

    def getType(self):
        return self.token_type
    def getValue(self):
        return self.value
    def getLine(self):
        return self.line

    def to_string(self) -> str:
        return "(" + self.token_type + ",\"" + self.value + "\"," + str(self.line) + ")"