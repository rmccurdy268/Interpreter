from project1_classes.lexer_fsm import LexerFSM
from project1_classes.token_1 import Token
from rdp1 import RDP
from project1_classes.p2_classes.datalog import Datalog
from project3_classes.interpreter import Interpreter
def project3(input: str) -> str:
    tokens: list[Token] = []
    #newToken:Token = Token("UNDEFINED", "#", 0)
    lexer: LexerFSM = LexerFSM()
    tokens = lexer.run(input)
    #tokens.append(newToken)
    my_rdp: RDP = RDP()
    newDatalog:Datalog =  my_rdp.parse_input(tokens)
    myInterpreter:Interpreter = Interpreter()
    returnString:str = myInterpreter.run(newDatalog)
    print(returnString)
    return returnString    

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read() 

#Use this to run and debug code within VS
if __name__ == "__main__":
    input_contents = "# COPYRIGHT © BRIGHAM YOUNG UNIVERSITY CS 236\n# FOR USE ONLY DURING SUMMER 2021 SEMESTER\nSchemes:\n    SK(X,Y)\nFacts:\n    SK('a','a').\nRules:\n    SK(A,B) :- SK(A,B).\nQueries:\n    SK(D,C)?\n    SK(A,'c')?\n"
    project3(input_contents)
