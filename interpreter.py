import instructor
import sys
import os


class Program:
    def __init__(self, original_text):
        ins = instructor.Instructor()
        self.state = State()
        self.instructors = ins.get_instructor_list()
        self.parsed_program = Parse(original_text).parse()

    def process_one(self):
        if self.state.executing:
            now_ins_num = self.state.ins_place
            try:
                for next_ins in self.instructors:
                    if self.parsed_program[now_ins_num][0] == next_ins.ins_name:
                        next_ins.process(self.parsed_program[now_ins_num][1],
                                         self.state)
                        break
            except IndexError:
                print('IndexError. Maybe you typed wrong instructor.')
                return 1
            if self.state.ins_place == now_ins_num:#if not jlz
                self.state.ins_place = now_ins_num + 2
                #now_ins_num + 1(next line) + 1(list starts from 0)
            return 0
        else:
            return 1

    @property
    def length(self):
        return len(self.parsed_program)


class State:
    def __init__(self):
        self.mem_place = 0
        self.mem_list = [0]
        self.executing = True
        self.__ins_place = 1
        self.output_list = []

    @property
    def mem(self):
        if self.mem_place > len(self.mem_list) - 1:
            to_append = self.mem_place - len(self.mem_list) + 1
            for i in range(to_append):
                self.mem_list.append(0)
        return self.mem_list[self.mem_place]

    @mem.setter
    def mem(self, value):
        if self.mem_place > len(self.mem_list) - 1:
            to_append = self.mem_place - len(self.mem_list) + 1
            for i in range(to_append):
                self.mem_list.append(0)
        self.mem_list[self.mem_place] = value

    @property
    def ins_place(self):
        return self.__ins_place - 1 #list starts from 0, and ins_place starts from 1

    @ins_place.setter
    def ins_place(self, value):
        self.__ins_place = value

    def __str__(self):
        def to_num(s, place):
            if place == self.mem_place:
                return s
            try:
                return int(s)
            except ValueError:
                try:
                    return float(s)
                except ValueError:
                    return s
        if self.mem_place >= len(self.mem_list):
            self.mem = 0
        mem_str = str(self.mem_list)[1:-1]
        mem_str_list = mem_str.split(", ")
        mem_str = str([to_num(x, i) for i, x in enumerate(mem_str_list)])
        
        return "memory = " + mem_str + "\nmem_place = " +\
               str(self.mem_place) + "\nins_place = " + str(self.ins_place + 1)


class ParseError(Exception):
    pass


class Parse:
    def __init__(self, original_text):
        self.text = original_text.split("\n")
        self.parsed = []

    def parse(self):
        for i, line in enumerate(self.text):
            to_append = []
            try:
                (ins_name, line_toparse) = line.split("(", 1)
            except ValueError:
                print("Warning : no opening bracket found in line", i)
                input("Press enter to continue...")
                os.system('cls' if os.name=='nt' else 'clear')
                pass
            to_append.append(ins_name.upper())
            is_character = False
            now_param = 0
            to_append.append([0])
            have_nothing = True
            is_token = False
            is_minus = False
            is_comment = False
            for next_char in line_toparse:
                if is_comment:
                    to_append[2] += next_char
                else:
                    if is_token:
                        if next_char == "\\":
                            to_append[1][now_param] += '\\'
                        elif next_char == 'n' or next_char == 'N':
                            to_append[1][now_param] += '\n'
                        elif next_char == "'":
                            to_append[1][now_param] += "'"
                        else:
                            raise ParseError("unexpected token " + next_char +
                                             " after \\ in line", i)
                        is_token = False
                    else:
                        if next_char == '\\':
                            is_token = True
                        if next_char == "'":
                            if is_character:
                                is_character = False
                            else:
                                is_character = True
                                to_append[1][now_param] = ''
                                have_nothing = False
                        elif next_char == ",":
                            if not is_character:
                                to_append[1].append(0)
                                now_param += 1
                                have_nothing = False
                                is_minus = False
                            else:
                                to_append[1][now_param] += ','
                        elif next_char == ")":
                            if not is_character:
                                if have_nothing:
                                    to_append[1] = []
                                is_comment = True
                                to_append.append('')
                            else:
                                to_append[1][now_param] += ")"
                        elif next_char == " ":
                            if not is_character:
                                pass
                            else:
                                to_append[1][now_param] += " "
                        elif next_char == "-":
                            if not is_character:
                                is_minus = True
                            else:
                                to_append[1][now_param] += "-"
                        else:
                            have_nothing = False
                            if is_character:
                                to_append[1][now_param] += next_char
                            elif not is_minus:
                                to_append[1][now_param] = to_append[1][now_param] *\
                                                          10 + int(next_char)
                            else:
                                to_append[1][now_param] = to_append[1][now_param] *\
                                                          10 - int(next_char)
            self.parsed.append(to_append)
        return self.parsed
