user_input = "Enter a todo:"

# 1==1, 2>1, True => All these cases are infinite loop
# Infinite user inputs because 1 is always match with 1
#while 1==1:
#    print(input(user_input))

i = 0
todos = []
while i<=1:
    todo = input(user_input)
    todos.append(todo)
    i = i + 1

print(todos)

'''
while True:
    user_name = input("What is your name? ")
    print(user_name.capitalize())
'''