from .toople import Toople
from .Relation import Relation
from .Database import Database
from .header import Header

# remove this and delete the file 
# after you add in your code from project 2
from project1_classes.p2_classes.datalog import * 

class Interpreter:
    def __init__(self) -> None:
        self.output_str: str = ""
        self.database:Database = Database()
        self.datalog_program:Datalog = Datalog()
    
    def run(self, datalog: Datalog) -> str:
        self.datalog_program = datalog
        self.interpret_schemes()
        self.interpret_facts()
        self.interpret_queries()
        # self.interpret_rules()
        return self.output_str
    
    def interpret_schemes(self) -> None:
        # Start with an empty Database. 
        # For each scheme in the Datalog program, 
        for each in self.datalog_program.schemesPredicates:
            newList:list[str] = []
            for every in each.parameters:
                newList.append(every.name)
            newHeader:Header = Header(newList)
            newRelation:Relation = Relation(each.name, newHeader)
            self.database.add_relation(each.name, newRelation)
        #   add an empty Relation to the Database. 
        #   Use the scheme name as the name of the relation 
        #   and the attribute list from the scheme as the header of the relation.
    
    def interpret_facts(self) -> None:
        # For each fact in the Datalog program, 
        for each in self.datalog_program.factsPredicates:
            newName:str = each.name
            for every in self.database.dictionary:
                if newName == every:
                    newToople:Toople = Toople(each.parameters)
                    self.database.dictionary[every].addToople(newToople)
                
        #   add a Tuple to a Relation. 
        #   Use the predicate name from the fact to 
        #   determine the Relation to which the Tuple should be added. 
        #   Use the values listed in the fact to provide the values for the Tuple.
    
    def interpret_queries(self) -> None:
        for each in self.datalog_program.queriesPredicates:
            self.output_str += each.toString() + "? "
            pseudoString:str = self.evaluate_predicate(each).__str__()
        # for each query in the datalog_program call evaluate predicate.
            # append the predicate returned by this function to the output string
            
        # output notes:
        # For each query, output the query and a space. 
        # If the relation resulting from evaluating the query is empty, output 'No'. 
        # If the resulting relation is not empty, output 'Yes(n)' where n is the number of tuples in the resulting relation.
        
        # If there are variables in the query, output the tuples from the resulting relation.

        # Output each tuple on a separate line as a comma-space-separated list of pairs.
        # Each pair has the form N='V', 
        # where N is the attribute name from the header and V is the value from the tuple. 
        # Output the name-value pairs in the same order as the variable names appear in the query. 
        # Indent the output of each tuple by two spaces.
        
        # some of this output code was given to you in the Relation.__str__() function. 
        # It may need to be modified slightly

        # Output the tuples in sorted order. 
        # Sort the tuples alphabetically based on the values in the tuples. 
        # Sort first by the value in the first position and if needed up to the value in the nth position.
        pass
    
    def evaluate_predicate(self, predicate: Predicate) -> Relation:
        # For this predicate you need to
        #   use a sequence of select, project, and rename operations on the Database 
        #   to evaluate the query. Evaluate the queries in the order given in the input.
        #DOES THIS NEED TO BE THE SAME RELATION IN THE DATABASE OR CAN I NAKE A COPY
        thisRelation:Relation = self.database.dictionary[predicate.name]
        # Get the Relation from the Database with the 
        #   same name as the predicate name in the query.
        marks:dict[str, int] = {}
        for each in predicate.parameters:
            count:int = 0
            if each.is_id:
                if each.name in marks:
                    thisRelation = thisRelation.select2(marks[each.name], count)
                else:
                    marks[each.name] = count
            else:
                thisRelation = thisRelation.select1(each.name, count)
            count += 1
        if len(thisRelation.tuplesSet) == 0:
            self.output_str += "No\n"
        else:
            self.output_str += "Yes(" + str(len(thisRelation.tuplesSet)) + ")\n"
            print("ESize of tupes set:" + str(len(thisRelation.tuplesSet)))

        # Use one or more select operations to select 
        #   the tuples from the Relation that match the query. Iterate over the parameters of the query: If the parameter is a constant, select the tuples from the Relation that have the same value as the constant in the same position as the constant. If the parameter is a variable and the same variable name appears later in the query, select the tuples from the Relation that have the same value in both positions where the variable name appears.
        thisRelation = thisRelation.project(marks.values())
        newHeader:Header = Header(marks.keys())
        thisRelation = thisRelation.rename(newHeader)
        if len(marks) != 0:
            print("ESize of tupes set:" + str(len(thisRelation.tuplesSet)))
            count:int = 0
            for tople in thisRelation.tuplesSet:
                print("Length of tuple: " + str(len(tople.items)))
                for every in tople.items:
                    self.output_str += ((list(marks)[count] + "=" + every.toString()))
                    print("looped\n")
                count += 1
        return thisRelation
        # After selecting the matching tuples, use the project operation 
        #   to keep only the columns from the Relation that correspond to the 
        #   positions of the variables in the query. Make sure that each variable name appears only once in the resulting relation. If the same name appears more than once, keep the first column where the name appears and remove any later columns where the same name appears. (This makes a difference when there are other columns in between the ones with the same name.)
        # After projecting, use the rename operation to 
        #   rename the header of the Relation to the
        #   names of the variables found in the query.
        # The operations must be done in the order described above: 
        #   any selects, 
        #   followed by a project, 
        #   followed by a rename.
        # return the new predicate
        pass
    
    # this will be implemented during project 4
    def interpret_rules(self) -> None:
        pass