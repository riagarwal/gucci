#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:30:41 2020

@author: rishabhagarwal
"""
 #Starting up of Game

GameResult=str()    
XOfirst=str()
XOsecond=str()
c = input("Would you like to play with X's or O's: ")
d = input('Would you like to play 1st or 2nd: ')
if d.lower()=='1st' or d.lower()=='first' and c.upper() == 'X':
    XOfirst = 'X'
    XOsecond= 'O'
elif d.lower()=='1st' or d.lower()=='first' and c.upper() == 'O':
    XOfirst = 'O'
    XOsecond= 'X'
elif d.lower()=='2nd' or d.lower()=='second' and c.upper() == 'X':
    XOfirst='O'
    XOsecond= 'X'
elif d.lower()=='2nd' or d.lower()=='second' and c.upper() == 'O':
    XOfirst = 'X'
    XOsecond= 'O'
 #Loop of game
i = 0;
a = ' '
b = ' '
cd = ' '
w = ' '
cv = ' '
e = ' '
bb = ' '
bc = ' '
bd = ' '


boxin = str()
Playvar = ' '
while GameResult != 'Done':
    i = i+1
    if i % 2 == 1:
        boxin=input("What box do you want to play: ")
        if boxin == "1":
            a = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '2':
            b = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin  == '3':
            cd= XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin== '4':
            w = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '5':
            cv = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '6':
            e = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '7':
            bb = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '8':
            bc = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '9':
            bd = XOfirst
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
    elif i % 2 == 0:
        boxin=input("What box do you want to play: ")
        if boxin == "1":
            a = XOsecond 
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '2':
            b = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin  == '3':
            cd= XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin== '4':
            w = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '5':
            cv = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '6':
            e = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '7':
            bb = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '8':
            bc = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
        if boxin == '9':
            bd = XOsecond
            print('   |   |   ')
            print(f' {a} | {b} | {cd} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {w} | {cv} | {e} ')
            print('___|___|___')
            print('   |   |   ')
            print(f' {bb} | {bc} | {bd} ')
            print('   |   |   ')
    if a == 'X' or a == 'O':
        if a == b and b == cd:
            print('Winner')
            Playvar = input("Would you like to play again: ")
        elif a == cv and cv == bd:
            print('Winner')
            Playvar = input("Would you like to play again: ")
        elif a == w and w == bb:
            print('Winner')
            Playvar = input("Would you like to play again: ")
    if b == 'X' or b == 'O':
        if b == cv and cv == bc:
            print('Winner')
            Playvar = input("Would you like to play again: ")
    if cd == 'X' or cd == 'O':
        if cd == e and e == bd:
            print('Winner')
            Playvar = input("Would you like to play again: ")
        elif cd == cv and cv == bb:
            print('Winner')
            Playvar = input("Would you like to play again: ")
    if w == 'X' or w == 'O':
        if w == cv and cv == e:
            print('Winner')
            Playvar = input("Would you like to play again: ")
    if bd== 'X' or bd == 'O':
        if bd == bc and bc == bb:
            print('Winner')
            Playvar = input("Would you like to play again: ")
    alist = list([a,b,cd,w,cv,e,bb,bc,bd])
    if ' ' not in alist:
        if Playvar == ' ':
            print("Draw")
            i = 0;
            a = ' '
            b = ' '
            cd = ' '
            w = ' '
            cv = ' '
            e = ' '
            bb = ' '
            bc = ' '
            bd = ' '
            Playvar = input("Would you like to play again: ")
    if Playvar.lower() == "yes" or Playvar.lower() == 'y':X
    
        i = 0;
        a = ' '
        b = ' '
        cd = ' '
        w = ' '
        cv = ' '
        e = ' '
        bb = ' '
        bc = ' '
        bd = ' '
        Playvar = ' '
    elif Playvar.lower() == "no" or Playvar.lower() == 'n':
        GameResult = 'Done'
        break
        
            
        
            
            
                
                
            
        
        
    
    
    