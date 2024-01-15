# Demo on how to enumerate and fstrings
# enumerate function we use to change the output from 
'''
listItem
  listItem
  listeItem

to

1 listItem
2 listItem
3 listeItem
'''
'''
 in output: 0 . nani
 why there is a gap between index and text
 this issue solves using fstrings

 Syntax: f"{variable1}-{variable2}"
 '''

# Create a new empty array
todos = []


while True:
    user_action = input("Todo App: add, edit, complete, show or exit : ")
    user_action = user_action.strip() # similar like trim() in c#
    match user_action:
        case "add": 
            user_input = input("Add a new todo item: ")
            todos.append(user_input)
        case "edit" | 'edit' : # both pattern works
            index = int(input("Which item do you want to edit? : "))
            editText = input("Enter your updated text: ")
            todos[index - 1] = editText
        case "show":
            for index, todo in enumerate(todos):
                print(f"{index + 1}.{todo}")
        case "complete":
            item_to_delete = int(input("Which todo is complete? "))
            todos.pop(item_to_delete - 1)
        case "exit":
            break

print("Catch up soon!!!")

