from .Relation import Relation

class Database:
    def __init__(self) -> None:
        self.dictionary:dict[str, Relation] = {}

    def add_relation(self, name:str, relation:Relation):
        self.dictionary[name] = relation
