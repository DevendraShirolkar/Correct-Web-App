# from functions import get_todos, write_todos
# this is another way to call function file as module
import functions
import time

now = time.strftime("%b %d, %Y, %H %M %S")
print("Time is as below")
print("It is ",now)

while True:
    user_action = input('Type add, show, edit, complete or exit')
    user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            # item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number =number -1

            todos = functions.get_todos()
            new_todo = input("Enter the new todo")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            continue

    elif user_action.startswith("complete"):
        try:
            #case 'complete':
            number = int(user_action[9:])
            index = number - 1
            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            print('To do completed',todo_to_remove)
            todos.pop(index)
            functions.write_todos(todos)

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid')

print('Bye!')



# #####  This is a alternative code ######
#match user_action: # case add:
#with open('todo.txt', 'w') as file:
        #   todos = file.writelines(todos)
#file = open('todo.txt','r') Original code
        #todos = file.readlines()
        #file.close()
        # file = open('todo.txt','w')
        # file.writelines(todos)
        # file.close()
#case 'show':
        #file =open('todo.txt','r')
        #todos = file.readlines()
        #file.close()

        #with open('todo.txt','r') as file:
            #todos = file.readlines()
#case 'edit':

# with open('todo.txt','r') as file:
# todos = file.readlines()
# with open('todo.txt', 'w') as file:
# todos = file.writelines(todos)