'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
inp = input().split()
queue = deque([ [inp[i], i+1] for i in range(len(inp)) ] )

i = 0
while len(queue) > 0 :
    tmp = queue.popleft()
    print(tmp[1], end = " ")
    #print(queue)
    tp = int(tmp[0])
    if tp > 0:
        tp=tp-1
    queue.rotate(-int(tp))
    