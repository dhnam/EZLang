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
        print(program.state)
        print(program.state.output_list)
        print(program.parsed_program[program.state.ins_place])
        while True:
            input("Press enter to continue...")
            os.system('cls' if os.name=='nt' else 'clear')
            is_finished = program.process_one()
            if is_finished == 1:
                os.system('cls' if os.name=='nt' else 'clear')
                print(program.state)
                print(program.state.output_list)
                print(program.parsed_program[program.state.ins_place])
                break
            print(program.state)
            print(program.state.output_list)
            print(program.parsed_program[program.state.ins_place])
    else:
        print("Usage : python(.exe) ezlang.py your_file (d to debug)")
