with open('pi.txt') as file_object:
    lines = file_object.readlines()

restri = ''
for i in lines:
    restri += i.rstrip()

filename = 'programming.txt'
with open(filename, 'a') as f_object:
    f_object.write('\n I like Python')
