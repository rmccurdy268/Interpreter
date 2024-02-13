from .fsa_classes.fsa import FSA
from .fsa_classes.colon_dash_fsa import ColonDashFSA
from .fsa_classes.colon_fsa import ColonFSA
from .fsa_classes.add_fsa import AddFSA
from .fsa_classes.block_comment_fsa import BlockCommentFSA
from .fsa_classes.comma_fsa import CommaFSA
from .fsa_classes.facts_fsa import FactsFSA
from .fsa_classes.id_fsa import IDFSA
from .fsa_classes.left_paren_FSA import LeftParenFSA
from .fsa_classes.line_comment_fsa import LineCommentFSA
from .fsa_classes.multiply_fsa import MultiplyFSA
from .fsa_classes.period_fsa import PeriodFSA
from .fsa_classes.q_mark_fsa import QMarkFSA
from .fsa_classes.queries_fsa import QueriesFSA
from .fsa_classes.right_paren_fsa import RightParenFSA
from .fsa_classes.rules_fsa import RulesFSA
from .fsa_classes.schemes_fsa import SchemesFSA
from .fsa_classes.string_fsa import StringFSA
from .token_1 import Token
from .manager_fsm import ManagerFSM

class LexerFSM:
    def __init__(self):
        self.tokens: list[Token] = []
        self.fsa_list:list[FSA] = []
        my_colon_fsa: ColonFSA = ColonFSA(name = "COLON")
        self.fsa_list.append(my_colon_fsa)
        my_colon_dash_fsa: ColonDashFSA = ColonDashFSA(name = "COLON_DASH")
        self.fsa_list.append(my_colon_dash_fsa)
        my_left_paren_fsa: LeftParenFSA = LeftParenFSA(name = "LEFT_PAREN")
        self.fsa_list.append(my_left_paren_fsa)
        my_right_paren_fsa: RightParenFSA = RightParenFSA(name = "RIGHT_PAREN")
        self.fsa_list.append(my_right_paren_fsa)
        my_comma_fsa: CommaFSA = CommaFSA(name = "COMMA")
        self.fsa_list.append(my_comma_fsa)
        my_period_fsa: PeriodFSA = PeriodFSA(name = "PERIOD")
        self.fsa_list.append(my_period_fsa)
        my_qmark_fsa: QMarkFSA = QMarkFSA(name = "Q_MARK")
        self.fsa_list.append(my_qmark_fsa)
        my_multiply_fsa: MultiplyFSA = MultiplyFSA(name = "MULTIPLY")
        self.fsa_list.append(my_multiply_fsa)
        my_add_fsa: AddFSA = AddFSA(name = "ADD")
        self.fsa_list.append(my_add_fsa)
        my_schemes_fsa: SchemesFSA = SchemesFSA(name = "SCHEMES")
        self.fsa_list.append(my_schemes_fsa)
        my_facts_fsa: FactsFSA = FactsFSA(name = "FACTS")
        self.fsa_list.append(my_facts_fsa)
        my_rules_fsa: RulesFSA = RulesFSA(name = "RULES")
        self.fsa_list.append(my_rules_fsa)
        my_queries_fsa: QueriesFSA = QueriesFSA(name = "QUERIES")
        self.fsa_list.append(my_queries_fsa)
        my_string_fsa: StringFSA = StringFSA(name = "STRING")
        self.fsa_list.append(my_string_fsa)
        my_id_fsa: IDFSA = IDFSA(name = "ID")
        self.fsa_list.append(my_id_fsa)
        my_block_comment_fsa: BlockCommentFSA = BlockCommentFSA(name = "COMMENT")
        self.fsa_list.append(my_block_comment_fsa)
        my_line_comment_fsa: LineCommentFSA = LineCommentFSA(name = "COMMENT")
        self.fsa_list.append(my_line_comment_fsa)

    
    def run(self, input: str) -> list:
        self.lineNumber: int = 1
        self.my_manager_fsm: ManagerFSM = ManagerFSM()
        while input != "":
            if input[0] == "\n":
                self.lineNumber += 1
                input = input[1:]
            elif (input[0].isspace() == True):
                input = input[1:]
            else:
                status_dict: dict = dict()
                passedTokenLength:int = 0
                for fsa in self.fsa_list:
                    temp_input = input  # create a copy of the input string
                    fsa.reset()
                    accept_status: bool = fsa.run(temp_input)
                    status_dict[fsa.get_fsa_name()] = accept_status
                    if accept_status == True:
                        if (fsa.get_fsa_name() == "COMMENT"):
                            passedTokenLength = fsa.get_token_len()
                            fsa.reset()
                            break
                        newToken = Token(token_type= fsa.get_fsa_name(), value= input[:fsa.get_token_len()], line_num=self.lineNumber)
                        passedTokenLength = fsa.get_token_len()
                        self.tokens.append(newToken)
                        fsa.reset()
                        break
                    fsa.reset()
                input = input[passedTokenLength:]
                
                if all(value == False for value in status_dict.values()):
                    newToken = Token(token_type= "UNDEFINED", value = input[0], line_num= self.lineNumber)  
                    self.tokens.append(newToken)
                    input = ""
                    firstString:str = ""
                    for token in self.tokens:
                        firstString += (token.to_string()+"\n") 
                    returnString = firstString + "\n" + "Total Tokens = Error on line " + str(self.lineNumber)
                    return self.tokens
        
        if input == "":
            newToken = Token(token_type= "EOF", value = "", line_num= self.lineNumber)
            self.tokens.append(newToken)
        return self.tokens

    def lex(self, input_string: str) -> Token:
        ...

    def __manager_fsm__(self) -> Token:
        ...

    def reset(self) -> None:
        ...