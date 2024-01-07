#Approch 1: 
# Step 1: Adding multiple input() functions and take all those inputs 
# Step 2: Add all these input's to list data type

user_prompt = "Enter a todo:"
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

# to know type of the variable
print(type(todo1))
#output: <class 'str'>

# create an empty list object
todos = []

print(type(todos))
#output: <class 'list'>

# Adding items using append function or [todo1, todo2, todo3]
todos.append(todo1)
todos.append(todo2)
todos.append(todo3)

print(todos)

#Problem with this approach is in real time: User doesnot know how many times he add or delete or update
#It should be dynamic and update this logic in such way that to work for any number of items.