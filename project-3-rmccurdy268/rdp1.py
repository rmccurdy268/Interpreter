from typing import Callable
from project1_classes.token_1 import Token
from project1_classes.p2_classes.datalog import Datalog
from project1_classes.p2_classes.predicate import Predicate
from project1_classes.p2_classes.parameter import Parameter
from project1_classes.p2_classes.rule import Rule

myDatalog:Datalog = Datalog()
myParamList:list[Parameter] = []
myRule:Rule = Rule()
class RDP:  # RDP stands for recursive descent parser
    def __init__(self) -> None:
        ###################################
        # Tuple defining an LL(1) grammar #
        # • set of nonterminals           #
        # • set of terminals              #
        # • starting nonterminal          #
        # • set of productions            #
        ###################################
        self.nonterminals: set[str] = {'scheme', 'schemeList', 'fact', 'factList', 'datalogProgram', 'idList', 
                                       'stringList', 'rule', 'ruleList', 'headPredicate', 'predicate',
                                       'predicateList', 'parameter', 'parameterList', 'query', 'queryList'}          # set of nonterminals. Each nonterminal will have its own function
        self.starting_nonterminal: Callable[[], None] = self.datalogProgram            # Starting nonterminal
        self.terminals: set[str] = {'SCHEMES', 'COLON', 'LEFT_PAREN', 'ID', 'COMMA', 'RIGHT_PAREN',
                                     'FACTS', 'PERIOD','STRING', 'RULES', 'COLON_DASH', 'QUERIES', 
                                     'QMARK', 'EOF'}  # set of terminals
        # Productions                                   # Defined within the nonterminal functions

        ##########################################
        # Define FIRST sets for each nonterminal #
        ##########################################
        self.first: dict[str, set[str]] = dict()
        self.first['datalogProgram'] = {'SCHEMES'}
        self.first['scheme'] = {'ID'}
        self.first['schemeList'] = {'ID'}
        self.first['idList'] = {'COMMA'}
        self.first['fact'] = {'ID'}
        self.first['factList'] = {'ID'}
        self.first['stringList'] = {'COMMA'}
        self.first['rule'] = {'ID'}
        self.first['ruleList'] = {'ID'}
        self.first['headPredicate'] = {'ID'}
        self.first['predicate'] = {'ID', 'STRING'}
        self.first['predicateList'] = {'COMMA'}
        self.first['parameter'] = {'STRING'}
        self.first['parameterList'] = {'COMMA'}
        self.first['query'] = {'ID'}
        self.first['queryList'] = {'ID'}
        ##########################################
        # Define FOLLOW sets for nonterminal I   #
        ##########################################
        self.follow: dict[str, set[str]] = dict()
        self.follow['schemeList'] = {'FACTS'}
        self.follow['idList'] = {'RIGHT_PAREN'}
        self.follow['factList'] = {'RULES'}
        self.follow['stringList'] = {'RIGHT_PAREN'}
        self.follow['ruleList'] = {'QUERIES'}
        self.follow['predicateList'] = {'PERIOD'}
        self.follow['parameterList'] = {'RIGHT_PAREN'}
        ###########################################
        # Variables for Managing the input string #
        ###########################################
        self.input: list = None
        self.num_chars_read: int = 0

        ###########################################
        # Variables for printing the trace        #
        ###########################################
        self.tree_depth: int = 0
        self.domain: set = set()
        self.domainCount: int = 0

    def parse_input(self, input: list) -> Datalog:
        """ Call this function from main.
            It gets the input, calls the starting non-terminal,
            and does the accounting to see if the parse was successful
        """
        myDatalog.clear()
        myParamList.clear()
        self.input = input
        self.starting_nonterminal()  # Run the RDP by calling the starting nonterminal
        returnString:str = ""
        returnString = ("Success!\n")
        returnString += myDatalog.datalogToString()
        returnString += ("Domain(" + str(len(self.domain)) + "):")
        newDomain:list = []
        newDomain = sorted(self.domain)
        for each in newDomain:
            returnString += ("\n  " + each)
        return myDatalog
        
    ##############################################################
    # Each nonterminal gets its own function.                      #
    # The function knows which productions have the nonterminal on #
    # the left hand side of the production. The correct right    #
    # hand side of the production is chosen by looking at the    #
    # current input and the FIRST set of the right hand side     #
    ##############################################################
    def datalogProgram(self) -> None:
        # Production E--> nDI | OEE
        #self.__print_entry_message("datalogProgram")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'SCHEMES'):
            self.__advance_input()
            current_input = self.__get_current_input()
            if self.__match(current_input, 'COLON'):
                self.__advance_input()
                self.scheme()
                self.schemeList()
                current_input = self.__get_current_input()
                if self.__match(current_input, 'FACTS'):
                    self.__advance_input()
                    current_input = self.__get_current_input()
                    if self.__match(current_input, 'COLON'):
                        self.__advance_input()
                        self.factList()
                        current_input = self.__get_current_input()
                        if self.__match(current_input, 'RULES'):
                            self.__advance_input()
                            current_input = self.__get_current_input()
                            if self.__match(current_input, 'COLON'):
                                self.__advance_input()
                                self.ruleList()
                                current_input = self.__get_current_input()
                                if self.__match(current_input, 'QUERIES'):
                                    self.__advance_input()
                                    current_input = self.__get_current_input()
                                    if self.__match(current_input, 'COLON'):
                                        self.__advance_input()
                                        self.query()
                                        self.queryList()
                                        current_input = self.__get_current_input()
                                        if self.__match(current_input, "UNDEFINED"):
                                            return
                                        if self.__match(current_input, "EOF"):
                                            
                                            return None                                    
                                        else: raise ValueError("Failure!\n  " + current_input.to_string())
                                    else: raise ValueError("Failure!\n  " + current_input.to_string())
                                else: raise ValueError("Failure!\n  " + current_input.to_string())
                            else: raise ValueError("Failure!\n  " + current_input.to_string())
                        else: raise ValueError("Failure!\n  " + current_input.to_string())
                    else: raise ValueError("Failure!\n  " + current_input.to_string())
                else: raise ValueError("Failure!\n  " + current_input.to_string())
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        else: raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("datalogProgram")

    def scheme(self) -> None:
        # Production scheme --> ID LEFT_PAREN ID idList RIGHT_PAREN
        #self.__print_entry_message("scheme")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            pred:Predicate = Predicate(str(current_input.getValue()))
            self.__advance_input()  # move to the next current input character
            current_input = self.__get_current_input()
            if self.__match(current_input, 'LEFT_PAREN'):
                self.__advance_input()
                current_input = self.__get_current_input()
                if self.__match(current_input, 'ID'):
                    param:Parameter = Parameter(current_input.getValue(), True)
                    myParamList.append(param)
                    self.__advance_input()
                    self.idList()
                    current_input = self.__get_current_input()
                    if self.__match(current_input, 'RIGHT_PAREN'):
                        self.__advance_input()
                        current_input = self.__get_current_input()
                        for each in myParamList:
                            pred.addParameter(each)
                        myDatalog.addSchemePredicate(pred)
                        myParamList.clear()
                    else: raise ValueError("Failure!\n  " + current_input.to_string())
                else: raise ValueError("Failure!\n  " + current_input.to_string())
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        else: raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("scheme")

    def idList(self) -> None:
        #self.__print_entry_message("idList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'COMMA'):
            self.__advance_input()  # move to the next current input character
            current_input = self.__get_current_input()
            if self.__match(current_input, 'ID'):
                param:Parameter = Parameter(current_input.getValue(), True)
                myParamList.append(param)
                self.__advance_input()
                self.idList()
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        elif self.__match(current_input, 'RIGHT_PAREN'):
            return
        else: raise ValueError("Failure!\n  " + current_input.to_string())
    
    def schemeList(self) -> None:
        #self.__print_entry_message("schemeList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            self.scheme()
            self.schemeList()
        elif self.__match(current_input, 'FACTS'):
            return
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("schemeList")

    def factList(self) -> None:
        #self.__print_entry_message("factList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            self.fact()
            self.factList()
        elif self.__match(current_input, 'RULES'):
            return
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("factList")

    def stringList(self) -> None:
        #self.__print_entry_message("stringList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'COMMA'):
            self.__advance_input()  # move to the next current input character
            current_input = self.__get_current_input()
            if self.__match(current_input, 'STRING'):
                self.domain.add(current_input.getValue())
                self.domainCount += 1
                param:Parameter = Parameter(current_input.getValue(), False)
                myParamList.append(param)
                self.__advance_input()
                current_input = self.__get_current_input()
                self.stringList()
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        elif self.__match(current_input, 'RIGHT_PAREN'):
            #print(current_input.getType())
            current_input = self.__get_current_input()
        else: raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("stringList")


    def fact(self) -> None:
        #self.__print_entry_message("fact")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            newPred:Predicate = Predicate(current_input.getValue())
            self.__advance_input()  # move to the next current input character
            current_input = self.__get_current_input()
            if self.__match(current_input, 'LEFT_PAREN'):
                self.__advance_input()
                current_input = self.__get_current_input()
                if self.__match(current_input, 'STRING'):
                    param:Parameter = Parameter(current_input.getValue(), False)
                    myParamList.append(param)
                    self.domain.add(current_input.getValue())
                    self.domainCount += 1
                    self.__advance_input()
                    self.stringList()
                    current_input = self.__get_current_input()
                    if self.__match(current_input, 'RIGHT_PAREN'):
                        self.__advance_input()
                        current_input = self.__get_current_input()
                        if self.__match(current_input, 'PERIOD'):
                            self.__advance_input()
                            current_input = self.__get_current_input()
                            for each in myParamList:
                                newPred.addParameter(each)
                            myDatalog.addFactPredicate(newPred)
                            myParamList.clear()
                        else: raise ValueError("Failure!\n  " + current_input.to_string())
                    else: raise ValueError("Failure!\n  " + current_input.to_string())
                else: raise ValueError("Failure!\n  " + current_input.to_string())
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        else: raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("fact")

    def ruleList(self) -> None:
        #self.__print_entry_message("ruleList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            self.rule()
            self.ruleList()
        elif self.__match(current_input, 'QUERIES'):
            return
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("rulesList")

    def headPredicate(self) -> None:
        #self.__print_entry_message("headPredicate")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            #print(self.__get_tab_string(), "Terminal 'ID' matched by input character", self.__get_current_input())
            pred:Predicate = Predicate(str(current_input.getValue()))
            self.__advance_input()  # move to the next current input character
            current_input = self.__get_current_input()
            if self.__match(current_input, 'LEFT_PAREN'):
                self.__advance_input()
                current_input = self.__get_current_input()
                if self.__match(current_input, 'ID'):
                    temp:Parameter = Parameter(str(current_input.getValue()), True)
                    myParamList.append(temp)
                    self.__advance_input()
                    self.idList()
                    current_input = self.__get_current_input()
                    if self.__match(current_input, 'RIGHT_PAREN'):
                        self.__advance_input()
                        current_input = self.__get_current_input()
                        for each in myParamList:
                            pred.addParameter(each)
                        myRule.setHeadPredicate(pred)
                        myParamList.clear()
                    else: raise ValueError("Failure!\n  " + current_input.to_string())
                else: raise ValueError("Failure!\n  " + current_input.to_string())
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        else: raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("headPredicate")

    def parameter(self) -> None:
        #self.__print_entry_message("parameter")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'STRING'):
            param:Parameter = Parameter(current_input.getValue(), False)
            myParamList.append(param)
            self.__advance_input()
            current_input = self.__get_current_input()
        elif self.__match(current_input, 'ID'):
            param:Parameter = Parameter(current_input.getValue(), True)
            myParamList.append(param)
            self.__advance_input()
            current_input = self.__get_current_input()
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        
    def parameterList(self) -> None:
        #self.__print_entry_message("parameterList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'COMMA'):
            self.__advance_input()
            current_input = self.__get_current_input()
            self.parameter()
            self.parameterList()
            current_input = self.__get_current_input()
        elif self.__match(current_input, 'RIGHT_PAREN'):
            return
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("parameterList")
        
    def predicateList(self, isQuery:bool) -> None:
        #self.__print_entry_message("predicateList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'COMMA'):
            self.__advance_input()
            self.predicate(isQuery)
            self.predicateList(isQuery)
            current_input = self.__get_current_input()
        elif self.__match(current_input, 'PERIOD'):
            return
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("predicateList")

    def predicate(self, isQuery:bool) -> None:
        #self.__print_entry_message("predicate")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            pred:Predicate = Predicate(str(current_input.getValue()))
            self.__advance_input()  # move to the next current input character
            current_input = self.__get_current_input()
            if self.__match(current_input, 'LEFT_PAREN'):
                self.__advance_input()
                self.parameter()
                self.parameterList()
                current_input = self.__get_current_input()
                if self.__match(current_input, 'RIGHT_PAREN'):
                    self.__advance_input()
                    current_input = self.__get_current_input()
                    for each in myParamList:
                        pred.addParameter(each)
                        #print("PARAMS: " + each.toString())
                    if isQuery == False:
                        myRule.addBodyPredicate(pred)
                    else:
                        myDatalog.addQueryPredicate(pred)
                    myParamList.clear()

                else: raise ValueError("Failure!\n  " + current_input.to_string())
            else: raise ValueError("Failure!\n  " + current_input.to_string())
        else: raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("predicate")

    def query(self) -> None:
        #self.__print_entry_message("query")
        isQuery:bool = True
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            pred:Predicate = Predicate(str(current_input.getValue()))
        self.predicate(isQuery)
        current_input = self.__get_current_input()
        #print (current_input.getType())
        if self.__match(current_input, "Q_MARK"):
            self.__advance_input()
            current_input = self.__get_current_input()
            for each in myParamList:
                pred.addParameter(each)
            myParamList.clear()
        #self.__print_exit_message("query")

    def queryList(self) -> None:
        #self.__print_entry_message("queryList")
        current_input: Token = self.__get_current_input()
        if self.__match(current_input, 'ID'):
            self.query()
            self.queryList()
            current_input = self.__get_current_input()
        elif self.__match(current_input,'EOF') or self.__match(current_input,'UNDEFINED'):
            return
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        #self.__print_exit_message("queryList")


    def rule(self) -> None:
        isQuery:bool = False
        #self.__print_entry_message("rule")
        current_input: Token = self.__get_current_input()
        myRule.reset()
        self.headPredicate()
        current_input = self.__get_current_input()
        if self.__match(current_input, 'COLON_DASH'):
            self.__advance_input()  
            self.predicate(isQuery)
            self.predicateList(isQuery)
            current_input = self.__get_current_input()
            if self.__match(current_input, 'PERIOD'):
                #print("saw period")
                copy:Rule = Rule()
                copy.setHeadPredicate(myRule.getHeadPredicate())
                newList:list[Predicate] = myRule.getBodyPredicates()
                for each in newList:
                    copy.addBodyPredicate(each)
                myDatalog.addRuletoDP(copy)
                self.__advance_input() 
                current_input = self.__get_current_input()
            else:
                raise ValueError("Failure!\n  " + current_input.to_string())
        else:
            raise ValueError("Failure!\n  " + current_input.to_string())
        
    ############################################################################
    # Helper functions for managing the input                                    #
    # One looks at the current input                                           #
    # Another reads the input and advances to the next input                  #
    # A third looks to see if the current input character matches a target     #
    # Convention in python is to prefix private functions by a double underscore #
    # https://www.geeksforgeeks.org/private-functions-in-python/                 #
    ############################################################################
    def __get_current_input(self) -> Token:
        if self.num_chars_read > len(self.input):
            raise ValueError("Expected to read another input character but no inputs left to read")
        elif self.num_chars_read == len(self.input):
            self.__print_message_about_current_string("Reading the end of string symbol in getCurrentInput", "")
            return None
        else:
            return self.input[self.num_chars_read]

    def __advance_input(self) -> None:
        if self.num_chars_read > len(self.input):
            raise ValueError("Expected to advance to the next input character but reached the end of input")
        self.num_chars_read += 1

    def __match(self, current_input: Token, target_input: str) -> bool:
        return current_input.getType() == target_input
    ########################
    # Other public functions #
    ########################
    def reset(self) -> None:
        self.num_chars_read = 0
        self.input = ""

    ###############################
    # Parse tree printing functions #
    ###############################
    """
    def __print_entry_message(self, function_name: str) -> None:
        print(self.__get_tab_string(), "In", function_name, "function.")
        self.tree_depth += 1

    def __print_exit_message(self, function_name: str) -> None:
        self.tree_depth -= 1
        print(self.__get_tab_string(), "Returning from", function_name, ".")

    def __print_message_about_current_string(self, message: str, current_input: Token) -> None:
        print(self.__get_tab_string(), message, current_input.getType())

    """

    def __get_tab_string(self) -> str:
        tab_string: str = ""
        for d in range(self.tree_depth):
            tab_string += "\t"
        return tab_string
