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
        if self.state.get_executing():
            now_ins_num = self.state.get_instructor_place()
            try:
                for next_ins in self.instructors:
                    if self.parsed_program[now_ins_num][0] == next_ins.ins_name:
                        next_ins.process(self.parsed_program[now_ins_num][1], self.state)
                        break
            except IndexError:
                print('IndexError. Maybe you typed wrong instructor.')
                return 1
            if self.state.get_instructor_place() == now_ins_num:#if not jlz
                self.state.set_instructor_place(now_ins_num + 2)#now_ins_num + 1(next line) + 1(list starts from 0)
            return 0
        else:
            return 1


class State:
    def __init__(self):
        self.mem_place = 0
        self.mem_list = [0]
        self.now_executing = True
        self.ins_place = 1
        self.output_list = []

    def get_mem_place(self):
        return self.mem_place

    def set_mem_place(self, place):
        self.mem_place = place

    def get_mem(self):
        if self.mem_place > len(self.mem_list) - 1:
            to_append = self.mem_place - len(self.mem_list) + 1
            for i in range(to_append):
                self.mem_list.append(0)
        return self.mem_list[self.mem_place]

    def set_mem(self, value):
        if self.mem_place > len(self.mem_list) - 1:
            to_append = self.mem_place - len(self.mem_list) + 1
            for i in range(to_append):
                self.mem_list.append(0)
        self.mem_list[self.mem_place] = value

    def get_executing(self):
        return self.now_executing

    def set_executing(self, value):
        self.now_executing = value

    def get_instructor_place(self):
        return self.ins_place - 1#list starts from 0, and ins_place starts from 1

    def set_instructor_place(self, value):
        self.ins_place = value

    def __str__(self):
        return str(self.mem_list) + "\nmem_place = " + str(self.mem_place) + "\nins_place = " + str(self.ins_place)


class ParseError(Exception):
    pass


class Parse:
    def __init__(self, original_text):
        self.text = original_text.split("\n")
        self.parsed = []

    def parse(self):
        for line in self.text:
            to_append = []
            (ins_name, line_toparse) = line.split("(", 1)
            to_append.append(ins_name.upper())
            is_character = False
            now_param = 0
            to_append.append([0])
            have_nothing = True
            is_token = False
            is_minus = False
            for next_char in line_toparse:
                if is_token:
                    if next_char == "\\":
                        to_append[1][now_param] += '\\'
                    elif next_char == 'n' or next_char == 'N':
                        to_append[1][now_param] += '\n'
                    elif next_char == "'":
                        to_append[1][now_param] += "'"
                    else:
                        raise ParseError("unexpected char " + next_char + " after \\")
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
                            break
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
                            to_append[1][now_param] = to_append[1][now_param] * 10 + int(next_char)
                        else:
                            to_append[1][now_param] = to_append[1][now_param] * 10 - int(next_char)
            self.parsed.append(to_append)
        return self.parsed


if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage : python(.exe) interpreter.py your_file (d to debug)")
else:
    os.system('cls')
    with open(sys.argv[1]) as file:
        law_program = file.read()
    program = Program(law_program)
    if len(sys.argv) == 2:
        while True:
            is_finished = program.process_one()
            if is_finished == 1:
                break
    elif sys.argv[2] == 'd':
        print(program.state)
        print(program.state.output_list)
        print(program.parsed_program[program.state.get_instructor_place()])
        os.system('pause')
        os.system('cls')
        while True:
            is_finished = program.process_one()
            if is_finished == 1:
                os.system('cls')
                print(program.state)
                print(program.state.output_list)
                print(program.parsed_program[program.state.get_instructor_place()])
                break
            print(program.state)
            print(program.state.output_list)
            print(program.parsed_program[program.state.get_instructor_place()])
            os.system('pause')
            os.system('cls')
    else:
        print("Usage : python(.exe) interpreter.py your_file (d to debug)")