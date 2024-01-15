# Storing data in file app

# Create a new todos empty list array
# todos = [] - reading existing data in todos.txt file and assign it to todos
file = open('todos.txt', 'r')
todos = file.readlines()
file.close()
           
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
            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case "edit":
            user_input_index = int(input("Which item you want to modify? "))
            updated_text = input("Please enter updated item: ")
            todos[user_input_index - 1] = updated_text
        case "show":
            for index, item in enumerate(todos):
                print(f"{index + 1}.{item.capitalize()}")
        case "complete":
            user_input_delete_index = int(input("Which item you want to set it as complete: "))
            todos.pop(user_input_delete_index - 1)
        case "exit":
            break

print("Will catchup soon!!!")