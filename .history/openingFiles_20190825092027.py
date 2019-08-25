
f = open('myfile.txt', 'w')
f.write('Hello')
f.write(' ')
f.clse()


f = open('myfile.txt', 'a')
f.write('Python')
f.write(' ')
f.write(str(2019))
f.close()


f = open('myfile.txt', 'r')
line = f.readline()
print(line)

print(line.split(' '))

print(int('1'))  # int('1') -> 1
