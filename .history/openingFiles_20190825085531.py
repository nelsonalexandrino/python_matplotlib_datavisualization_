
f = open('myfile.txt', 'w')
f.write('Hello')
f.close()


f = open('myfile.txt', 'a')
f.write('Python')
f.close()


f = open('myfile.txt', 'r')
line = f.readline()
print(line)
f.close()
