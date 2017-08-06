import os


class Instructor:
    def __init__(self):
        self.ins_name = "" '''have to be 3 character'''
        self.par_count_min = 0
        self.par_count_max = 0

    def process(self, param, state):
        if len(param) < self.par_count_min or len(param) > self.par_count_max:
            print("Error : At line " + str(state.get_instructor_place()) + ", excepted " + str(self.par_count_min) +
                  " to " + str(self.par_count_max) + " parameters but got " + str(len(param)))
            state.set_executing(False)

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
            state.set_mem_place(param[0])
        else:
            if param[1] == 0:
                state.set_mem_place(param[0])
            else:
                state.set_mem_place(state.get_mem_place() + param[0])


class Set(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "SET"
        self.par_count_min = 1
        self.par_count_max = 2

    def process(self, param, state):
        super(Set, self).process(param, state)
        if len(param) == self.par_count_min:
            state.set_mem(param[0])
        else:
            if param[1] == 0:
                state.set_mem(param[0])
            else:
                state.set_mem(state.get_mem() + param[0])


class Jlz(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "JLZ"
        self.par_count_min = 1
        self.par_count_max = 1

    def process(self, param, state):
        super(Jlz, self).process(param, state)
        if state.get_mem() < 0:
            state.set_instructor_place(param[0])


class Get(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "GET"
        self.par_count_min = 0
        self.par_count_max = 1

    def process(self, param, state):
        super(Get, self).process(param, state)
        if len(param) == self.par_count_min:
            state.set_mem(int(input("input a number : ")))
            os.system('cls')
        else:
            if param[0] == 0:
                state.set_mem(int(input("input a number : ")))
                os.system('cls')
            else:
                state.set_mem(ord(input("input a character : ")))
                os.system('cls')


class Prt(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "PRT"
        self.par_count_min = 0
        self.par_count_max = 1

    def process(self, param, state):
        super(Prt, self).process(param, state)
        if len(param) == self.par_count_min:
            print(state.get_mem(), end=" ")
            state.output_list.append(state.get_mem())
        else:
            if param[0] == 0:
                print(state.get_mem(), end=" ")
                state.output_list.append(state.get_mem())
            else:
                print(chr(state.get_mem()), end="")
                state.output_list.append(chr(state.get_mem()))


class Hlt(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "HLT"
        self.par_count_min = 0
        self.par_count_max = 0

    def process(self, param, state):
        super(Hlt, self).process(param, state)
        print("")
        state.set_executing(False)


class Neg(Instructor):
    def __init__(self):
        Instructor.__init__(self)
        self.ins_name = "NEG"
        self.par_count_min = 0
        self.par_count_max = 0

    def process(self, param, state):
        super(Neg, self).process(param, state)
        state.set_mem(-state.get_mem())


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



