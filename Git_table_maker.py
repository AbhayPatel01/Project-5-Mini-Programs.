
# Project Difficulty: Easy. 
# Programming Pardigm: OOP. 
# Modules: Not Used. 
# TO DO:# Error Handling Printed Messages, Edge Cases etc..
        # Different input formats: e.g. (R,10) ( nested tuple)
        # Column type (e.g. entire column of code block, or bold/italics)


class GitTable: 
    def __init__(self,size:tuple,alignment='L'):
        ''' Constructor for the object ''' 
        self.__size = size
        self.__alignment = alignment 

    def create(self) -> None: 
        ''' Creates the table ''' 
        cell_heading = {'L':'|:---','C':'|:---:','R':'|---:'} 
        if len(self.__alignment) > self.__size[1]: 
            self.__alignment = self.__alignment[:self.__size[1]]
        elif len(self.__alignment) < self.__size[1]:
            self.__alignment += (self.__size[1] - len(self.__alignment)) * 'L'
           
        core_symbol = '|'
        alignment = ''.join([ cell_heading[x] for x in self.__alignment ]) + core_symbol
        for x in range(-1, self.__size[0]):
            out = (self.__size[1] + 1) * core_symbol
            if x == 0:
                print(alignment)
            
            print(out)

    @property 
    def size(self): 
        return self.__size


a_git_table = GitTable((10,3))
a_git_table.create()
