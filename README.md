# EZLang
EZLang, 'easy' esoteric programming language

Have four feauture : 
 - Sentiency
 - Convenience
 - Readability
 - Expendability

## Instructors
Can read Korean? [My blog link here.](https://dhnam0502.blog.me/221068174333)

Like turing machine, memory with infinite size is provided.

There are 7 instructors in EZLang

 1. MEM(N, U = 0). Go to `N`th memory. If `U` is 1, Go to +`N`th memory. Use like `MEM(3)` or `MEM(1, 1)`
 2. SET(V, U = 0). Set current memory to `V`. If `U` is 1, Add `V` to current memory. Use like `SET(5)` or `SET(-1, 1)`
 3. JLZ(N). Jump to `N`th instructor if current memory is less than zero. Use like `JLZ(3)`. Note that first line is 1, not 0.
 4. GET(C = 0). Get a number and set current memory to the number. if `C` is 1, Get a character and set current memory to unicode number of the character.
 5. PRT(C = 0). Same as `GET`, but not get but print.
 6. HLT(). Halt program.
 7. NEG(). Save negative number to current memory.
 
...And anything following `)` is comment.

## Example

This is program which get two numbers for input, and print sum of the numbers.
```
MEM(0) plus. when first made this language
SET(-1)
MEM(1)
GET()
MEM(2)
GET()
MEM(1)
SET(-1, 1)
JLZ(14)
MEM(2)
SET(1, 1)
MEM(0)
JLZ(7)
MEM(2)
PRT()
HLT()
```

## How to use?

`python(.exe) ezlang.py your_file (d to debug)`

## How to write new instructor?

First, make new class with this format : 
```
    class Yourclass(Instructor):
        def __init__(self):
            self.ins_name = "(name)"
            self.par_count_min = 0 # minimum parameter
            self.par_count_max = 0 # maximum parameter
        def process(self, param, state):
            super(Yourclass, self).process(param, state)
            #and your code
```

Second, write your code. You can access to variables with `state.variable`.

There is five variable you can access, `mem_place`, `mem_list`, `excuting`, `ins_place`(When get, it is 0-based, and when set, it is 1-based.), `output_list`, `mem`(current memory)

Third, add your new instructor in `get_instructor_list` method of `Instructor` class.

Done!
