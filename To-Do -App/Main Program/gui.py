import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue11")

clock= sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box =sg.InputText(tooltip="Enter to Do", key='Todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='Todos',
                      enable_events=True,
                      size=[35,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout =300)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['Todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['Todos'][0]
                new_todo = values['Todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['Todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))

        case 'Todos':
            window['Todo'].update(value=values['Todos'][0])

        case 'Complete':
            try:
                todo_to_complete = values['Todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['Todo'].update(value="")
            except IndexError:
                sg.popup('Please select an item first', font=('Helvetica', 20))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break
window.close()
