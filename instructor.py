import os


class Instructor:
    def __init__(self):
        self.ins_name = "" '''have to be 3 character'''
        self.par_count_min = 0
        self.par_count_max = 0

    def process(self, param, state):
        if len(param) < self.par_count_min or len(param) > self.par_count_max:
            print("Error : At line " + str(state.ins_place) +
                  ", excepted " + str(self.par_count_min) + " to " +
                  str(self.par_count_max) + " parameters but got " + str(len(param)))
            state.executing = False

    def get_instructor_list(self):
        return[Mem(), Set(), Jlz(), Get(), Prt(), Hlt(), Neg()]
    #and your own...


class Mem(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "MEM"
        self.par_count_min = 1
        self.par_count_max = 2

    def process(self, param, state):
        super(Mem, self).process(param, state)
        if len(param) == self.par_count_min:
            state.mem_place = param[0]
        else:
            if param[1] == 0:
                state.mem_place = param[0]
            else:
                state.mem_place = state.mem_place + param[0]


class Set(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "SET"
        self.par_count_min = 1
        self.par_count_max = 2

    def process(self, param, state):
        super(Set, self).process(param, state)
        if len(param) == self.par_count_min:
            state.mem = param[0]
        else:
            if param[1] == 0:
                state.mem = param[0]
            else:
                state.mem = state.mem + param[0]

class Jlz(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "JLZ"
        self.par_count_min = 1
        self.par_count_max = 1

    def process(self, param, state):
        super(Jlz, self).process(param, state)
        if state.mem < 0:
            state.ins_place = param[0]


class Get(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "GET"
        self.par_count_min = 0
        self.par_count_max = 1

    def process(self, param, state):
        super(Get, self).process(param, state)
        if len(param) == self.par_count_min:
            state.mem = int(input("input a number : "))
        else:
            if param[0] == 0:
                state.mem = int(input("input a number : "))
            else:
                state.mem = ord(input("input a character : "))
        os.system('cls' if os.name=='nt' else 'clear') 


class Prt(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "PRT"
        self.par_count_min = 0
        self.par_count_max = 1

    def process(self, param, state):
        super(Prt, self).process(param, state)
        if len(param) == self.par_count_min:
            print(state.mem, end=" ")
            state.output_list.append(state.mem)
        else:
            if param[0] == 0:
                print(state.mem, end=" ")
                state.output_list.append(state.mem)
            else:
                print(chr(state.mem), end="")
                state.output_list.append(chr(state.mem))


class Hlt(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "HLT"
        self.par_count_min = 0
        self.par_count_max = 0

    def process(self, param, state):
        super(Hlt, self).process(param, state)
        print()
        state.executing = False


class Neg(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "NEG"
        self.par_count_min = 0
        self.par_count_max = 0

    def process(self, param, state):
        super(Neg, self).process(param, state)
        state.mem = -state.mem


'''
    class Yourclass(Instructor):
        def __init__(self):
            self.ins_name = "(name)"
            self.par_count_min = 0
            self.par_count_max = 0

        def process(self, param, state):
            super(Yourclass, self).process(param, state)
            #and your code
            '''



