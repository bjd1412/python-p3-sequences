#!/usr/bin/env python3

def print_fibonacci(length):
    i = [0, 1, 1, 2]
    while len(i) < length:
        fibo = i[-1] + i[-2]
        i.append(fibo)
    print(i[:length])    

