from .header import Header
from .toople import Toople

class Relation:
    def __init__(self, name: str, header: Header) -> None:
        self.name:str = name
        self.relationHeader:Header = header
        self.tuplesSet:set = set()
        
    def addToople(self, tuple:Toople) -> None:
        self.tuplesSet.add(tuple)

    def byList(element:Toople):
        return element.items

    def __str__(self) -> str:
        returnString:str = self.name + "(" + self.relationHeader.toString() + ")\n"
        for each in self.tuplesSet:
            returnString += '\t'
            returnString += each.toString()
        return returnString
    
    def toString(self):
        print(self.name + " " + self.relationHeader.toString())
        print("\n")
        for each in self.tuplesSet:
            print('\t')
            print(each.toString())
        
    def add_row(self, row: Toople) -> None:
        ...
    
    def select1(self, value: str, colIndex: int) -> 'Relation':
        newRelation:Relation = Relation(self.name, self.relationHeader)
        for each in self.tuplesSet:
            if each.items[colIndex] == value:
                newRelation.addToople(each)
            else:
                pass
        return newRelation
    
    def select2(self, index1: int, index2: int) -> 'Relation':
        newRelation:Relation(self.name, self.relationHeader)
        for each in self.tuplesSet:
            if each.items[index1] == each.items[index2]:
                newRelation.addToople(each)
            else:
                pass
        return newRelation
    
    def rename(self, new_header: Header) -> 'Relation':
        #CHECK IF THEY ARE THE SAME LENGTH
        newRelation:Relation = Relation(self.name, new_header)
        for each in self.tuplesSet:
            newRelation.addToople(each)
        return newRelation

    def project(self, col_indexes: list[int]) -> 'Relation':
        count:int = 0
        newList:list[str] = []
        for each in self.relationHeader.headerItems:
            if count in col_indexes:
                newList.append(each)
            count += 1
        
        newHeader:Header = Header(newList)
        newRelation:Relation = Relation(self.name, newHeader)
        
        count = 0
        for each in self.tuplesSet:
            newItems:list[str] = []
            for every in each.items:
                if count in col_indexes:
                    newItems.append(every)
                count += 1
            newToople:Toople = Toople(newItems)
            newRelation.addToople(newToople)

        return newRelation