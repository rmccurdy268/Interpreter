from typing import Callable as function

"""class FSA:
    def __init__(self, name: str):
        self.fsa_name: str = name
        self.start_state: function = self.S0
        self.accept_states: set[function] = set()
        self.input_string: str = ""
        self.num_chars_read: int = 0
    
    def S0(self) -> NotImplemented:
        raise NotImplementedError()
    
    def run(self, input_string: str) -> bool:
        self.input_string = input_string
        current_state: function = self.start_state
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
        if current_state in self.accept_states:
            return True # Output this if the FSA ended in an accept state
        else: 
            return False

        

    def reset(self) -> None:
        self.num_chars_read = 0
        self.input_string = ""

    def get_fsa_name(self) -> str:
        return self.fsa_name

    def set_fsa_name(self, FSA_name) -> None:
        self.fsa_name = FSA_name

    def get_chars_read(self) -> int:  
        return self.num_chars_read"""
class FSA:
    """ FSA Base or Super class"""
    def __init__(self, name: str):
        self.fsa_name: str = name        # name of your state machine
        self.start_state: function = self.s0  # start state always named s0 in this implementation
        self.accept_states: set[function] = set()  # set of accept states must be specified in derived class
        self.input_string: str = ""      # input string and
        self.num_chars_read: int = 0     # current input character
        self.tokenLength: int = 0
    
    def run(self, input_string: str) -> bool:
        """ The workhorse of the FSA shared by all the FSAs in project 1.
        • record the input string
        • initialize the start state
        • while there are still characters to read in the input string ...
        • transition between states
        • return something useful if the final state is an accept state """
        self.input_string = input_string
        current_state: function = self.start_state
        while self.num_chars_read < len(self.input_string):
            current_state = current_state()
        if current_state in self.accept_states:
            return True # Output this if the FSA ended in an accept state
        else: 
            return False # Output this if the FSA ended in anything other than an accept state

    def reset(self) -> None:
        self.num_chars_read = 0
        self.tokenLength = 0
        self.input_string = ""

    def s0(self) -> NotImplemented:
        """ Every FSA must have a start state, and we'll always name 
        it s0. The function for the start state must be defined in the
        derived class since it's not defined here. """
        pass

    def get_fsa_name(self) -> str: return self.fsa_name

    def get_chars_read(self) -> int: return self.num_chars_read

    def get_token_len(self) -> int: return self.tokenLength