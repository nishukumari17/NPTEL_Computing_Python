# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 12:28:18 2025

@author: Nishu
"""
import random
def choose():
    words=["rainbow","water","jar","mathematics","player","condition","reverse","science","computer""board" ]
    pick=random.choice(words)
    return pick

def jumble(word):
      jumbled="".join(random.sample(word,len(word)))
      return jumbled

def play():
    p1name=input("Player 1, Please enter your name:")
    p2name=input("Player 2, Please enter your name:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #player1
        if(turn%2==0):
            print(p1name,"Your turn .")
            ans=input("What is on my mind: ")
            if ans==picked_word:
                pp1=pp1+1
                print("Your score is : ",pp1)
            else:
                print("Better luck nxt time. I thought ",picked_word)
            c=int(input("Press 1 to continue and 0 to quit"))
            if c==0:
                print("thank",p1name,p2name,pp1,pp2)
                break
        #player2
        else:
            print(p2name,"Your turn .")
            ans=input("What is on my mind: ")
            if ans==picked_word:
                pp2=pp2+1
                print("Your score is : ",pp2)
            else:
                print("Better luck nxt time. I thought ",picked_word)
            c=int(input("Press 1 to continue and 0 to quit"))
            if c==0:
                print("thank",p1name,p2name,pp1,pp2)
                break
        turn=turn+1
            
play()