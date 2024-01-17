# print([i.strip(10) for i in [1,2,3]])
# gives "AttributeError: 'int' object has no attribute 'strip'"

# Working solution
old = [1,2,3]
new = [i+10 for i in old]
print(new)

# gives this error "SyntaxError: invalid syntax"
#print([for i in old i+10])

names = ["john smith", "jay santi", "eva kuki"]
capitalizeNames = [name.title() for name in names]
print(capitalizeNames)
#output : ['John Smith', 'Jay Santi', 'Eva Kuki']

names = ["john smith", "jay santi", "eva kuki"]
capitalizeNames = [name.capitalize() for name in names]
print(capitalizeNames)
#output : ['John smith', 'Jay santi', 'Eva kuki']

# Convert eact time from int to string and added a new line to each entry
temperatures = [10, 12, 14]
temperatures = [str(temp)+'\n' for temp in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)

# convert float to int
'''
numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for item in numbers] => It's a wrong code and we get an error
print(numbers)
'''
numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)