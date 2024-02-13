from .fsa import FSA
from typing import Callable as function

class RulesFSA(FSA):
    def __init__(self, name):
        FSA.__init__(self, name)
        self.start_state: function = self.s0
        self.accept_states.add(self.s5)
        self.tokenLength:int = 0
        
    def s0(self) -> function:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'R': 
            next_state = self.s_err
        else:
            next_state = self.s1
            self.tokenLength += 1
        self.num_chars_read += 1
        return next_state
    
    def s1(self) -> function:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'u': 
            next_state = self.s_err
        else:
            next_state = self.s2
            self.tokenLength += 1
        self.num_chars_read += 1
        return next_state
    
    def s2(self) -> function:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'l': 
            next_state = self.s_err
        else:
            next_state = self.s3
            self.tokenLength += 1
        self.num_chars_read += 1
        return next_state
    
    def s3(self) -> function:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 'e': 
            next_state = self.s_err
        else:
            next_state = self.s4
            self.tokenLength += 1
        self.num_chars_read += 1
        return next_state
    
    def s4(self) -> function:
        next_state: function = None
        if self.input_string[self.num_chars_read] != 's': 
            next_state = self.s_err
        else:
            next_state = self.s5
            self.tokenLength += 1
        self.num_chars_read += 1
        if self.input_string[self.num_chars_read].isspace() == False and self.input_string[self.num_chars_read] != ':':
            next_state = self.s_err
        return next_state
    
    def s5(self) -> function:  
        if self.num_chars_read >= len(self.input_string):
            return self.s_err
        self.num_chars_read += 1
        return self.s5
    
    def s_err(self) -> function:
        self.num_chars_read += 1
        return self.s_err
    
    def get_token_len(self) -> int: return self.tokenLength