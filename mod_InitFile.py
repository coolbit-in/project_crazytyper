# -*- coding:utf=8 -*-
import os
# def InitFile(path, x):
#    f = open(path, 'r')
#    line = f.read()
#    m = len(line)
#    n = m / x
#    next_line = line + ' '*((n+1)*x-m)
#    string = [None]*(n+1)
#    for i in range(n+1):
#        string[i] = next_line[i*x : (i*x + x)]
#        string[i] = string[i] + '\n'
#    new_line = ''.join(string)
#    g = open(os.getcwd() + '/files/tempfile.txt', 'w')
#    g.write(new_line)
#    g.close()
#    return os.getcwd() + '/files/tempfile.txt'


def InitFile(path):
    oriFile = open(path, "r")
    tmpFile = open(os.getcwd() + "/files/tempfile.txt", "w")
    tmpFile.write(oriFile.read().replace("\n", "↲\n"))
    tmpFile.close()
    return os.getcwd() + "/files/tempfile.txt"
