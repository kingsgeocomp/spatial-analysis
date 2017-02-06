import random

#    for i in range(100):
#        print '%.6f' % random.random(), '%.6f' % random.random()

file = open('random_points.txt', 'w')

for i in range(100):
    file.write('%.6f' % random.random())
    file.write('%.6f' % random.random())
    file.write("\n")

file.close()
