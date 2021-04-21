# Use this file as your main entrypoint for your program

import sys
import json

FILENAME = "TODO_LIST.txt"
todo_list = []


# class Task:
#     def __init__(self,description,complete):
#         self.description = description
#         self.complete = complete
        


def test(dummy):
    # foo = Task("Walk the Dog", 0)
    # bar = Task("Take the Washing Out", 0)
    # foo = {"description": "Walk the Dog", "complete": 0}
    # bar = {"description": "Take the Washing Out", "complete": 0}

    # todo_list.append(foo)
    # todo_list.append(bar)

    # with open(FILENAME,'w') as outfile:
    #     json.dump(todo_list, outfile)
    #     # json.dump(bar.__dict__, outfile)
    readinfile()
    # print(todo_list[1]["complete"])
    # print(data["complete"])       


def readinfile():
    # with open (FILENAME) as f:
    #     data = json.load(f)
    # todo_list = data
    # print(todo_list[1]["complete"])
    ###JSON ABOVE

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
    


def readsubstring(substring):
    readinfile()
    found = False
    for task in todo_list:
        if (task.find(substring) != -1):
            print(task)
            found = True

    if not found:
        print("Substring does not exist")    
        
    
 

def main(inputs):
    if inputs[1] == "create":
        create(inputs[2:])
    elif inputs[1] == "list-all":
        if len(inputs) > 2:
            if inputs[2] == "--substring":
                readsubstring(inputs[3])
            # read()
            elif inputs[2] == "--complete": 
                readcomplete()
            else:
                print("Unlucky")
        else:
            read()
    else:
        print("Not A Valid Input")


if __name__ == '__main__':
    main(sys.argv)