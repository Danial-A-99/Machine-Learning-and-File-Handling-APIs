

class inpu_manipulator:

    def __init__(self,inpu):
        self.inp = inpu

    def type_changer(self,wanted_type:type): 
        if type(self.inp) == list and type(self.inp) == wanted_type:
            return self.inp
        elif type(self.inp) == list and type(self.inp) != wanted_type:
            return " ".join(self.inp)
        elif type(self.inp) == str and type(self.inp) == wanted_type:
            return self.inp
        else:
            return (self.inp).split(" ")
        
    def list_space_remover(self):
        inp = self.type_changer(list)
        newlis = []
        for item in inp:
            if item != " " or item != "  ":
                newlis.append(item)
        return newlis
        
    def sep_list_into_two(self):
        inp = self.type_changer(list)
        listone = []
        listtwo = []
        for thing in inp:
            location = inp.index(thing)
            if location %2 == 0:
                listone.append(thing)
            else:
                listtwo.append(thing)
        return listone,listtwo
        
    def list_duplicate_remover(self):
        inp = self.type_changer(list)
        return list(dict.fromkeys(inp))
        
    def str_space_remover(self):
        inp = self.type_changer(str)
        return (inp).replace(" ","")