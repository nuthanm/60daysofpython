# Demo on how to use match case
# This is available from python 3.10 plus version
# similar like switch in c#

# Create a new empty array
todos = []


while True:
    user_action = input("Todo App: add, show or exit : ")

    match user_action:
        case "add": 
            user_input = input("Add a new todo item: ")
            todos.append(user_input)
        case "show":
            print(todos)
        case "exit":
            break

print("Catch up soon!!!")

