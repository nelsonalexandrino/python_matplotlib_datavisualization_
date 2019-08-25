
f = open('myfile.txt', 'w')
f.write('Hello')
f.write(' ')
f.close()


f = open('myfile.txt', 'a')
f.write('Python')
f.write(' ')
f.write(str(2019))
f.close()


f = open('myfile.txt', 'r')
line = f.readline()
print(line)
f.close()

print(line.split(' '))
