// Author: Petrov Sergey
// Random key distribution for not great 1000 students
M = 1000
from random import choice
fin = open('input.txt','r')
fout = open('output.txt','w')
s = list(range(M))
for i in fin:
    x = choice(s)
    s.remove(x)
    fout.write('{:03d}'.format(x)+'\n')
fin.close()
fout.close()
s = input()