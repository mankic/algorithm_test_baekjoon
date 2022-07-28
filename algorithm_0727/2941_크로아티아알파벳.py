croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


input_string = input()

for i in croatia_list:
    if i in input_string:
        print(i)
        input_string