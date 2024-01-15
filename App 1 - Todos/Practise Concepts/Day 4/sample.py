#input
waiting_list = ['nani','arav','sobha','arjun']

#Expected output
'''
1.Arav
2.Arjun
3.Nani
4.Sobha

Capitalise, sorting, sequence of numbers
'''
waiting_list.sort()
for index, item in enumerate(waiting_list):
    print(f"{index + 1}.{item.capitalize()}")

print('Now descending')
waiting_list.sort(reverse=True)
for index, item in enumerate(waiting_list):
    print(f"{index + 1}.{item.capitalize()}")
