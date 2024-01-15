contents = ["firstfile","secondfile","thirdfile"]
filenames = ["file1.txt","file2.txt","file3.txt"]

# Option 1
'''
for content in contents:
    for fileName in filenames:
        file = open(fileName, 'w')
        file.writelines(content)
        filenames.pop(0)
        break
'''
# Option 2
for content, fileName in zip(contents, filenames):
    file = open(fileName, 'w')
    file.writelines(content)
    file.close()