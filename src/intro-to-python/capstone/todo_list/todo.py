# Use this file as your main entrypoint for your program

import sys

FILENAME = "TODO_LIST.txt"
todo_list = []

def readinfile():
    try:
        f = open(FILENAME, "r")
        line = f.readline()
        while line:
            todo_list.append(line)
            line = f.readline()
    except IOError:
        f = open(FILENAME, "a")
    finally:
        f.close()
    

def writetofile():
    f = open(FILENAME, "w")
    for i in todo_list:
        f.write(i)
    f.close()


def create(tasks):
    readinfile()
    for task in tasks:
        todo_list.append(task + "\n")
    writetofile()


def read():
    readinfile()
    for i in todo_list:
        print(i, end="")
    




def main(inputs):
    if inputs[1] == "create":
        create(inputs[2:])
    elif inputs[1] == "list-all":
        if inputs[2] == "--substring":
            readsubstring()
        # read()
        elif inputs[2] == "--complete": 
            readcomplete()
    else:
        "Print Not A Valid Input"


if __name__ == '__main__':
    main(sys.argv)

