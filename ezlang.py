from interpreter import *

if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage : python(.exe) ezlang.py your_file (d to debug)")
else:
    os.system('cls' if os.name=='nt' else 'clear')
    with open(sys.argv[1], 'r', encoding='utf8') as file:
        law_program = file.read()
    program = Program(law_program)
    if len(sys.argv) == 2:
        while True:
            is_finished = program.process_one()
            if is_finished == 1:
                break
    elif sys.argv[2] == 'd':
        while True:
            def print_():
                os.system('cls' if os.name=='nt' else 'clear')
                print("===STATE===")
                print(program.state)
                print()
                print("===OUTPUT===")
                print(program.state.output_list)
                print()
                print("==PROGRAM==")
                for i in range(-2, 3):
                    place = program.state.ins_place + i
                    if place < 0:
                        continue
                    if place >= program.length:
                        break
                    if i == 0:
                        print(">>> ", end='')
                    print(place + 1,
                          program.parsed_program[place])
                print()
                place = program.state.ins_place
                if place < program.length and\
                   program.parsed_program[place][0] == 'JLZ':
                    print("===Line " +\
                          str(program.parsed_program[place][1][0]) +\
                          "===")
                    for i in range(5):
                        place_new =\
                                  program.parsed_program[place][1][0] -\
                                  1 + i
                        if place_new >= program.length:
                            break
                        print(place_new + 1,
                              program.parsed_program[place_new])

            print_()
            input("Press enter to continue...")
            is_finished = program.process_one()
            if is_finished == 1:
                print_()
                break
    else:
        print("Usage : python(.exe) ezlang.py your_file (d to debug)")
