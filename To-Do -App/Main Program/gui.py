import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box =sg.InputText(tooltip="Enter to Do", key='Todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='Todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box, add_button],[list_box,edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['Todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['Todo']
            todos.append(new_todo)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break
        case "Edit":
            todo_to_edit = values['Todos'][0]
            new_todo = values['Todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
        case 'Todos':
            window['Todo'].update(value=values['Todos'][0])





window.close()
