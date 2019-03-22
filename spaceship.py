import random
import turtle
from operator import itemgetter
import os

def pickword():
    
    try:
        f=open("wordlist.txt","r")
        target_word = random.choice(f.readlines()).strip()
        # call the draw function to write down the spaces
        return target_word
        f.close()
        
    except IOError as err:
        print('Error: can\'t find file or read data.')
    
        

def spaceship(wrong_count):
    
    ship=turtle.Turtle()
    ship.hideturtle()
    if wrong_count==1:
        #draw the body
        
        ship.penup()
        ship.goto(0,175)
        ship.pendown()
        ship.goto(-50,100)
        ship.goto(-50,-100)
        ship.goto(50,-100)
        ship.goto(50,100)
        ship.goto(0,175)
        

    if wrong_count==2:
        #draw the left rocket
        ship.penup()
        ship.goto(-70,-50)
        ship.pendown()
        ship.goto(-40,-130)
        ship.goto(-100,-130)
        ship.goto(-70,-50)
        
    if wrong_count==3:
        #draw the right rocket
        ship.penup()
        ship.goto(70,-50)
        ship.pendown()
        ship.goto(40,-130)
        ship.goto(100,-130)
        ship.goto(70,-50)

    if wrong_count==4:
        #draw the left flame
        ship.penup()
        ship.goto(-100,-130)
        ship.pendown()
        ship.goto(-90,-150)
        ship.goto(-80,-130)
        ship.goto(-70,-160)
        ship.goto(-60,-130)
        ship.goto(-50,-150)
        ship.goto(-40,-130)

    if wrong_count==5:
        #draw the right flame
        ship.penup()
        ship.goto(100,-130)
        ship.pendown()
        ship.goto(90,-150)
        ship.goto(80,-130)
        ship.goto(70,-160)
        ship.goto(60,-130)
        ship.goto(50,-150)
        ship.goto(40,-130)

#draw blank space according to the number of letters
def blank_spaces(word):
    blk_spc = turtle.Turtle()
    blk_spc.hideturtle()

    for i in range(len(word)):
        blk_spc.penup()
        blk_spc.goto((100+30*i),-150)
        blk_spc.pendown()
        blk_spc.goto((120+30*i),-150)

#if answer correctly, draw corresponding position
def right_guess(char,pos):
    dra_ch = turtle.Turtle()
    dra_ch.hideturtle()
    dra_ch.penup()
    dra_ch.goto((105+pos*30),-145)
    dra_ch.pendown()
    dra_ch.write(char,move=False,align="left",font=("Arial","16","normal"))
    
#if answer wrong,put to the left side of the spaceship
def wrong_guess(char,pos):
    dra_wrg = turtle.Turtle()
    dra_wrg.hideturtle()
    dra_wrg.penup()
    dra_wrg.goto(-210+pos*20,-150)
    dra_wrg.pendown()
    dra_wrg.write(char,move=False,align="right",font=("Arial","16","normal"))



    
def playgame(win_total):
    
    target_word = pickword()
    left_word=target_word
    count=0
    cha_list = list(target_word)
    blank_spaces(target_word)
    while count < 5:
        #prompt user for the guess for the letter
        guess = input("Guess a letter")
        letter = guess.lower()
        
        if len(guess)>=2:
            continue

        #if the guess is correct
        if letter in cha_list:
            #draw the char in the corresdonding position
            for pos in range(len(cha_list)):
                if letter == cha_list[pos]:
                    right_guess(letter,pos)
                    left_word = left_word.replace(letter,"")
            if len(left_word)==0:
                break
                
            
        if letter not in cha_list:
            #draw the char in the turtle page
            #draw parts in the spaceship  
            count += 1
            wrong_guess(letter,count)
            spaceship(count)
            
    if len(left_word) == 0:
        #this means they win
        win_total += 1
    
        print("You Win!\nYou have won",win_total,"games so far\n")
    else:
        print('You lose,sorry\nThe word is '+ target_word)

    #ask user if they want to play again
    play_again = input("Play again? Enter Y/N")
    if play_again =='Y':
       
        turtle.clearscreen()
        playgame(win_total)
    else:
        return win_total
           
        

def scores(win_total):
    try:
        win_total=int(win_total)
        name = input("Enter your name for posterity")
        #append the name and the win_total to file put into file
        # reoprn keep the info
        if os.stat("scores.txt").st_size==0:
            f=open("scores.txt","w+")
       
            f.write(name+" "+str(win_total)+"\n")

            f.close()
        

        else:
            f=open("scores.txt","r")
            score_list = [i.strip().split() for i in f.readlines()]
            score_list.append([name,str(win_total)])
    
    
            max_infile =int(score_list[0][1])
            if win_total > max_infile:
                score_list[0],score_list[len(score_list)-1] = score_list[len(score_list)-1],score_list[0]
   
            f=open("scores.txt","w+")
            for sub_score in score_list:
                f.write(sub_score[0]+" "+str(sub_score[1])+"\n")


            f.close()
            #write to the file
    except IOError as err:
        print('Error: can\'t find file or read data.')
            





