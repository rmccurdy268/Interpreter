from .fsa import FSA
from typing import Callable as function

class CommaFSA(FSA):
    def __init__(self, name):
        FSA.__init__(self, name) # You must invoke the __init__ of the parent class
        self.start_state:function = self.s0
        self.accept_states.add(self.s1)
        self.tokenLength:int = 0

    def s0(self) -> function:
        next_state: function = None
        if self.input_string[self.num_chars_read] != ',': 
            next_state = self.s_err
        else: 
            next_state = self.s1
        self.num_chars_read += 1
        self.tokenLength += 1
        return next_state

    def s1(self) -> function:
        next_state: function = self.s1 # if any inputs, go to error state
        self.num_chars_read += 1
        return next_state

    def s_err(self) -> function:
        next_state: function = self.s_err # stay in error state on all inputs
        self.num_chars_read += 1
        return next_state
    

    def get_token_len(self) -> int: return self.tokenLength