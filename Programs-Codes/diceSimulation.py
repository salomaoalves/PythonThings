'''Simulates dice from a board game and can play then N times'''
import numpy as np

def playDice(f):
    number = np.random.choice(a=range(f),size=1)
    return number[0]+1

def main():
    f = int(input("How many face: "))
    m = int(input("How many moves do you want to make: "))
    for i in range(m):
        print("Move",i)
        print(playDice(f))

main()