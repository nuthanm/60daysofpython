# Demo on how to use with context manager
# Dispose automatically when we use with
# Similar like using block in c#

# Storing data in file app

# Create a new todos empty list array
# todos = [] - reading existing data in todos.txt file and assign it to todos

# Traditional approch
'''
file = open('todos.txt', 'r')
todos = file.readlines()
file.close()
'''

with open('todos.txt', 'r') as file:
    todos = file.readlines()
           
# Create a file object
# file = open('todos.txt','w')

# Until you break the loop this will ask you to choose the action
while True:
    user_action = input("Todo App - Please select your action: add, edit, complete, show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            user_input = input("Add your todo item: ") + "\n"
            todos.append(user_input)
            #todos.append(f"{len(todos) + 1}.{user_input}")
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case "edit":
            user_input_index = int(input("Which item you want to modify? "))
            updated_text = input("Please enter updated item: ")
            todos[user_input_index - 1] = updated_text
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case "show":
            new_todos = []
            #traditonal approach
            '''for item in todos:
                item = item.strip('\n')
                new_todos.append(item)
            '''
            #list comprehension
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item.capitalize()}")
        case "complete":
            user_input_delete_index = int(input("Which item you want to set it as complete: "))
            todos.pop(user_input_delete_index - 1)
            with open('todos.txt','w') as file:
                file.writelines(todos)
        case "exit":
            break

print("Will catchup soon!!!")
