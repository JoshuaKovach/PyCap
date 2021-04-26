# Use this file as your main entrypoint for your program

import sys
import json
import os

from pathlib import Path
from typing import Optional
import typer

app = typer.Typer()


FILENAME = "TODO_LIST.txt"




# class Task:
#     def __init__(self,description,complete):
#         self.description = description
#         self.complete = complete
        

#Where test code for JSON is going
def test(dummy):
    todo_list = []
    # foo = Task("Walk the Dog", 0)
    # bar = Task("Take the Washing Out", 0)
    foo = {"description": "Walk the Dog", "complete": 0}
    bar = {"description": "Take the Washing Out", "complete": 0}

    todo_list.append(foo)
    todo_list.append(bar)

    
        # json.dump(bar.__dict__, outfile)
    
    
    # print(data["complete"])       


#A function to read my txt file into todo_list
def readinfile(todo_list):
   
    try:
        f = open(FILENAME, "r")
        if os.stat(FILENAME).st_size != 0:
            todo_list = json.load(f)
            # with open (FILENAME) as f:
            #     todo_list = json.load(f)
    except IOError:
        f = open(FILENAME, "a")
        
    finally:
        f.close()
    return todo_list


#A function to write to todo_list
def writetofile(todo_list):
    with open(FILENAME,'w') as outfile:
        json.dump(todo_list, outfile)
    


#Function to add tasks to and external txt
# @app.command()
def create(todo_list,tasks):
    # todo_list = []
    # todo_list = readinfile(todo_list)
    for task in tasks:
        todo_list.append({"description": task, "complete": 0})
    writetofile(todo_list)

#Read ToDo List
def read(todo_list):
    
    for task in todo_list:
        print(task["description"])
    

#Read a substring from an external txt and display the substring if it exists
def readsubstring(todo_list, substring):
    
    found = False
    for task in todo_list:
        if (task["description"].find(substring) != -1):
            print(task["description"])
            found = True

    if not found:
        print("Substring does not exist")    
        
def deleteall(todo_list):
    open(FILENAME,'w').close()
 
#Main function, runs through inputs
def main(inputs):
    todo_list = []
    todo_list = readinfile(todo_list)
    if inputs[1] == "create":
        create(todo_list, inputs[2:])
    elif inputs[1] == "list-all":
        if len(inputs) > 2:
            if inputs[2] == "--substring":
                readsubstring(todo_list, inputs[3])
            # read()
            elif inputs[2] == "--complete": 
                readcomplete(todo_list)
            else:
                print("Unlucky")
        else:
            read(todo_list)
    elif inputs[1] == "delete-all":
        deleteall(todo_list)
    else:
        print("Not A Valid Input")

#Not sure, but helps work
if __name__ == '__main__':
    main(sys.argv)









# if __name__ == "__main__":
#     app()