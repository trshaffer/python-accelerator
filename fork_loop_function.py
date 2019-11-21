#!/usr/bin/env python3
#This file contains the tested fork loop and eval combo.
#
#  How this process should run
#  1) TODO: collect imports
#  2) fork and eval function
#  3) TODO: colect output   
#
# This child process uses the compile() builtin method to take the function call 
#  and change it into an AST string for the eval()
#
#TODO: Find a way to hold onto the return of the function.
#  Current ideas: 1) Thunk function (Tim's idea)
#                 2) Pipe into globals (?) 
import os
import sys

test_gloabl = 77
return_val = None

def read_imports(file_name):
    source = open(file_name, "r")
    for line in source.readlines():
        line = line.rstrip()
        if line == "":
            continue
        words = line.split()
        if words[0][0] == '#':
            continue
        if words[0] != "from" and words[0] != "import":
            break
        exec(line)
    

for i in range(1, 5):
    read_imports('test_file.py')
    pid = os.fork()
    if pid == 0:
        func_test = open('test_file.py')
        read_test = func_test.read()
        # Convert read-in function into an AST
        comp_test = compile(read_test, 'test_file.py', 'exec')
        #print(comp_test)
        eval(comp_test, globals(), locals())
        #print(return_val)       
        exit(0)
    else:
        childProcExit = os.waitpid(pid, 0)
        print("Exit value: ", childProcExit[1] >> 8)

